# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types import Metric

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="int",
            prompt_template="promptTemplate",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="int",
            prompt_template="promptTemplate",
            description="description",
            eval_model_name="evalModelName",
            guidelines="guidelines",
            passing_threshold=1,
            temperature=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="int",
            prompt_template="promptTemplate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="int",
            prompt_template="promptTemplate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.metrics.with_raw_response.create(
                project_id="",
                eval_type="ai",
                name="name",
                output_type="int",
                prompt_template="promptTemplate",
            )

    @parametrize
    def test_method_create_overload_2(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="int",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="int",
            description="description",
            guidelines="guidelines",
            passing_threshold=1,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="int",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="int",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.metrics.with_raw_response.create(
                project_id="",
                eval_type="human",
                name="name",
                output_type="int",
            )

    @parametrize
    def test_method_create_overload_3(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="int",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="int",
            description="description",
            guidelines="guidelines",
            passing_threshold=1,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="int",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="int",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_3(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.metrics.with_raw_response.create(
                project_id="",
                eval_type="heuristic",
                name="name",
                output_type="int",
            )

    @parametrize
    def test_method_create_overload_4(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="boolean",
            prompt_template="promptTemplate",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="boolean",
            prompt_template="promptTemplate",
            description="description",
            eval_model_name="evalModelName",
            guidelines="guidelines",
            temperature=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_create_overload_4(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="boolean",
            prompt_template="promptTemplate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_4(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="boolean",
            prompt_template="promptTemplate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_4(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.metrics.with_raw_response.create(
                project_id="",
                eval_type="ai",
                name="name",
                output_type="boolean",
                prompt_template="promptTemplate",
            )

    @parametrize
    def test_method_create_overload_5(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="boolean",
            description="description",
            guidelines="guidelines",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_create_overload_5(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="boolean",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_5(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="boolean",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_5(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.metrics.with_raw_response.create(
                project_id="",
                eval_type="human",
                name="name",
                output_type="boolean",
            )

    @parametrize
    def test_method_create_overload_6(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="boolean",
            description="description",
            guidelines="guidelines",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_create_overload_6(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="boolean",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_6(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="boolean",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_6(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.metrics.with_raw_response.create(
                project_id="",
                eval_type="heuristic",
                name="name",
                output_type="boolean",
            )


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="int",
            prompt_template="promptTemplate",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="int",
            prompt_template="promptTemplate",
            description="description",
            eval_model_name="evalModelName",
            guidelines="guidelines",
            passing_threshold=1,
            temperature=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="int",
            prompt_template="promptTemplate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="int",
            prompt_template="promptTemplate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.metrics.with_raw_response.create(
                project_id="",
                eval_type="ai",
                name="name",
                output_type="int",
                prompt_template="promptTemplate",
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="int",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="int",
            description="description",
            guidelines="guidelines",
            passing_threshold=1,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="int",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="int",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.metrics.with_raw_response.create(
                project_id="",
                eval_type="human",
                name="name",
                output_type="int",
            )

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="int",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="int",
            description="description",
            guidelines="guidelines",
            passing_threshold=1,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="int",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="int",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.metrics.with_raw_response.create(
                project_id="",
                eval_type="heuristic",
                name="name",
                output_type="int",
            )

    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="boolean",
            prompt_template="promptTemplate",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="boolean",
            prompt_template="promptTemplate",
            description="description",
            eval_model_name="evalModelName",
            guidelines="guidelines",
            temperature=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="boolean",
            prompt_template="promptTemplate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="boolean",
            prompt_template="promptTemplate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.metrics.with_raw_response.create(
                project_id="",
                eval_type="ai",
                name="name",
                output_type="boolean",
                prompt_template="promptTemplate",
            )

    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="boolean",
            description="description",
            guidelines="guidelines",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="boolean",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="boolean",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_5(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.metrics.with_raw_response.create(
                project_id="",
                eval_type="human",
                name="name",
                output_type="boolean",
            )

    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="boolean",
            description="description",
            guidelines="guidelines",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="boolean",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="boolean",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_6(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.metrics.with_raw_response.create(
                project_id="",
                eval_type="heuristic",
                name="name",
                output_type="boolean",
            )
