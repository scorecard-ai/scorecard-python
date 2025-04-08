# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecardpy import ScorecardDev, AsyncScorecardDev
from tests.utils import assert_matches_type
from scorecardpy.pagination import SyncPaginatedResponse, AsyncPaginatedResponse
from scorecardpy.types.testsets import (
    TestcaseListResponse,
    TestcaseCreateResponse,
    TestcaseDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestcases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: ScorecardDev) -> None:
        testcase = client.testsets.testcases.create(
            testset_id=0,
            items=[
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
            ],
        )
        assert_matches_type(TestcaseCreateResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: ScorecardDev) -> None:
        response = client.testsets.testcases.with_raw_response.create(
            testset_id=0,
            items=[
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(TestcaseCreateResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: ScorecardDev) -> None:
        with client.testsets.testcases.with_streaming_response.create(
            testset_id=0,
            items=[
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(TestcaseCreateResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: ScorecardDev) -> None:
        testcase = client.testsets.testcases.list(
            testset_id=0,
        )
        assert_matches_type(SyncPaginatedResponse[TestcaseListResponse], testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: ScorecardDev) -> None:
        testcase = client.testsets.testcases.list(
            testset_id=0,
            cursor="cursor",
            limit=20,
        )
        assert_matches_type(SyncPaginatedResponse[TestcaseListResponse], testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: ScorecardDev) -> None:
        response = client.testsets.testcases.with_raw_response.list(
            testset_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(SyncPaginatedResponse[TestcaseListResponse], testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: ScorecardDev) -> None:
        with client.testsets.testcases.with_streaming_response.list(
            testset_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(SyncPaginatedResponse[TestcaseListResponse], testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: ScorecardDev) -> None:
        testcase = client.testsets.testcases.delete(
            testset_id=0,
            ids=[123, 124, 125],
        )
        assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: ScorecardDev) -> None:
        response = client.testsets.testcases.with_raw_response.delete(
            testset_id=0,
            ids=[123, 124, 125],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: ScorecardDev) -> None:
        with client.testsets.testcases.with_streaming_response.delete(
            testset_id=0,
            ids=[123, 124, 125],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTestcases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncScorecardDev) -> None:
        testcase = await async_client.testsets.testcases.create(
            testset_id=0,
            items=[
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
            ],
        )
        assert_matches_type(TestcaseCreateResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecardDev) -> None:
        response = await async_client.testsets.testcases.with_raw_response.create(
            testset_id=0,
            items=[
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(TestcaseCreateResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecardDev) -> None:
        async with async_client.testsets.testcases.with_streaming_response.create(
            testset_id=0,
            items=[
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(TestcaseCreateResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncScorecardDev) -> None:
        testcase = await async_client.testsets.testcases.list(
            testset_id=0,
        )
        assert_matches_type(AsyncPaginatedResponse[TestcaseListResponse], testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecardDev) -> None:
        testcase = await async_client.testsets.testcases.list(
            testset_id=0,
            cursor="cursor",
            limit=20,
        )
        assert_matches_type(AsyncPaginatedResponse[TestcaseListResponse], testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecardDev) -> None:
        response = await async_client.testsets.testcases.with_raw_response.list(
            testset_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(AsyncPaginatedResponse[TestcaseListResponse], testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecardDev) -> None:
        async with async_client.testsets.testcases.with_streaming_response.list(
            testset_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(AsyncPaginatedResponse[TestcaseListResponse], testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncScorecardDev) -> None:
        testcase = await async_client.testsets.testcases.delete(
            testset_id=0,
            ids=[123, 124, 125],
        )
        assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScorecardDev) -> None:
        response = await async_client.testsets.testcases.with_raw_response.delete(
            testset_id=0,
            ids=[123, 124, 125],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScorecardDev) -> None:
        async with async_client.testsets.testcases.with_streaming_response.delete(
            testset_id=0,
            ids=[123, 124, 125],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True
