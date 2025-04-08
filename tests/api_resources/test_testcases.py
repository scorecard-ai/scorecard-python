# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecardpy import ScorecardDev, AsyncScorecardDev
from tests.utils import assert_matches_type
from scorecardpy.types import TestcaseUpdateResponse, TestcaseRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestcases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: ScorecardDev) -> None:
        testcase = client.testcases.retrieve(
            0,
        )
        assert_matches_type(TestcaseRetrieveResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: ScorecardDev) -> None:
        response = client.testcases.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(TestcaseRetrieveResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: ScorecardDev) -> None:
        with client.testcases.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(TestcaseRetrieveResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: ScorecardDev) -> None:
        testcase = client.testcases.update(
            testcase_id=0,
            data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        )
        assert_matches_type(TestcaseUpdateResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: ScorecardDev) -> None:
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
        assert_matches_type(TestcaseUpdateResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: ScorecardDev) -> None:
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
            assert_matches_type(TestcaseUpdateResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTestcases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncScorecardDev) -> None:
        testcase = await async_client.testcases.retrieve(
            0,
        )
        assert_matches_type(TestcaseRetrieveResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncScorecardDev) -> None:
        response = await async_client.testcases.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(TestcaseRetrieveResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncScorecardDev) -> None:
        async with async_client.testcases.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(TestcaseRetrieveResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncScorecardDev) -> None:
        testcase = await async_client.testcases.update(
            testcase_id=0,
            data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        )
        assert_matches_type(TestcaseUpdateResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecardDev) -> None:
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
        assert_matches_type(TestcaseUpdateResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecardDev) -> None:
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
            assert_matches_type(TestcaseUpdateResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True
