# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecard import Scorecard, AsyncScorecard
from tests.utils import assert_matches_type
from scorecard.types.run.testrecord import Grade

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScore:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        score = client.run.testrecord.score.create(
            testrecord_id=12,
            run_id=1,
            binary_score=True,
            int_score=10,
            metric_id=1,
            reasoning="The moon is made of cheese.",
        )
        assert_matches_type(Grade, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.run.testrecord.score.with_raw_response.create(
            testrecord_id=12,
            run_id=1,
            binary_score=True,
            int_score=10,
            metric_id=1,
            reasoning="The moon is made of cheese.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = response.parse()
        assert_matches_type(Grade, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.run.testrecord.score.with_streaming_response.create(
            testrecord_id=12,
            run_id=1,
            binary_score=True,
            int_score=10,
            metric_id=1,
            reasoning="The moon is made of cheese.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = response.parse()
            assert_matches_type(Grade, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Scorecard) -> None:
        score = client.run.testrecord.score.update(
            score_id=123,
            run_id=1,
            testrecord_id=12,
            binary_score=False,
            int_score=1,
            reasoning="Turns out the moon insn't acutally made of cheese.",
        )
        assert_matches_type(Grade, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Scorecard) -> None:
        response = client.run.testrecord.score.with_raw_response.update(
            score_id=123,
            run_id=1,
            testrecord_id=12,
            binary_score=False,
            int_score=1,
            reasoning="Turns out the moon insn't acutally made of cheese.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = response.parse()
        assert_matches_type(Grade, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Scorecard) -> None:
        with client.run.testrecord.score.with_streaming_response.update(
            score_id=123,
            run_id=1,
            testrecord_id=12,
            binary_score=False,
            int_score=1,
            reasoning="Turns out the moon insn't acutally made of cheese.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = response.parse()
            assert_matches_type(Grade, score, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScore:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        score = await async_client.run.testrecord.score.create(
            testrecord_id=12,
            run_id=1,
            binary_score=True,
            int_score=10,
            metric_id=1,
            reasoning="The moon is made of cheese.",
        )
        assert_matches_type(Grade, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.run.testrecord.score.with_raw_response.create(
            testrecord_id=12,
            run_id=1,
            binary_score=True,
            int_score=10,
            metric_id=1,
            reasoning="The moon is made of cheese.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = await response.parse()
        assert_matches_type(Grade, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.run.testrecord.score.with_streaming_response.create(
            testrecord_id=12,
            run_id=1,
            binary_score=True,
            int_score=10,
            metric_id=1,
            reasoning="The moon is made of cheese.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = await response.parse()
            assert_matches_type(Grade, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncScorecard) -> None:
        score = await async_client.run.testrecord.score.update(
            score_id=123,
            run_id=1,
            testrecord_id=12,
            binary_score=False,
            int_score=1,
            reasoning="Turns out the moon insn't acutally made of cheese.",
        )
        assert_matches_type(Grade, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecard) -> None:
        response = await async_client.run.testrecord.score.with_raw_response.update(
            score_id=123,
            run_id=1,
            testrecord_id=12,
            binary_score=False,
            int_score=1,
            reasoning="Turns out the moon insn't acutally made of cheese.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = await response.parse()
        assert_matches_type(Grade, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecard) -> None:
        async with async_client.run.testrecord.score.with_streaming_response.update(
            score_id=123,
            run_id=1,
            testrecord_id=12,
            binary_score=False,
            int_score=1,
            reasoning="Turns out the moon insn't acutally made of cheese.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = await response.parse()
            assert_matches_type(Grade, score, path=["response"])

        assert cast(Any, response.is_closed) is True
