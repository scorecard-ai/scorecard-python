# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types import Metric
from scorecard_ai.pagination import SyncPaginatedResponse, AsyncPaginatedResponse

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
            output_type="float",
            prompt_template="promptTemplate",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="float",
            prompt_template="promptTemplate",
            description="description",
            eval_model_name="evalModelName",
            guidelines="guidelines",
            passing_threshold=0,
            temperature=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_create_overload_4(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="float",
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
            output_type="float",
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
                output_type="float",
                prompt_template="promptTemplate",
            )

    @parametrize
    def test_method_create_overload_5(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="float",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="float",
            description="description",
            guidelines="guidelines",
            passing_threshold=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_create_overload_5(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="float",
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
            output_type="float",
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
                output_type="float",
            )

    @parametrize
    def test_method_create_overload_6(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="float",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="float",
            description="description",
            guidelines="guidelines",
            passing_threshold=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_create_overload_6(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="float",
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
            output_type="float",
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
                output_type="float",
            )

    @parametrize
    def test_method_create_overload_7(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="boolean",
            prompt_template="promptTemplate",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Scorecard) -> None:
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
    def test_raw_response_create_overload_7(self, client: Scorecard) -> None:
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
    def test_streaming_response_create_overload_7(self, client: Scorecard) -> None:
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
    def test_path_params_create_overload_7(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.metrics.with_raw_response.create(
                project_id="",
                eval_type="ai",
                name="name",
                output_type="boolean",
                prompt_template="promptTemplate",
            )

    @parametrize
    def test_method_create_overload_8(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Scorecard) -> None:
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
    def test_raw_response_create_overload_8(self, client: Scorecard) -> None:
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
    def test_streaming_response_create_overload_8(self, client: Scorecard) -> None:
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
    def test_path_params_create_overload_8(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.metrics.with_raw_response.create(
                project_id="",
                eval_type="human",
                name="name",
                output_type="boolean",
            )

    @parametrize
    def test_method_create_overload_9(self, client: Scorecard) -> None:
        metric = client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_9(self, client: Scorecard) -> None:
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
    def test_raw_response_create_overload_9(self, client: Scorecard) -> None:
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
    def test_streaming_response_create_overload_9(self, client: Scorecard) -> None:
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
    def test_path_params_create_overload_9(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.metrics.with_raw_response.create(
                project_id="",
                eval_type="heuristic",
                name="name",
                output_type="boolean",
            )

    @parametrize
    def test_method_update_overload_1(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="ai",
            output_type="int",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="ai",
            output_type="int",
            description="description",
            eval_model_name="evalModelName",
            guidelines="guidelines",
            name="name",
            passing_threshold=1,
            prompt_template="promptTemplate",
            temperature=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="ai",
            output_type="int",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="ai",
            output_type="int",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="ai",
                output_type="int",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="human",
            output_type="int",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="human",
            output_type="int",
            description="description",
            guidelines="guidelines",
            name="name",
            passing_threshold=1,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="human",
            output_type="int",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="human",
            output_type="int",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="human",
                output_type="int",
            )

    @parametrize
    def test_method_update_overload_3(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="int",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="int",
            description="description",
            guidelines="guidelines",
            name="name",
            passing_threshold=1,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_update_overload_3(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="int",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_3(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="int",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_3(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="heuristic",
                output_type="int",
            )

    @parametrize
    def test_method_update_overload_4(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="ai",
            output_type="float",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="ai",
            output_type="float",
            description="description",
            eval_model_name="evalModelName",
            guidelines="guidelines",
            name="name",
            passing_threshold=0,
            prompt_template="promptTemplate",
            temperature=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_update_overload_4(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="ai",
            output_type="float",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_4(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="ai",
            output_type="float",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_4(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="ai",
                output_type="float",
            )

    @parametrize
    def test_method_update_overload_5(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="human",
            output_type="float",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="human",
            output_type="float",
            description="description",
            guidelines="guidelines",
            name="name",
            passing_threshold=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_update_overload_5(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="human",
            output_type="float",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_5(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="human",
            output_type="float",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_5(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="human",
                output_type="float",
            )

    @parametrize
    def test_method_update_overload_6(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="float",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_6(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="float",
            description="description",
            guidelines="guidelines",
            name="name",
            passing_threshold=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_update_overload_6(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="float",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_6(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="float",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_6(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="heuristic",
                output_type="float",
            )

    @parametrize
    def test_method_update_overload_7(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="ai",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_7(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="ai",
            output_type="boolean",
            description="description",
            eval_model_name="evalModelName",
            guidelines="guidelines",
            name="name",
            prompt_template="promptTemplate",
            temperature=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_update_overload_7(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="ai",
            output_type="boolean",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_7(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="ai",
            output_type="boolean",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_7(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="ai",
                output_type="boolean",
            )

    @parametrize
    def test_method_update_overload_8(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="human",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_8(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="human",
            output_type="boolean",
            description="description",
            guidelines="guidelines",
            name="name",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_update_overload_8(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="human",
            output_type="boolean",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_8(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="human",
            output_type="boolean",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_8(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="human",
                output_type="boolean",
            )

    @parametrize
    def test_method_update_overload_9(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_9(self, client: Scorecard) -> None:
        metric = client.metrics.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="boolean",
            description="description",
            guidelines="guidelines",
            name="name",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_update_overload_9(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="boolean",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_9(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="boolean",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_9(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="heuristic",
                output_type="boolean",
            )

    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        metric = client.metrics.list(
            project_id="314",
        )
        assert_matches_type(SyncPaginatedResponse[Metric], metric, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Scorecard) -> None:
        metric = client.metrics.list(
            project_id="314",
            cursor="123",
            limit=20,
        )
        assert_matches_type(SyncPaginatedResponse[Metric], metric, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.list(
            project_id="314",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(SyncPaginatedResponse[Metric], metric, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.list(
            project_id="314",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(SyncPaginatedResponse[Metric], metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.metrics.with_raw_response.list(
                project_id="",
            )

    @parametrize
    def test_method_get(self, client: Scorecard) -> None:
        metric = client.metrics.get(
            "321",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Scorecard) -> None:
        response = client.metrics.with_raw_response.get(
            "321",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Scorecard) -> None:
        with client.metrics.with_streaming_response.get(
            "321",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.get(
                "",
            )


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

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
            output_type="float",
            prompt_template="promptTemplate",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="float",
            prompt_template="promptTemplate",
            description="description",
            eval_model_name="evalModelName",
            guidelines="guidelines",
            passing_threshold=0,
            temperature=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="float",
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
            output_type="float",
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
                output_type="float",
                prompt_template="promptTemplate",
            )

    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="float",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="float",
            description="description",
            guidelines="guidelines",
            passing_threshold=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="float",
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
            output_type="float",
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
                output_type="float",
            )

    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="float",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="float",
            description="description",
            guidelines="guidelines",
            passing_threshold=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="float",
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
            output_type="float",
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
                output_type="float",
            )

    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="ai",
            name="name",
            output_type="boolean",
            prompt_template="promptTemplate",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncScorecard) -> None:
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
    async def test_raw_response_create_overload_7(self, async_client: AsyncScorecard) -> None:
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
    async def test_streaming_response_create_overload_7(self, async_client: AsyncScorecard) -> None:
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
    async def test_path_params_create_overload_7(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.metrics.with_raw_response.create(
                project_id="",
                eval_type="ai",
                name="name",
                output_type="boolean",
                prompt_template="promptTemplate",
            )

    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="human",
            name="name",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncScorecard) -> None:
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
    async def test_raw_response_create_overload_8(self, async_client: AsyncScorecard) -> None:
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
    async def test_streaming_response_create_overload_8(self, async_client: AsyncScorecard) -> None:
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
    async def test_path_params_create_overload_8(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.metrics.with_raw_response.create(
                project_id="",
                eval_type="human",
                name="name",
                output_type="boolean",
            )

    @parametrize
    async def test_method_create_overload_9(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.create(
            project_id="314",
            eval_type="heuristic",
            name="name",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_9(self, async_client: AsyncScorecard) -> None:
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
    async def test_raw_response_create_overload_9(self, async_client: AsyncScorecard) -> None:
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
    async def test_streaming_response_create_overload_9(self, async_client: AsyncScorecard) -> None:
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
    async def test_path_params_create_overload_9(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.metrics.with_raw_response.create(
                project_id="",
                eval_type="heuristic",
                name="name",
                output_type="boolean",
            )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="ai",
            output_type="int",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="ai",
            output_type="int",
            description="description",
            eval_model_name="evalModelName",
            guidelines="guidelines",
            name="name",
            passing_threshold=1,
            prompt_template="promptTemplate",
            temperature=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="ai",
            output_type="int",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="ai",
            output_type="int",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="ai",
                output_type="int",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="human",
            output_type="int",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="human",
            output_type="int",
            description="description",
            guidelines="guidelines",
            name="name",
            passing_threshold=1,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="human",
            output_type="int",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="human",
            output_type="int",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="human",
                output_type="int",
            )

    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="int",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="int",
            description="description",
            guidelines="guidelines",
            name="name",
            passing_threshold=1,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="int",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="int",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="heuristic",
                output_type="int",
            )

    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="ai",
            output_type="float",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="ai",
            output_type="float",
            description="description",
            eval_model_name="evalModelName",
            guidelines="guidelines",
            name="name",
            passing_threshold=0,
            prompt_template="promptTemplate",
            temperature=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="ai",
            output_type="float",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="ai",
            output_type="float",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="ai",
                output_type="float",
            )

    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="human",
            output_type="float",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="human",
            output_type="float",
            description="description",
            guidelines="guidelines",
            name="name",
            passing_threshold=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="human",
            output_type="float",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="human",
            output_type="float",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="human",
                output_type="float",
            )

    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="float",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_6(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="float",
            description="description",
            guidelines="guidelines",
            name="name",
            passing_threshold=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="float",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="float",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_6(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="heuristic",
                output_type="float",
            )

    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="ai",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_7(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="ai",
            output_type="boolean",
            description="description",
            eval_model_name="evalModelName",
            guidelines="guidelines",
            name="name",
            prompt_template="promptTemplate",
            temperature=0,
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="ai",
            output_type="boolean",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_7(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="ai",
            output_type="boolean",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_7(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="ai",
                output_type="boolean",
            )

    @parametrize
    async def test_method_update_overload_8(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="human",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_8(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="human",
            output_type="boolean",
            description="description",
            guidelines="guidelines",
            name="name",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_8(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="human",
            output_type="boolean",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_8(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="human",
            output_type="boolean",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_8(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="human",
                output_type="boolean",
            )

    @parametrize
    async def test_method_update_overload_9(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="boolean",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_9(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="boolean",
            description="description",
            guidelines="guidelines",
            name="name",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_9(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="boolean",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_9(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.update(
            metric_id="321",
            eval_type="heuristic",
            output_type="boolean",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_9(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.update(
                metric_id="",
                eval_type="heuristic",
                output_type="boolean",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.list(
            project_id="314",
        )
        assert_matches_type(AsyncPaginatedResponse[Metric], metric, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.list(
            project_id="314",
            cursor="123",
            limit=20,
        )
        assert_matches_type(AsyncPaginatedResponse[Metric], metric, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.list(
            project_id="314",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(AsyncPaginatedResponse[Metric], metric, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.list(
            project_id="314",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(AsyncPaginatedResponse[Metric], metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.metrics.with_raw_response.list(
                project_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncScorecard) -> None:
        metric = await async_client.metrics.get(
            "321",
        )
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncScorecard) -> None:
        response = await async_client.metrics.with_raw_response.get(
            "321",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(Metric, metric, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncScorecard) -> None:
        async with async_client.metrics.with_streaming_response.get(
            "321",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(Metric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.get(
                "",
            )
