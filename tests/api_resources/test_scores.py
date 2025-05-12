# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types import Score

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_upsert(self, client: Scorecard) -> None:
        score = client.scores.upsert(
            metric_config_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
            record_id="777",
            score={
                "value": "bar",
                "reasoning": "bar",
            },
        )
        assert_matches_type(Score, score, path=["response"])

    @parametrize
    def test_raw_response_upsert(self, client: Scorecard) -> None:
        response = client.scores.with_raw_response.upsert(
            metric_config_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
            record_id="777",
            score={
                "value": "bar",
                "reasoning": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = response.parse()
        assert_matches_type(Score, score, path=["response"])

    @parametrize
    def test_streaming_response_upsert(self, client: Scorecard) -> None:
        with client.scores.with_streaming_response.upsert(
            metric_config_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
            record_id="777",
            score={
                "value": "bar",
                "reasoning": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = response.parse()
            assert_matches_type(Score, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upsert(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.scores.with_raw_response.upsert(
                metric_config_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
                record_id="",
                score={
                    "value": "bar",
                    "reasoning": "bar",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_config_id` but received ''"):
            client.scores.with_raw_response.upsert(
                metric_config_id="",
                record_id="777",
                score={
                    "value": "bar",
                    "reasoning": "bar",
                },
            )


class TestAsyncScores:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_upsert(self, async_client: AsyncScorecard) -> None:
        score = await async_client.scores.upsert(
            metric_config_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
            record_id="777",
            score={
                "value": "bar",
                "reasoning": "bar",
            },
        )
        assert_matches_type(Score, score, path=["response"])

    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncScorecard) -> None:
        response = await async_client.scores.with_raw_response.upsert(
            metric_config_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
            record_id="777",
            score={
                "value": "bar",
                "reasoning": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = await response.parse()
        assert_matches_type(Score, score, path=["response"])

    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncScorecard) -> None:
        async with async_client.scores.with_streaming_response.upsert(
            metric_config_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
            record_id="777",
            score={
                "value": "bar",
                "reasoning": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = await response.parse()
            assert_matches_type(Score, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.scores.with_raw_response.upsert(
                metric_config_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
                record_id="",
                score={
                    "value": "bar",
                    "reasoning": "bar",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_config_id` but received ''"):
            await async_client.scores.with_raw_response.upsert(
                metric_config_id="",
                record_id="777",
                score={
                    "value": "bar",
                    "reasoning": "bar",
                },
            )
