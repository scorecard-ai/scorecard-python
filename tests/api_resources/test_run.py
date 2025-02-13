# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecard import Scorecard, AsyncScorecard
from tests.utils import assert_matches_type
from scorecard.types.run import Run

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRun:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        run = client.run.create()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Scorecard) -> None:
        run = client.run.create(
            metrics=[1, 2, 3],
            model_params={
                "isCustom": False,
                "maxTokens": 2048,
                "modelName": "gpt-4-1106-preview",
                "temperature": 0,
                "topP": 0.9,
            },
            notes="This is a test run",
            prompt_id="0003ffd4-6d39-4d34-92c1-9cc9c62bbcfd",
            prompt_template="You are a helpful assistant",
            scoring_config_id=3345,
            source="api",
            status="pending",
            testset_id=1,
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.run.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.run.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Scorecard) -> None:
        run = client.run.retrieve(
            310,
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Scorecard) -> None:
        response = client.run.with_raw_response.retrieve(
            310,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Scorecard) -> None:
        with client.run.with_streaming_response.retrieve(
            310,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update_status(self, client: Scorecard) -> None:
        run = client.run.update_status(
            run_id=310,
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_status_with_all_params(self, client: Scorecard) -> None:
        run = client.run.update_status(
            run_id=310,
            status="pending",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_status(self, client: Scorecard) -> None:
        response = client.run.with_raw_response.update_status(
            run_id=310,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_status(self, client: Scorecard) -> None:
        with client.run.with_streaming_response.update_status(
            run_id=310,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRun:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        run = await async_client.run.create()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncScorecard) -> None:
        run = await async_client.run.create(
            metrics=[1, 2, 3],
            model_params={
                "isCustom": False,
                "maxTokens": 2048,
                "modelName": "gpt-4-1106-preview",
                "temperature": 0,
                "topP": 0.9,
            },
            notes="This is a test run",
            prompt_id="0003ffd4-6d39-4d34-92c1-9cc9c62bbcfd",
            prompt_template="You are a helpful assistant",
            scoring_config_id=3345,
            source="api",
            status="pending",
            testset_id=1,
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.run.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.run.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncScorecard) -> None:
        run = await async_client.run.retrieve(
            310,
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncScorecard) -> None:
        response = await async_client.run.with_raw_response.retrieve(
            310,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncScorecard) -> None:
        async with async_client.run.with_streaming_response.retrieve(
            310,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_status(self, async_client: AsyncScorecard) -> None:
        run = await async_client.run.update_status(
            run_id=310,
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_status_with_all_params(self, async_client: AsyncScorecard) -> None:
        run = await async_client.run.update_status(
            run_id=310,
            status="pending",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncScorecard) -> None:
        response = await async_client.run.with_raw_response.update_status(
            run_id=310,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncScorecard) -> None:
        async with async_client.run.with_streaming_response.update_status(
            run_id=310,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True
