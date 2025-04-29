# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types import Run, RunUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        run = client.runs.create(
            project_id="314",
            metric_ids=["789", "101"],
            testset_id="246",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Scorecard) -> None:
        run = client.runs.create(
            project_id="314",
            metric_ids=["789", "101"],
            testset_id="246",
            system_config_id="87654321-4d3b-4ae4-8c7a-4b6e2a19ccf0",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.runs.with_raw_response.create(
            project_id="314",
            metric_ids=["789", "101"],
            testset_id="246",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.runs.with_streaming_response.create(
            project_id="314",
            metric_ids=["789", "101"],
            testset_id="246",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.runs.with_raw_response.create(
                project_id="",
                metric_ids=["789", "101"],
                testset_id="246",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Scorecard) -> None:
        run = client.runs.update(
            run_id="135",
            status="awaiting_scoring",
        )
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Scorecard) -> None:
        response = client.runs.with_raw_response.update(
            run_id="135",
            status="awaiting_scoring",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Scorecard) -> None:
        with client.runs.with_streaming_response.update(
            run_id="135",
            status="awaiting_scoring",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunUpdateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.update(
                run_id="",
                status="awaiting_scoring",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        run = await async_client.runs.create(
            project_id="314",
            metric_ids=["789", "101"],
            testset_id="246",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncScorecard) -> None:
        run = await async_client.runs.create(
            project_id="314",
            metric_ids=["789", "101"],
            testset_id="246",
            system_config_id="87654321-4d3b-4ae4-8c7a-4b6e2a19ccf0",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.runs.with_raw_response.create(
            project_id="314",
            metric_ids=["789", "101"],
            testset_id="246",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.runs.with_streaming_response.create(
            project_id="314",
            metric_ids=["789", "101"],
            testset_id="246",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.runs.with_raw_response.create(
                project_id="",
                metric_ids=["789", "101"],
                testset_id="246",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncScorecard) -> None:
        run = await async_client.runs.update(
            run_id="135",
            status="awaiting_scoring",
        )
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecard) -> None:
        response = await async_client.runs.with_raw_response.update(
            run_id="135",
            status="awaiting_scoring",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecard) -> None:
        async with async_client.runs.with_streaming_response.update(
            run_id="135",
            status="awaiting_scoring",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunUpdateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.update(
                run_id="",
                status="awaiting_scoring",
            )
