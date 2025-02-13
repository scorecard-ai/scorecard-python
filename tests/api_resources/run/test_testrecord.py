# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecard import Scorecard, AsyncScorecard
from tests.utils import assert_matches_type
from scorecard.types.run.testrecord import Testrecord

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestrecord:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        testrecord = client.run.testrecord.create(
            run_id=123,
        )
        assert_matches_type(Testrecord, testrecord, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Scorecard) -> None:
        testrecord = client.run.testrecord.create(
            run_id=123,
            context="After the Apollo missions, we know the moon is made of cheese.",
            custom_inputs={"foo": "Here is some example text"},
            custom_labels={"foo": "Here is some example text"},
            custom_outputs={"foo": "Here is some example text"},
            error_message="Error generating a model response.",
            ideal="The moon is made of rock.",
            model_debug_info={
                "completion_token_count": 92,
                "latency_seconds": 3.2360787391662598,
                "prompt_token_count": 28,
                "total_cost": 0.0030399999999999997,
                "total_token_count": 120,
            },
            model_params={
                "isCustom": 0,
                "maxTokens": 2048,
                "modelName": "gpt-4-1106-preview",
                "temperature": 0,
                "topP": 0.9,
            },
            prompt="You are a helpful assistant. Use the provided context to answer the user query.",
            response="The moon is made of cheese.",
            testcase_id=124,
            testset_id=13,
            user_query="What is the moon made of?",
        )
        assert_matches_type(Testrecord, testrecord, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.run.testrecord.with_raw_response.create(
            run_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testrecord = response.parse()
        assert_matches_type(Testrecord, testrecord, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.run.testrecord.with_streaming_response.create(
            run_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testrecord = response.parse()
            assert_matches_type(Testrecord, testrecord, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Scorecard) -> None:
        testrecord = client.run.testrecord.retrieve(
            testrecord_id=0,
            run_id=0,
        )
        assert_matches_type(Testrecord, testrecord, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Scorecard) -> None:
        response = client.run.testrecord.with_raw_response.retrieve(
            testrecord_id=0,
            run_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testrecord = response.parse()
        assert_matches_type(Testrecord, testrecord, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Scorecard) -> None:
        with client.run.testrecord.with_streaming_response.retrieve(
            testrecord_id=0,
            run_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testrecord = response.parse()
            assert_matches_type(Testrecord, testrecord, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTestrecord:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        testrecord = await async_client.run.testrecord.create(
            run_id=123,
        )
        assert_matches_type(Testrecord, testrecord, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncScorecard) -> None:
        testrecord = await async_client.run.testrecord.create(
            run_id=123,
            context="After the Apollo missions, we know the moon is made of cheese.",
            custom_inputs={"foo": "Here is some example text"},
            custom_labels={"foo": "Here is some example text"},
            custom_outputs={"foo": "Here is some example text"},
            error_message="Error generating a model response.",
            ideal="The moon is made of rock.",
            model_debug_info={
                "completion_token_count": 92,
                "latency_seconds": 3.2360787391662598,
                "prompt_token_count": 28,
                "total_cost": 0.0030399999999999997,
                "total_token_count": 120,
            },
            model_params={
                "isCustom": 0,
                "maxTokens": 2048,
                "modelName": "gpt-4-1106-preview",
                "temperature": 0,
                "topP": 0.9,
            },
            prompt="You are a helpful assistant. Use the provided context to answer the user query.",
            response="The moon is made of cheese.",
            testcase_id=124,
            testset_id=13,
            user_query="What is the moon made of?",
        )
        assert_matches_type(Testrecord, testrecord, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.run.testrecord.with_raw_response.create(
            run_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testrecord = await response.parse()
        assert_matches_type(Testrecord, testrecord, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.run.testrecord.with_streaming_response.create(
            run_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testrecord = await response.parse()
            assert_matches_type(Testrecord, testrecord, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncScorecard) -> None:
        testrecord = await async_client.run.testrecord.retrieve(
            testrecord_id=0,
            run_id=0,
        )
        assert_matches_type(Testrecord, testrecord, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncScorecard) -> None:
        response = await async_client.run.testrecord.with_raw_response.retrieve(
            testrecord_id=0,
            run_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testrecord = await response.parse()
        assert_matches_type(Testrecord, testrecord, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncScorecard) -> None:
        async with async_client.run.testrecord.with_streaming_response.retrieve(
            testrecord_id=0,
            run_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testrecord = await response.parse()
            assert_matches_type(Testrecord, testrecord, path=["response"])

        assert cast(Any, response.is_closed) is True
