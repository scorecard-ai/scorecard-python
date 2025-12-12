"""Wrapper for OpenAI and Anthropic SDKs to automatically trace LLM calls."""

from __future__ import annotations

import json
import os
from typing import Any, Optional, TYPE_CHECKING

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

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


_global_provider: Optional[TracerProvider] = None
_global_tracer: Optional[trace.Tracer] = None


def _init_provider(config: WrapConfig) -> None:
    """Initialize OpenTelemetry provider for LLM SDK wrappers."""
    global _global_provider, _global_tracer

    if _global_provider is not None:
        return

    api_key = config.get("api_key") or os.getenv("SCORECARD_API_KEY")
    if not api_key:
        raise ScorecardError(
            "Scorecard API key is required. Set SCORECARD_API_KEY environment variable or pass api_key in config."
        )

    endpoint = config.get("endpoint", "https://tracing.scorecard.io/otel/v1/traces")
    service_name = config.get("service_name", "llm-app")
    project_id = config.get("project_id") or os.getenv("SCORECARD_PROJECT_ID")

    exporter = OTLPSpanExporter(
        endpoint=endpoint,
        headers={"Authorization": f"Bearer {api_key}"},
    )

    resource_attrs = {"service.name": service_name}
    if project_id:
        resource_attrs["scorecard.project_id"] = project_id

    resource = Resource.create(resource_attrs)

    _global_provider = TracerProvider(resource=resource)
    _global_provider.add_span_processor(
        BatchSpanProcessor(exporter, max_export_batch_size=1)  # Export immediately
    )

    trace.set_tracer_provider(_global_provider)
    _global_tracer = trace.get_tracer("scorecard-llm")


def _detect_provider(client: Any) -> str:
    """Detect which LLM provider the client is for."""
    # Check for OpenAI SDK structure
    if hasattr(client, "chat") and hasattr(client.chat, "completions"):
        return "openai"

    # Check for Anthropic SDK structure
    if hasattr(client, "messages"):
        return "anthropic"

    raise ScorecardError(
        "Unable to detect LLM provider. Client must be an OpenAI or Anthropic SDK instance."
    )


def _handle_openai_response(span: trace.Span, result: Any, params: dict[str, Any]) -> None:
    """Handle OpenAI-specific response parsing."""
    span.set_attributes(
        {
            "gen_ai.response.id": getattr(result, "id", "unknown"),
            "gen_ai.response.model": getattr(result, "model", params.get("model", "unknown")),
            "gen_ai.response.finish_reason": (
                result.choices[0].finish_reason if result.choices else "unknown"
            ),
            "gen_ai.usage.prompt_tokens": getattr(result.usage, "prompt_tokens", 0) if result.usage else 0,
            "gen_ai.usage.completion_tokens": (
                getattr(result.usage, "completion_tokens", 0) if result.usage else 0
            ),
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
            "gen_ai.response.finish_reason": getattr(result, "stop_reason", "unknown"),
            "gen_ai.usage.prompt_tokens": input_tokens,
            "gen_ai.usage.completion_tokens": output_tokens,
            "gen_ai.usage.total_tokens": input_tokens + output_tokens,
        }
    )

    if result.content and len(result.content) > 0:
        first_content = result.content[0]
        if hasattr(first_content, "text"):
            span.set_attribute(
                "gen_ai.completion.choices",
                json.dumps([{"message": {"role": "assistant", "content": first_content.text}}]),
            )


class _LLMClientWrapper:
    """Wrapper class that adds tracing to LLM SDK clients."""

    def __init__(self, client: Any, config: WrapConfig, provider: str):
        self._client = client
        self._config = config
        self._provider = provider
        self._tracer = _global_tracer

    def __getattr__(self, name: str) -> Any:
        """Delegate attribute access to wrapped client."""
        attr = getattr(self._client, name)

        # If it's an object (like 'chat' or 'messages'), wrap it recursively
        if hasattr(attr, "__dict__") and not callable(attr):
            return _NestedWrapper(attr, self._tracer, self._provider)

        return attr


class _NestedWrapper:
    """Wrapper for nested objects like client.chat.completions."""

    def __init__(self, obj: Any, tracer: Optional[trace.Tracer], provider: str):
        self._obj = obj
        self._tracer = tracer
        self._provider = provider

    def __getattr__(self, name: str) -> Any:
        """Delegate attribute access to wrapped object."""
        attr = getattr(self._obj, name)

        # Wrap 'create' methods with tracing
        if name == "create" and callable(attr):
            return self._wrap_create(attr)

        # Recursively wrap nested objects
        if hasattr(attr, "__dict__") and not callable(attr):
            return _NestedWrapper(attr, self._tracer, self._provider)

        return attr

    def _wrap_create(self, original_method: Any) -> Any:
        """Wrap the 'create' method with tracing."""

        def traced_create(*args: Any, **kwargs: Any) -> Any:
            if self._tracer is None:
                raise ScorecardError("Failed to initialize tracer")

            # Start span in current active context (enables nesting)
            with self._tracer.start_as_current_span(f"{self._provider}.request") as span:
                # Set request attributes (common to both providers)
                span.set_attributes(
                    {
                        "gen_ai.system": self._provider,
                        "gen_ai.request.model": kwargs.get("model", "unknown"),
                        "gen_ai.operation.name": "chat",
                    }
                )

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


def wrap(client: Any, config: Optional[WrapConfig] = None) -> Any:
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

    _init_provider(config)

    if _global_tracer is None:
        raise ScorecardError("Failed to initialize tracer")

    provider = _detect_provider(client)

    return _LLMClientWrapper(client, config, provider)


# Backwards compatibility aliases
wrap_openai = wrap
wrap_anthropic = wrap


__all__ = ["wrap", "wrap_openai", "wrap_anthropic", "WrapConfig"]
