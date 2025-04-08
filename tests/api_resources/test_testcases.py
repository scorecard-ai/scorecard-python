# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecardpy import Scorecard, AsyncScorecard
from tests.utils import assert_matches_type
from scorecardpy.types.shared import Testcase

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestcases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Scorecard) -> None:
        testcase = client.testcases.update(
            testcase_id=0,
            data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        )
        assert_matches_type(Testcase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Scorecard) -> None:
        response = client.testcases.with_raw_response.update(
            testcase_id=0,
            data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(Testcase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Scorecard) -> None:
        with client.testcases.with_streaming_response.update(
            testcase_id=0,
            data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(Testcase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Scorecard) -> None:
        testcase = client.testcases.get(
            0,
        )
        assert_matches_type(Testcase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Scorecard) -> None:
        response = client.testcases.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(Testcase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Scorecard) -> None:
        with client.testcases.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(Testcase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTestcases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testcases.update(
            testcase_id=0,
            data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        )
        assert_matches_type(Testcase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testcases.with_raw_response.update(
            testcase_id=0,
            data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(Testcase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecard) -> None:
        async with async_client.testcases.with_streaming_response.update(
            testcase_id=0,
            data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(Testcase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testcases.get(
            0,
        )
        assert_matches_type(Testcase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testcases.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(Testcase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncScorecard) -> None:
        async with async_client.testcases.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(Testcase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True
