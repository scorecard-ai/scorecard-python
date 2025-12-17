"""Wrapper for OpenAI and Anthropic SDKs to automatically trace LLM calls."""

from __future__ import annotations

import os
import json
import inspect
import threading
from typing import TYPE_CHECKING, Any, TypeVar, Optional, Sequence
from typing_extensions import override

from opentelemetry import trace
from opentelemetry.context import Context
from opentelemetry.sdk.trace import Span, ReadableSpan, SpanProcessor, TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import SpanExporter, SpanExportResult, BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

from .._exceptions import ScorecardError

if TYPE_CHECKING:
    from typing_extensions import TypedDict

    class WrapConfig(TypedDict, total=False):
        """Configuration for wrapping LLM SDKs."""

        api_key: Optional[str]
        """Scorecard API key. Defaults to SCORECARD_API_KEY env var."""

        project_id: Optional[str]
        """Project ID to associate traces with. Defaults to SCORECARD_PROJECT_ID env var."""

        service_name: Optional[str]
        """Service name for telemetry. Defaults to "llm-app"."""

        endpoint: Optional[str]
        """OTLP endpoint. Defaults to "https://tracing.scorecard.io/otel/v1/traces"."""

        max_export_batch_size: Optional[int]
        """Maximum batch size of spans to be exported. Defaults to 1."""


_ClientT = TypeVar("_ClientT")


class _SpanWrapper(ReadableSpan):
    """Wrapper that returns a modified resource for a span."""

    def __init__(self, span: ReadableSpan, new_resource: Resource):
        self.__span = span
        self.__resource = new_resource

    @property
    @override
    def resource(self) -> Resource:
        """Return the modified resource."""
        return self.__resource

    def __getattr__(self, name: str) -> Any:
        """Delegate all other attributes to the wrapped span."""
        return getattr(self.__span, name)

    @override
    def __setattr__(self, name: str, value: Any) -> None:
        """Delegate attribute setting to the wrapped span, except for internal attributes."""
        if name in ("_SpanWrapper__span", "_SpanWrapper__resource"):
            object.__setattr__(self, name, value)
        else:
            setattr(self.__span, name, value)


class ScorecardExporter(SpanExporter):
    """Custom exporter that injects projectId from span attributes into ResourceAttributes."""

    def __init__(self, endpoint: str, headers: dict[str, str]):
        self._otlp_exporter = OTLPSpanExporter(endpoint=endpoint, headers=headers)

    @override
    def export(self, spans: Sequence[ReadableSpan]) -> SpanExportResult:
        """Export spans after injecting scorecard.* attributes into resource."""
        modified_spans: list[ReadableSpan] = []
        for span in spans:
            result_span: ReadableSpan = span
            if span.attributes is not None:
                # Collect all scorecard.* attributes from span attributes
                scorecard_attrs = {key: value for key, value in span.attributes.items() if key.startswith("scorecard.")}

                if scorecard_attrs:
                    # Merge all scorecard.* attributes into the resource
                    # Use Resource() directly to avoid resource detectors during shutdown
                    scorecard_resource = Resource(attributes=scorecard_attrs)
                    new_resource = span.resource.merge(scorecard_resource)
                    # Wrap the span with modified resource
                    result_span = _SpanWrapper(span, new_resource)

            modified_spans.append(result_span)

        return self._otlp_exporter.export(modified_spans)

    @override
    def shutdown(self) -> None:
        """Shutdown the exporter."""
        self._otlp_exporter.shutdown()  # type: ignore


class CompositeProcessor(SpanProcessor):
    """Composite processor that manages multiple batch processors."""

    def __init__(self) -> None:
        self.__processors: dict[str, BatchSpanProcessor] = {}

    def add_processor(self, api_key: str, endpoint: str, max_export_batch_size: int) -> None:
        """Add a processor for the given API key and endpoint."""
        key = f"{api_key}:{endpoint}"
        if key in self.__processors:
            return

        exporter = ScorecardExporter(endpoint=endpoint, headers={"Authorization": f"Bearer {api_key}"})
        processor = BatchSpanProcessor(exporter, max_export_batch_size=max_export_batch_size)
        self.__processors[key] = processor

    @override
    def on_start(self, span: Span, parent_context: Optional[Context] = None) -> None:
        """Forward on_start to all processors."""
        for processor in self.__processors.values():
            processor.on_start(span, parent_context)

    @override
    def on_end(self, span: ReadableSpan) -> None:
        """Forward on_end to all processors."""
        for processor in self.__processors.values():
            processor.on_end(span)

    @override
    def shutdown(self) -> None:
        """Shutdown all processors."""
        for processor in self.__processors.values():
            processor.shutdown()  # type: ignore[no-untyped-call]

    @override
    def force_flush(self, timeout_millis: int = 30000) -> bool:
        """Force flush all processors."""
        return all(processor.force_flush(timeout_millis) for processor in self.__processors.values())


_global_provider: Optional[TracerProvider] = None
_global_tracer: Optional[trace.Tracer] = None
_composite_processor: Optional[CompositeProcessor] = None
_provider_lock = threading.Lock()


def _init_provider(config: WrapConfig) -> Optional[str]:
    """
    Initialize OpenTelemetry provider for LLM SDK wrappers.
    Returns the project_id if provided.
    Thread-safe initialization using double-checked locking pattern.
    """
    global _global_provider, _global_tracer, _composite_processor  # noqa: PLW0603

    api_key = config.get("api_key") or os.getenv("SCORECARD_API_KEY")
    if not api_key:
        raise ScorecardError(
            "Scorecard API key is required. Set SCORECARD_API_KEY environment variable or pass api_key in config."
        )

    endpoint = config.get("endpoint") or "https://tracing.scorecard.io/otel/v1/traces"
    service_name = config.get("service_name") or "llm-app"
    project_id = config.get("project_id") or os.getenv("SCORECARD_PROJECT_ID")
    max_export_batch_size = config.get("max_export_batch_size") or 1

    # Double-checked locking pattern for thread-safe initialization
    if _global_provider is None:
        with _provider_lock:
            # Check again inside the lock in case another thread just initialized it
            if _global_provider is None:
                _composite_processor = CompositeProcessor()

                resource = Resource(attributes={"service.name": service_name})

                _global_provider = TracerProvider(resource=resource)
                _global_provider.add_span_processor(_composite_processor)

                trace.set_tracer_provider(_global_provider)
                _global_tracer = trace.get_tracer("scorecard-llm")

    # Add an exporter for this specific apiKey+endpoint (if not already added)
    # This also needs to be thread-safe
    with _provider_lock:
        if _composite_processor is not None:
            _composite_processor.add_processor(api_key, endpoint, max_export_batch_size)

    return project_id


def _detect_provider(client: Any) -> str:
    """Detect which LLM provider the client is for."""
    # Check for OpenAI SDK structure
    if hasattr(client, "chat") and hasattr(client.chat, "completions"):
        return "openai"

    # Check for Anthropic SDK structure
    if hasattr(client, "messages"):
        return "anthropic"

    raise ScorecardError("Unable to detect LLM provider. Client must be an OpenAI or Anthropic SDK instance.")


def _handle_openai_response(span: trace.Span, result: Any, params: dict[str, Any]) -> None:
    """Handle OpenAI-specific response parsing."""
    span.set_attributes(
        {
            "gen_ai.response.id": getattr(result, "id", "unknown"),
            "gen_ai.response.model": getattr(result, "model", params.get("model", "unknown")),
            "gen_ai.response.finish_reason": (result.choices[0].finish_reason or "unknown")
            if result.choices
            else "unknown",
            "gen_ai.usage.prompt_tokens": getattr(result.usage, "prompt_tokens", 0) if result.usage else 0,
            "gen_ai.usage.completion_tokens": (getattr(result.usage, "completion_tokens", 0) if result.usage else 0),
            "gen_ai.usage.total_tokens": getattr(result.usage, "total_tokens", 0) if result.usage else 0,
        }
    )

    if result.choices and result.choices[0].message:
        span.set_attribute(
            "gen_ai.completion.choices",
            json.dumps([{"message": {"role": "assistant", "content": result.choices[0].message.content}}]),
        )


def _handle_anthropic_response(span: trace.Span, result: Any, params: dict[str, Any]) -> None:
    """Handle Anthropic-specific response parsing."""
    input_tokens = getattr(result.usage, "input_tokens", 0) if result.usage else 0
    output_tokens = getattr(result.usage, "output_tokens", 0) if result.usage else 0

    span.set_attributes(
        {
            "gen_ai.response.id": getattr(result, "id", "unknown"),
            "gen_ai.response.model": getattr(result, "model", params.get("model", "unknown")),
            "gen_ai.response.finish_reason": getattr(result, "stop_reason", None) or "unknown",
            "gen_ai.usage.prompt_tokens": input_tokens,
            "gen_ai.usage.completion_tokens": output_tokens,
            "gen_ai.usage.total_tokens": input_tokens + output_tokens,
        }
    )

    if result.content:
        # Collect text from all text blocks (Anthropic can return multiple content blocks)
        completion_texts = [c.text for c in result.content if hasattr(c, "text")]
        if completion_texts:
            span.set_attribute(
                "gen_ai.completion.choices",
                json.dumps([{"message": {"role": "assistant", "content": "\n".join(completion_texts)}}]),
            )


class _StreamWrapper:
    """Wrapper for synchronous streams that collects metadata and ends span when consumed."""

    def __init__(self, stream: Any, span: trace.Span, provider: str, params: dict[str, Any]):
        self.__stream = stream
        self.__span = span
        self.__provider = provider
        self.__params = params
        self.__content_parts: list[str] = []
        self.__finish_reason: Optional[str] = None
        self.__usage_data: dict[str, int] = {}
        self.__response_id: Optional[str] = None
        self.__model: Optional[str] = None

    def __iter__(self) -> Any:
        """Make the wrapper iterable."""
        return self

    def __next__(self) -> Any:
        """Get the next chunk from the stream and accumulate metadata."""
        try:
            chunk = next(self.__stream)
            self.__process_chunk(chunk)
            return chunk
        except StopIteration:
            # Stream is exhausted, finalize span
            self.__finalize_span()
            raise

    def __enter__(self) -> Any:
        """Support context manager protocol."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Ensure span is ended when context exits."""
        if not self.__span.is_recording():
            return
        self.__finalize_span()

    def __del__(self) -> None:
        """Finalize span upon garbage collection as a fallback."""
        self.__finalize_span()

    def __process_chunk(self, chunk: Any) -> None:
        """Process a chunk and extract metadata."""
        # OpenAI streaming format
        if self.__provider == "openai" and hasattr(chunk, "choices"):
            if not self.__response_id and hasattr(chunk, "id"):
                self.__response_id = chunk.id
            if not self.__model and hasattr(chunk, "model"):
                self.__model = chunk.model

            if chunk.choices:
                choice = chunk.choices[0]
                if hasattr(choice, "delta") and hasattr(choice.delta, "content") and choice.delta.content:
                    self.__content_parts.append(choice.delta.content)
                if hasattr(choice, "finish_reason") and choice.finish_reason:
                    self.__finish_reason = choice.finish_reason

            # OpenAI includes usage in the last chunk with stream_options
            if hasattr(chunk, "usage") and chunk.usage:
                self.__usage_data = {
                    "prompt_tokens": getattr(chunk.usage, "prompt_tokens", 0),
                    "completion_tokens": getattr(chunk.usage, "completion_tokens", 0),
                    "total_tokens": getattr(chunk.usage, "total_tokens", 0),
                }

        # Anthropic streaming format
        elif self.__provider == "anthropic":
            if hasattr(chunk, "type"):
                if chunk.type == "message_start" and hasattr(chunk, "message"):
                    self.__response_id = getattr(chunk.message, "id", None)
                    self.__model = getattr(chunk.message, "model", None)
                elif chunk.type == "content_block_delta" and hasattr(chunk, "delta"):
                    if hasattr(chunk.delta, "text"):
                        self.__content_parts.append(chunk.delta.text)
                elif chunk.type == "message_delta" and hasattr(chunk, "delta"):
                    if hasattr(chunk.delta, "stop_reason"):
                        self.__finish_reason = chunk.delta.stop_reason
                    if hasattr(chunk, "usage"):
                        self.__usage_data["output_tokens"] = getattr(chunk.usage, "output_tokens", 0)
                elif chunk.type == "message_start" and hasattr(chunk, "message") and hasattr(chunk.message, "usage"):
                    self.__usage_data["input_tokens"] = getattr(chunk.message.usage, "input_tokens", 0)

    def __finalize_span(self) -> None:
        """Set final attributes on span and end it."""
        if not self.__span.is_recording():
            return

        # Set response attributes
        self.__span.set_attributes(
            {
                "gen_ai.response.id": self.__response_id or "unknown",
                "gen_ai.response.model": self.__model or self.__params.get("model", "unknown"),
                "gen_ai.response.finish_reason": self.__finish_reason or "unknown",
            }
        )

        # Set usage data
        if self.__usage_data:
            if self.__provider == "openai":
                self.__span.set_attributes(
                    {
                        "gen_ai.usage.prompt_tokens": self.__usage_data.get("prompt_tokens", 0),
                        "gen_ai.usage.completion_tokens": self.__usage_data.get("completion_tokens", 0),
                        "gen_ai.usage.total_tokens": self.__usage_data.get("total_tokens", 0),
                    }
                )
            elif self.__provider == "anthropic":
                input_tokens = self.__usage_data.get("input_tokens", 0)
                output_tokens = self.__usage_data.get("output_tokens", 0)
                self.__span.set_attributes(
                    {
                        "gen_ai.usage.prompt_tokens": input_tokens,
                        "gen_ai.usage.completion_tokens": output_tokens,
                        "gen_ai.usage.total_tokens": input_tokens + output_tokens,
                    }
                )

        # Set completion content if any was collected
        if self.__content_parts:
            content = "".join(self.__content_parts)
            self.__span.set_attribute(
                "gen_ai.completion.choices",
                json.dumps([{"message": {"role": "assistant", "content": content}}]),
            )

        self.__span.end()


class _AsyncStreamWrapper:
    """Wrapper for asynchronous streams that collects metadata and ends span when consumed."""

    def __init__(self, stream: Any, span: trace.Span, provider: str, params: dict[str, Any]):
        self.__stream = stream
        self.__span = span
        self.__provider = provider
        self.__params = params
        self.__content_parts: list[str] = []
        self.__finish_reason: Optional[str] = None
        self.__usage_data: dict[str, int] = {}
        self.__response_id: Optional[str] = None
        self.__model: Optional[str] = None

    def __aiter__(self) -> Any:
        """Make the wrapper async iterable."""
        return self

    async def __anext__(self) -> Any:
        """Get the next chunk from the async stream and accumulate metadata."""
        try:
            chunk = await self.__stream.__anext__()
            self.__process_chunk(chunk)
            return chunk
        except StopAsyncIteration:
            # Stream is exhausted, finalize span
            self.__finalize_span()
            raise

    async def __aenter__(self) -> Any:
        """Support async context manager protocol."""
        return self

    async def __aexit__(self, *args: Any) -> None:
        """Ensure span is ended when context exits."""
        if not self.__span.is_recording():
            return
        self.__finalize_span()

    def __del__(self) -> None:
        """Finalize span upon garbage collection as a fallback."""
        self.__finalize_span()

    def __process_chunk(self, chunk: Any) -> None:
        """Process a chunk and extract metadata."""
        # OpenAI streaming format
        if self.__provider == "openai" and hasattr(chunk, "choices"):
            if not self.__response_id and hasattr(chunk, "id"):
                self.__response_id = chunk.id
            if not self.__model and hasattr(chunk, "model"):
                self.__model = chunk.model

            if chunk.choices:
                choice = chunk.choices[0]
                if hasattr(choice, "delta") and hasattr(choice.delta, "content") and choice.delta.content:
                    self.__content_parts.append(choice.delta.content)
                if hasattr(choice, "finish_reason") and choice.finish_reason:
                    self.__finish_reason = choice.finish_reason

            # OpenAI includes usage in the last chunk with stream_options
            if hasattr(chunk, "usage") and chunk.usage:
                self.__usage_data = {
                    "prompt_tokens": getattr(chunk.usage, "prompt_tokens", 0),
                    "completion_tokens": getattr(chunk.usage, "completion_tokens", 0),
                    "total_tokens": getattr(chunk.usage, "total_tokens", 0),
                }

        # Anthropic streaming format
        elif self.__provider == "anthropic":
            if hasattr(chunk, "type"):
                if chunk.type == "message_start" and hasattr(chunk, "message"):
                    self.__response_id = getattr(chunk.message, "id", None)
                    self.__model = getattr(chunk.message, "model", None)
                elif chunk.type == "content_block_delta" and hasattr(chunk, "delta"):
                    if hasattr(chunk.delta, "text"):
                        self.__content_parts.append(chunk.delta.text)
                elif chunk.type == "message_delta" and hasattr(chunk, "delta"):
                    if hasattr(chunk.delta, "stop_reason"):
                        self.__finish_reason = chunk.delta.stop_reason
                    if hasattr(chunk, "usage"):
                        self.__usage_data["output_tokens"] = getattr(chunk.usage, "output_tokens", 0)
                elif chunk.type == "message_start" and hasattr(chunk, "message") and hasattr(chunk.message, "usage"):
                    self.__usage_data["input_tokens"] = getattr(chunk.message.usage, "input_tokens", 0)

    def __finalize_span(self) -> None:
        """Set final attributes on span and end it."""
        if not self.__span.is_recording():
            return

        # Set response attributes
        self.__span.set_attributes(
            {
                "gen_ai.response.id": self.__response_id or "unknown",
                "gen_ai.response.model": self.__model or self.__params.get("model", "unknown"),
                "gen_ai.response.finish_reason": self.__finish_reason or "unknown",
            }
        )

        # Set usage data
        if self.__usage_data:
            if self.__provider == "openai":
                self.__span.set_attributes(
                    {
                        "gen_ai.usage.prompt_tokens": self.__usage_data.get("prompt_tokens", 0),
                        "gen_ai.usage.completion_tokens": self.__usage_data.get("completion_tokens", 0),
                        "gen_ai.usage.total_tokens": self.__usage_data.get("total_tokens", 0),
                    }
                )
            elif self.__provider == "anthropic":
                input_tokens = self.__usage_data.get("input_tokens", 0)
                output_tokens = self.__usage_data.get("output_tokens", 0)
                self.__span.set_attributes(
                    {
                        "gen_ai.usage.prompt_tokens": input_tokens,
                        "gen_ai.usage.completion_tokens": output_tokens,
                        "gen_ai.usage.total_tokens": input_tokens + output_tokens,
                    }
                )

        # Set completion content if any was collected
        if self.__content_parts:
            content = "".join(self.__content_parts)
            self.__span.set_attribute(
                "gen_ai.completion.choices",
                json.dumps([{"message": {"role": "assistant", "content": content}}]),
            )

        self.__span.end()


class _LLMClientWrapper:
    """Wrapper class that adds tracing to LLM SDK clients."""

    def __init__(self, client: Any, config: WrapConfig, provider: str, project_id: Optional[str]):
        self._client = client
        self._config = config
        self._provider = provider
        self._project_id = project_id
        self._tracer = _global_tracer

    def __getattr__(self, name: str) -> Any:
        """Delegate attribute access to wrapped client."""
        attr = getattr(self._client, name)

        # If it's an object (like 'chat' or 'messages'), wrap it recursively
        if hasattr(attr, "__dict__") and not callable(attr):
            return _NestedWrapper(attr, self._tracer, self._provider, self._project_id)

        return attr


class _NestedWrapper:
    """Wrapper for nested objects like client.chat.completions."""

    def __init__(self, obj: Any, tracer: Optional[trace.Tracer], provider: str, project_id: Optional[str]):
        self._obj = obj
        self._tracer = tracer
        self._provider = provider
        self._project_id = project_id

    def __getattr__(self, name: str) -> Any:
        """Delegate attribute access to wrapped object."""
        attr = getattr(self._obj, name)

        # Wrap 'create' methods with tracing
        if name == "create" and callable(attr):
            return self._wrap_create(attr)

        # Recursively wrap nested objects
        if hasattr(attr, "__dict__") and not callable(attr):
            return _NestedWrapper(attr, self._tracer, self._provider, self._project_id)

        return attr

    def _wrap_create(self, original_method: Any) -> Any:
        """Wrap the 'create' method with tracing, supporting both sync and async."""

        def _populate_span_attributes(span: trace.Span, kwargs: dict[str, Any]) -> None:
            """Helper to set common span attributes."""
            # Set request attributes (common to both providers)
            span.set_attributes(
                {
                    "gen_ai.system": self._provider,
                    "gen_ai.request.model": kwargs.get("model", "unknown"),
                    "gen_ai.operation.name": "chat",
                }
            )

            # Store projectId as span attribute - our custom exporter will inject it
            # into ResourceAttributes before export (where the backend expects it)
            if self._project_id:
                span.set_attribute("scorecard.project_id", self._project_id)

            # Optional parameters
            if "temperature" in kwargs:
                span.set_attribute("gen_ai.request.temperature", kwargs["temperature"])
            if "max_tokens" in kwargs:
                span.set_attribute("gen_ai.request.max_tokens", kwargs["max_tokens"])
            if "top_p" in kwargs:
                span.set_attribute("gen_ai.request.top_p", kwargs["top_p"])

            # Set prompt messages
            if "messages" in kwargs:
                span.set_attribute("gen_ai.prompt.messages", json.dumps(kwargs["messages"]))

        # Check if the method is async
        if inspect.iscoroutinefunction(original_method):

            async def async_traced_create(*args: Any, **kwargs: Any) -> Any:
                if self._tracer is None:
                    raise ScorecardError("Failed to initialize tracer")

                # Check if streaming is enabled
                is_streaming = kwargs.get("stream", False)

                if is_streaming:
                    # For streaming, start span manually (not with context manager)
                    span = self._tracer.start_span(f"{self._provider}.request")
                    _populate_span_attributes(span, kwargs)

                    try:
                        stream = await original_method(*args, **kwargs)
                        # Wrap the stream so it can finalize the span when consumed
                        return _AsyncStreamWrapper(stream, span, self._provider, kwargs)
                    except Exception as e:
                        span.record_exception(e)
                        span.end()
                        raise
                else:
                    # Non-streaming: use context manager as before
                    with self._tracer.start_as_current_span(f"{self._provider}.request") as span:
                        _populate_span_attributes(span, kwargs)

                        try:
                            result = await original_method(*args, **kwargs)

                            # Set response attributes (provider-specific)
                            if self._provider == "openai":
                                _handle_openai_response(span, result, kwargs)
                            elif self._provider == "anthropic":
                                _handle_anthropic_response(span, result, kwargs)

                            return result
                        except Exception as e:
                            span.record_exception(e)
                            raise

            return async_traced_create

        # Sync wrapper
        def traced_create(*args: Any, **kwargs: Any) -> Any:
            if self._tracer is None:
                raise ScorecardError("Failed to initialize tracer")

            # Check if streaming is enabled
            is_streaming = kwargs.get("stream", False)

            if is_streaming:
                # For streaming, start span manually (not with context manager)
                span = self._tracer.start_span(f"{self._provider}.request")
                _populate_span_attributes(span, kwargs)

                try:
                    stream = original_method(*args, **kwargs)
                    # Wrap the stream so it can finalize the span when consumed
                    return _StreamWrapper(stream, span, self._provider, kwargs)
                except Exception as e:
                    span.record_exception(e)
                    span.end()
                    raise
            else:
                # Non-streaming: use context manager as before
                with self._tracer.start_as_current_span(f"{self._provider}.request") as span:
                    _populate_span_attributes(span, kwargs)

                    try:
                        result = original_method(*args, **kwargs)

                        # Set response attributes (provider-specific)
                        if self._provider == "openai":
                            _handle_openai_response(span, result, kwargs)
                        elif self._provider == "anthropic":
                            _handle_anthropic_response(span, result, kwargs)

                        return result
                    except Exception as e:
                        span.record_exception(e)
                        raise

        return traced_create


def wrap(client: _ClientT, config: Optional[WrapConfig] = None) -> _ClientT:  # type: ignore[return-value]
    """
    Wrap any LLM SDK (OpenAI or Anthropic) to automatically trace all API calls.

    Args:
        client: An instance of OpenAI or Anthropic SDK client
        config: Optional configuration for tracing

    Returns:
        The wrapped client with automatic tracing enabled

    Example:
        >>> from scorecard_ai import wrap
        >>> from openai import OpenAI
        >>> from anthropic import Anthropic
        >>>
        >>> # Works with OpenAI
        >>> openai = wrap(OpenAI(api_key="..."), {
        ...     "api_key": os.getenv("SCORECARD_API_KEY"),
        ...     "project_id": "123"
        >>> })
        >>>
        >>> # Works with Anthropic
        >>> claude = wrap(Anthropic(api_key="..."), {
        ...     "api_key": os.getenv("SCORECARD_API_KEY"),
        ...     "project_id": "123"
        >>> })
        >>>
        >>> # Use normally - traces are automatically sent to Scorecard
        >>> response = openai.chat.completions.create(...)
        >>> response2 = claude.messages.create(...)
    """
    if config is None:
        config = {}

    project_id = _init_provider(config)

    if _global_tracer is None:
        raise ScorecardError("Failed to initialize tracer")

    provider = _detect_provider(client)

    return _LLMClientWrapper(client, config, provider, project_id)  # type: ignore[return-value]  # pyright: ignore[reportReturnType]


# Backwards compatibility aliases
wrap_openai = wrap
wrap_anthropic = wrap


__all__ = ["wrap", "wrap_openai", "wrap_anthropic", "WrapConfig"]
