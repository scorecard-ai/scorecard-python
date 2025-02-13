# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecard import Scorecard, AsyncScorecard
from tests.utils import assert_matches_type
from scorecard.types import Trace, TraceListResponse, TraceRetrieveSpanResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTraces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Scorecard) -> None:
        trace = client.traces.retrieve(
            "8e45b6060adab3fb460c3a0ca65f5046",
        )
        assert_matches_type(Trace, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Scorecard) -> None:
        response = client.traces.with_raw_response.retrieve(
            "8e45b6060adab3fb460c3a0ca65f5046",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(Trace, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Scorecard) -> None:
        with client.traces.with_streaming_response.retrieve(
            "8e45b6060adab3fb460c3a0ca65f5046",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(Trace, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            client.traces.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        trace = client.traces.list()
        assert_matches_type(TraceListResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.traces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(TraceListResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.traces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(TraceListResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_span(self, client: Scorecard) -> None:
        trace = client.traces.retrieve_span(
            span_id="41adbaf1091c6609",
            trace_id="8e45b6060adab3fb460c3a0ca65f5046",
        )
        assert_matches_type(TraceRetrieveSpanResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_span(self, client: Scorecard) -> None:
        response = client.traces.with_raw_response.retrieve_span(
            span_id="41adbaf1091c6609",
            trace_id="8e45b6060adab3fb460c3a0ca65f5046",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(TraceRetrieveSpanResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_span(self, client: Scorecard) -> None:
        with client.traces.with_streaming_response.retrieve_span(
            span_id="41adbaf1091c6609",
            trace_id="8e45b6060adab3fb460c3a0ca65f5046",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(TraceRetrieveSpanResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_span(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            client.traces.with_raw_response.retrieve_span(
                span_id="41adbaf1091c6609",
                trace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            client.traces.with_raw_response.retrieve_span(
                span_id="",
                trace_id="8e45b6060adab3fb460c3a0ca65f5046",
            )


class TestAsyncTraces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncScorecard) -> None:
        trace = await async_client.traces.retrieve(
            "8e45b6060adab3fb460c3a0ca65f5046",
        )
        assert_matches_type(Trace, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncScorecard) -> None:
        response = await async_client.traces.with_raw_response.retrieve(
            "8e45b6060adab3fb460c3a0ca65f5046",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(Trace, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncScorecard) -> None:
        async with async_client.traces.with_streaming_response.retrieve(
            "8e45b6060adab3fb460c3a0ca65f5046",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(Trace, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            await async_client.traces.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        trace = await async_client.traces.list()
        assert_matches_type(TraceListResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.traces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(TraceListResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.traces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(TraceListResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_span(self, async_client: AsyncScorecard) -> None:
        trace = await async_client.traces.retrieve_span(
            span_id="41adbaf1091c6609",
            trace_id="8e45b6060adab3fb460c3a0ca65f5046",
        )
        assert_matches_type(TraceRetrieveSpanResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_span(self, async_client: AsyncScorecard) -> None:
        response = await async_client.traces.with_raw_response.retrieve_span(
            span_id="41adbaf1091c6609",
            trace_id="8e45b6060adab3fb460c3a0ca65f5046",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(TraceRetrieveSpanResponse, trace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_span(self, async_client: AsyncScorecard) -> None:
        async with async_client.traces.with_streaming_response.retrieve_span(
            span_id="41adbaf1091c6609",
            trace_id="8e45b6060adab3fb460c3a0ca65f5046",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(TraceRetrieveSpanResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_span(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            await async_client.traces.with_raw_response.retrieve_span(
                span_id="41adbaf1091c6609",
                trace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `span_id` but received ''"):
            await async_client.traces.with_raw_response.retrieve_span(
                span_id="",
                trace_id="8e45b6060adab3fb460c3a0ca65f5046",
            )
