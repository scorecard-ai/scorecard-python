from __future__ import annotations

import json
from typing import Any, Callable, Iterator
from unittest.mock import Mock

import httpx
import pytest

import scorecard_ai

pytest.importorskip("opentelemetry.sdk")

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

from scorecard_ai.lib import _wrap_llms_otel


@pytest.fixture
def spans(monkeypatch: pytest.MonkeyPatch) -> Iterator[InMemorySpanExporter]:
    exporter = InMemorySpanExporter()
    provider = TracerProvider()
    provider.add_span_processor(SimpleSpanProcessor(exporter))
    monkeypatch.setattr(_wrap_llms_otel, "_init_provider", Mock(return_value="project-id"))
    monkeypatch.setattr(_wrap_llms_otel, "_global_tracer", provider.get_tracer("test-wrap"))
    yield exporter
    provider.shutdown()


def make_client(provider: str, asynchronous: bool, handler: Callable[[httpx.Request], httpx.Response]) -> Any:
    sdk = pytest.importorskip(provider)
    sdk_base = pytest.importorskip(f"{provider}._base_client")
    # Use the SDK's HTTP backend (httpx or httpx2) without adding a dependency.
    http = getattr(sdk_base, "httpx2", httpx)
    name = "OpenAI" if provider == "openai" else "Anthropic"

    def mock_handler(request: Any) -> Any:
        response = handler(request)
        return http.Response(response.status_code, headers=response.headers, content=response.content)

    transport = http.MockTransport(mock_handler)
    http_client = http.AsyncClient(transport=transport) if asynchronous else http.Client(transport=transport)
    return getattr(sdk, f"Async{name}" if asynchronous else name)(
        api_key="test-key", max_retries=0, http_client=http_client
    )


def resolve(obj: Any, path: str) -> Any:
    for name in path.split("."):
        obj = getattr(obj, name)
    return obj


PASSTHROUGH_PATHS = [
    ("openai", "responses"),
    ("openai", "embeddings"),
    ("openai", "images"),
    ("openai", "files"),
    ("openai", "beta.responses"),
    ("openai", "beta.chat.completions.messages"),
    ("openai", "beta.chat.completions.with_raw_response"),
    ("openai", "beta.chat.completions.with_streaming_response"),
    ("openai", "models"),
    ("openai", "chat.completions.messages"),
    ("openai", "chat.completions.with_raw_response"),
    ("openai", "chat.completions.with_streaming_response"),
    ("anthropic", "beta.files"),
    ("anthropic", "beta.models"),
    ("anthropic", "beta.messages.batches"),
    ("anthropic", "beta.messages.with_raw_response"),
    ("anthropic", "beta.messages.with_streaming_response"),
    ("anthropic", "files"),
    ("anthropic", "models"),
    ("anthropic", "messages.batches"),
    ("anthropic", "messages.with_raw_response"),
    ("anthropic", "messages.with_streaming_response"),
]


@pytest.mark.parametrize("provider,path", PASSTHROUGH_PATHS)
@pytest.mark.parametrize("asynchronous", [False, True], ids=["sync", "async"])
async def test_other_resources_pass_through(
    provider: str, path: str, asynchronous: bool, spans: InMemorySpanExporter
) -> None:
    client = make_client(provider, asynchronous, Mock(side_effect=AssertionError("Unexpected HTTP request")))
    try:
        wrapped = scorecard_ai.wrap(client)
        assert resolve(wrapped, path) is resolve(client, path)
        assert wrapped.close == client.close
        assert wrapped.api_key == client.api_key
        assert spans.get_finished_spans() == ()
    finally:
        if asynchronous:
            await client.close()
        else:
            client.close()


@pytest.mark.parametrize("resource,streaming", [("responses", False), ("embeddings", False), ("responses", True)])
@pytest.mark.parametrize("asynchronous", [False, True], ids=["sync", "async"])
async def test_non_chat_create_passes_through(
    resource: str, streaming: bool, asynchronous: bool, spans: InMemorySpanExporter
) -> None:
    body: dict[str, Any]
    if resource == "responses":
        body = {"id": "resp_test", "object": "response", "model": "test-model", "output": []}
    else:
        body = {
            "object": "list",
            "data": [{"object": "embedding", "index": 0, "embedding": [0.1, 0.2]}],
            "model": "test-model",
            "usage": {"prompt_tokens": 1, "total_tokens": 1},
        }

    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if streaming:
            event = {"type": "response.completed", "response": body}
            return httpx.Response(
                200,
                text=f"event: response.completed\ndata: {json.dumps(event)}\n\n",
                headers={"content-type": "text/event-stream"},
            )
        return httpx.Response(200, json=body)

    client = make_client("openai", asynchronous, handler)
    try:
        wrapped = scorecard_ai.wrap(client)
        params: dict[str, Any] = {"model": "test-model", "input": "hello"}
        if streaming:
            params["stream"] = True
        expected = getattr(client, resource).create(**params)
        result = getattr(wrapped, resource).create(**params)
        if asynchronous:
            expected = await expected
            result = await result
        if streaming:
            if asynchronous:
                async with expected, result:
                    expected = [event async for event in expected]
                    result = [event async for event in result]
            else:
                with expected, result:
                    expected = list(expected)
                    result = list(result)
            assert result
        assert result == expected
        assert requests[0].url == requests[1].url
        assert requests[0].content == requests[1].content
        assert spans.get_finished_spans() == ()
    finally:
        if asynchronous:
            await client.close()
        else:
            client.close()


def response_body(provider: str) -> dict[str, Any]:
    if provider == "openai":
        return {
            "id": "chatcmpl_test",
            "object": "chat.completion",
            "created": 0,
            "model": "test-model",
            "choices": [{"index": 0, "message": {"role": "assistant", "content": "hello"}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 2, "completion_tokens": 3, "total_tokens": 5},
        }
    return {
        "id": "msg_test",
        "type": "message",
        "role": "assistant",
        "model": "test-model",
        "content": [{"type": "text", "text": "hello"}],
        "stop_reason": "end_turn",
        "stop_sequence": None,
        "usage": {"input_tokens": 2, "output_tokens": 3},
    }


def stream_body(provider: str) -> str:
    if provider == "openai":
        chunk = {
            "id": "chatcmpl_test",
            "object": "chat.completion.chunk",
            "created": 0,
            "model": "test-model",
            "choices": [{"index": 0, "delta": {"content": "hello"}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 2, "completion_tokens": 3, "total_tokens": 5},
        }
        return f"data: {json.dumps(chunk)}\n\ndata: [DONE]\n\n"
    events = [
        {"type": "message_start", "message": response_body(provider)},
        {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "hello"}},
        {"type": "message_delta", "delta": {"stop_reason": "end_turn"}, "usage": {"output_tokens": 3}},
        {"type": "message_stop"},
    ]
    return "".join(f"event: {event['type']}\ndata: {json.dumps(event)}\n\n" for event in events)


SUPPORTED_RESOURCES = [
    ("openai", "chat.completions"),
    ("openai", "beta.chat.completions"),
    ("anthropic", "messages"),
    ("anthropic", "beta.messages"),
]


@pytest.mark.parametrize("provider,path", SUPPORTED_RESOURCES)
@pytest.mark.parametrize("asynchronous", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize("streaming", [False, True], ids=["response", "stream"])
async def test_supported_create_keeps_tracing(
    provider: str, path: str, asynchronous: bool, streaming: bool, spans: InMemorySpanExporter
) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        expected_path = "/v1/chat/completions" if provider == "openai" else "/v1/messages"
        assert request.url.path == expected_path
        if path == "beta.messages":
            assert request.url.params["beta"] == "true"
        if streaming:
            return httpx.Response(200, text=stream_body(provider), headers={"content-type": "text/event-stream"})
        return httpx.Response(200, json=response_body(provider))

    client = make_client(provider, asynchronous, handler)
    try:
        wrapped = scorecard_ai.wrap(client)
        params = {"model": "test-model", "messages": [{"role": "user", "content": "hi"}], "max_tokens": 10}
        result = resolve(wrapped, path + ".create")(**params, stream=streaming)
        if asynchronous:
            result = await result
        if streaming:
            assert spans.get_finished_spans() == ()
            if asynchronous:
                async with result:
                    chunks = [chunk async for chunk in result]
            else:
                with result:
                    chunks = list(result)
            assert chunks
        else:
            assert result.id == response_body(provider)["id"]

        finished = spans.get_finished_spans()
        assert len(finished) == 1
        assert finished[0].name == f"{provider}.request"
        attributes = finished[0].attributes
        assert attributes is not None
        assert attributes["gen_ai.system"] == provider
        assert attributes["scorecard.project_id"] == "project-id"
        assert attributes["gen_ai.request.model"] == "test-model"
        assert attributes["gen_ai.response.id"] == response_body(provider)["id"]
        assert attributes["gen_ai.completion.choices"] == json.dumps(
            [{"message": {"role": "assistant", "content": "hello"}}]
        )
        assert attributes["gen_ai.usage.completion_tokens"] == 3
        if not streaming or provider == "openai":
            assert attributes["gen_ai.usage.total_tokens"] == 5
    finally:
        if asynchronous:
            await client.close()
        else:
            client.close()


@pytest.mark.parametrize("provider,path", SUPPORTED_RESOURCES)
@pytest.mark.parametrize("response_wrapper", ["with_raw_response", "with_streaming_response"])
@pytest.mark.parametrize("asynchronous", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize("streaming", [False, True], ids=["response", "stream"])
async def test_response_wrappers_pass_through(
    provider: str,
    path: str,
    response_wrapper: str,
    asynchronous: bool,
    streaming: bool,
    spans: InMemorySpanExporter,
) -> None:
    async def check_parsed(parsed: Any) -> None:
        if streaming:
            if asynchronous:
                async with parsed:
                    chunks = [chunk async for chunk in parsed]
            else:
                with parsed:
                    chunks = list(parsed)
            assert chunks
        else:
            assert parsed.id == response_body(provider)["id"]

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "POST"
        if streaming:
            return httpx.Response(200, text=stream_body(provider), headers={"content-type": "text/event-stream"})
        return httpx.Response(200, json=response_body(provider))

    client = make_client(provider, asynchronous, handler)
    try:
        wrapped = scorecard_ai.wrap(client)
        resource_path = path + "." + response_wrapper
        assert resolve(wrapped, resource_path) is resolve(client, resource_path)
        result = resolve(wrapped, resource_path + ".create")(
            model="test-model", messages=[{"role": "user", "content": "hi"}], max_tokens=10, stream=streaming
        )
        if response_wrapper == "with_streaming_response":
            if asynchronous:
                async with result as response:
                    parsed = await response.parse()
                    await check_parsed(parsed)
            else:
                with result as response:
                    parsed = response.parse()
                    await check_parsed(parsed)
        else:
            if asynchronous:
                result = await result
            parsed = result.parse()
            # OpenAI's legacy response parser is synchronous for async clients too.
            if asynchronous and provider == "anthropic":
                parsed = await parsed
            await check_parsed(parsed)
        assert spans.get_finished_spans() == ()
    finally:
        if asynchronous:
            await client.close()
        else:
            client.close()
