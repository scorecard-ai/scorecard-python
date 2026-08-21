# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types import (
    MetricGroup,
    MetricGroupDeleteResponse,
)
from scorecard_ai.pagination import SyncPaginatedResponse, AsyncPaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetricGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        metric_group = client.metric_groups.create(
            project_id="314",
            metric_ids=["321", "322"],
            name="Accuracy Metrics",
        )
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Scorecard) -> None:
        metric_group = client.metric_groups.create(
            project_id="314",
            metric_ids=["321", "322"],
            name="Accuracy Metrics",
            description="Metrics that evaluate factual accuracy",
        )
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.metric_groups.with_raw_response.create(
            project_id="314",
            metric_ids=["321", "322"],
            name="Accuracy Metrics",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_group = response.parse()
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.metric_groups.with_streaming_response.create(
            project_id="314",
            metric_ids=["321", "322"],
            name="Accuracy Metrics",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_group = response.parse()
            assert_matches_type(MetricGroup, metric_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.metric_groups.with_raw_response.create(
                project_id="",
                metric_ids=["321", "322"],
                name="Accuracy Metrics",
            )

    @parametrize
    def test_method_update(self, client: Scorecard) -> None:
        metric_group = client.metric_groups.update(
            metric_group_id="612",
        )
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Scorecard) -> None:
        metric_group = client.metric_groups.update(
            metric_group_id="612",
            description="description",
            metric_ids=["321"],
            name="Quality Metrics",
        )
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Scorecard) -> None:
        response = client.metric_groups.with_raw_response.update(
            metric_group_id="612",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_group = response.parse()
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Scorecard) -> None:
        with client.metric_groups.with_streaming_response.update(
            metric_group_id="612",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_group = response.parse()
            assert_matches_type(MetricGroup, metric_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_group_id` but received ''"):
            client.metric_groups.with_raw_response.update(
                metric_group_id="",
            )

    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        metric_group = client.metric_groups.list(
            project_id="314",
        )
        assert_matches_type(SyncPaginatedResponse[MetricGroup], metric_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Scorecard) -> None:
        metric_group = client.metric_groups.list(
            project_id="314",
            cursor="123",
            limit=20,
        )
        assert_matches_type(SyncPaginatedResponse[MetricGroup], metric_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.metric_groups.with_raw_response.list(
            project_id="314",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_group = response.parse()
        assert_matches_type(SyncPaginatedResponse[MetricGroup], metric_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.metric_groups.with_streaming_response.list(
            project_id="314",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_group = response.parse()
            assert_matches_type(SyncPaginatedResponse[MetricGroup], metric_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.metric_groups.with_raw_response.list(
                project_id="",
            )

    @parametrize
    def test_method_delete(self, client: Scorecard) -> None:
        metric_group = client.metric_groups.delete(
            "612",
        )
        assert_matches_type(MetricGroupDeleteResponse, metric_group, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Scorecard) -> None:
        response = client.metric_groups.with_raw_response.delete(
            "612",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_group = response.parse()
        assert_matches_type(MetricGroupDeleteResponse, metric_group, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Scorecard) -> None:
        with client.metric_groups.with_streaming_response.delete(
            "612",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_group = response.parse()
            assert_matches_type(MetricGroupDeleteResponse, metric_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_group_id` but received ''"):
            client.metric_groups.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Scorecard) -> None:
        metric_group = client.metric_groups.get(
            "612",
        )
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Scorecard) -> None:
        response = client.metric_groups.with_raw_response.get(
            "612",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_group = response.parse()
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Scorecard) -> None:
        with client.metric_groups.with_streaming_response.get(
            "612",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_group = response.parse()
            assert_matches_type(MetricGroup, metric_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_group_id` but received ''"):
            client.metric_groups.with_raw_response.get(
                "",
            )


class TestAsyncMetricGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        metric_group = await async_client.metric_groups.create(
            project_id="314",
            metric_ids=["321", "322"],
            name="Accuracy Metrics",
        )
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncScorecard) -> None:
        metric_group = await async_client.metric_groups.create(
            project_id="314",
            metric_ids=["321", "322"],
            name="Accuracy Metrics",
            description="Metrics that evaluate factual accuracy",
        )
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metric_groups.with_raw_response.create(
            project_id="314",
            metric_ids=["321", "322"],
            name="Accuracy Metrics",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_group = await response.parse()
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.metric_groups.with_streaming_response.create(
            project_id="314",
            metric_ids=["321", "322"],
            name="Accuracy Metrics",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_group = await response.parse()
            assert_matches_type(MetricGroup, metric_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.metric_groups.with_raw_response.create(
                project_id="",
                metric_ids=["321", "322"],
                name="Accuracy Metrics",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncScorecard) -> None:
        metric_group = await async_client.metric_groups.update(
            metric_group_id="612",
        )
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncScorecard) -> None:
        metric_group = await async_client.metric_groups.update(
            metric_group_id="612",
            description="description",
            metric_ids=["321"],
            name="Quality Metrics",
        )
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metric_groups.with_raw_response.update(
            metric_group_id="612",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_group = await response.parse()
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecard) -> None:
        async with async_client.metric_groups.with_streaming_response.update(
            metric_group_id="612",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_group = await response.parse()
            assert_matches_type(MetricGroup, metric_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_group_id` but received ''"):
            await async_client.metric_groups.with_raw_response.update(
                metric_group_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        metric_group = await async_client.metric_groups.list(
            project_id="314",
        )
        assert_matches_type(AsyncPaginatedResponse[MetricGroup], metric_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecard) -> None:
        metric_group = await async_client.metric_groups.list(
            project_id="314",
            cursor="123",
            limit=20,
        )
        assert_matches_type(AsyncPaginatedResponse[MetricGroup], metric_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metric_groups.with_raw_response.list(
            project_id="314",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_group = await response.parse()
        assert_matches_type(AsyncPaginatedResponse[MetricGroup], metric_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.metric_groups.with_streaming_response.list(
            project_id="314",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_group = await response.parse()
            assert_matches_type(AsyncPaginatedResponse[MetricGroup], metric_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.metric_groups.with_raw_response.list(
                project_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncScorecard) -> None:
        metric_group = await async_client.metric_groups.delete(
            "612",
        )
        assert_matches_type(MetricGroupDeleteResponse, metric_group, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metric_groups.with_raw_response.delete(
            "612",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_group = await response.parse()
        assert_matches_type(MetricGroupDeleteResponse, metric_group, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScorecard) -> None:
        async with async_client.metric_groups.with_streaming_response.delete(
            "612",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_group = await response.parse()
            assert_matches_type(MetricGroupDeleteResponse, metric_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_group_id` but received ''"):
            await async_client.metric_groups.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncScorecard) -> None:
        metric_group = await async_client.metric_groups.get(
            "612",
        )
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metric_groups.with_raw_response.get(
            "612",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric_group = await response.parse()
        assert_matches_type(MetricGroup, metric_group, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncScorecard) -> None:
        async with async_client.metric_groups.with_streaming_response.get(
            "612",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric_group = await response.parse()
            assert_matches_type(MetricGroup, metric_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_group_id` but received ''"):
            await async_client.metric_groups.with_raw_response.get(
                "",
            )
