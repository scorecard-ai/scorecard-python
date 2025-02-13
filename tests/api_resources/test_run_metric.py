# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecard import Scorecard, AsyncScorecard
from tests.utils import assert_matches_type
from scorecard.types import RunMetricRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRunMetric:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Scorecard) -> None:
        run_metric = client.run_metric.retrieve(
            310,
        )
        assert_matches_type(RunMetricRetrieveResponse, run_metric, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Scorecard) -> None:
        response = client.run_metric.with_raw_response.retrieve(
            310,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run_metric = response.parse()
        assert_matches_type(RunMetricRetrieveResponse, run_metric, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Scorecard) -> None:
        with client.run_metric.with_streaming_response.retrieve(
            310,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run_metric = response.parse()
            assert_matches_type(RunMetricRetrieveResponse, run_metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRunMetric:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncScorecard) -> None:
        run_metric = await async_client.run_metric.retrieve(
            310,
        )
        assert_matches_type(RunMetricRetrieveResponse, run_metric, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncScorecard) -> None:
        response = await async_client.run_metric.with_raw_response.retrieve(
            310,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run_metric = await response.parse()
        assert_matches_type(RunMetricRetrieveResponse, run_metric, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncScorecard) -> None:
        async with async_client.run_metric.with_streaming_response.retrieve(
            310,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run_metric = await response.parse()
            assert_matches_type(RunMetricRetrieveResponse, run_metric, path=["response"])

        assert cast(Any, response.is_closed) is True
