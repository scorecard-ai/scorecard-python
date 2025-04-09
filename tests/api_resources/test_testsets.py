# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecardpy import Scorecard, AsyncScorecard
from tests.utils import assert_matches_type
from scorecardpy.types import (
    Testcase,
    TestsetDeleteResponse,
    TestsetCreateTestcasesResponse,
    TestsetDeleteTestcasesResponse,
)
from scorecardpy.pagination import SyncPaginatedResponse, AsyncPaginatedResponse
from scorecardpy.types.shared import Testset

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestsets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        testset = client.testsets.create(
            project_id=0,
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Long Context Q&A",
            schema={
                "type": "bar",
                "properties": "bar",
                "fieldMapping": "bar",
            },
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.create(
            project_id=0,
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Long Context Q&A",
            schema={
                "type": "bar",
                "properties": "bar",
                "fieldMapping": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.create(
            project_id=0,
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Long Context Q&A",
            schema={
                "type": "bar",
                "properties": "bar",
                "fieldMapping": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Scorecard) -> None:
        testset = client.testsets.update(
            testset_id=0,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Scorecard) -> None:
        testset = client.testsets.update(
            testset_id=0,
            description="Updated description for the Q&A testset.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Updated Q&A Testset",
            schema={"foo": "bar"},
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.update(
            testset_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.update(
            testset_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        testset = client.testsets.list(
            project_id=0,
        )
        assert_matches_type(SyncPaginatedResponse[Testset], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Scorecard) -> None:
        testset = client.testsets.list(
            project_id=0,
            cursor="cursor",
            limit=20,
        )
        assert_matches_type(SyncPaginatedResponse[Testset], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.list(
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(SyncPaginatedResponse[Testset], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.list(
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(SyncPaginatedResponse[Testset], testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Scorecard) -> None:
        testset = client.testsets.delete(
            0,
        )
        assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_testcases(self, client: Scorecard) -> None:
        testset = client.testsets.create_testcases(
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
        assert_matches_type(TestsetCreateTestcasesResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_testcases(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.create_testcases(
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
        testset = response.parse()
        assert_matches_type(TestsetCreateTestcasesResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_testcases(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.create_testcases(
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

            testset = response.parse()
            assert_matches_type(TestsetCreateTestcasesResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_testcases(self, client: Scorecard) -> None:
        testset = client.testsets.delete_testcases(
            testset_id=0,
            ids=[123, 124, 125],
        )
        assert_matches_type(TestsetDeleteTestcasesResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_testcases(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.delete_testcases(
            testset_id=0,
            ids=[123, 124, 125],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(TestsetDeleteTestcasesResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_testcases(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.delete_testcases(
            testset_id=0,
            ids=[123, 124, 125],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(TestsetDeleteTestcasesResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Scorecard) -> None:
        testset = client.testsets.get(
            0,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_testcases(self, client: Scorecard) -> None:
        testset = client.testsets.list_testcases(
            testset_id=0,
        )
        assert_matches_type(SyncPaginatedResponse[Testcase], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_testcases_with_all_params(self, client: Scorecard) -> None:
        testset = client.testsets.list_testcases(
            testset_id=0,
            cursor="cursor",
            limit=20,
        )
        assert_matches_type(SyncPaginatedResponse[Testcase], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_testcases(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.list_testcases(
            testset_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(SyncPaginatedResponse[Testcase], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_testcases(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.list_testcases(
            testset_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(SyncPaginatedResponse[Testcase], testset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTestsets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.create(
            project_id=0,
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Long Context Q&A",
            schema={
                "type": "bar",
                "properties": "bar",
                "fieldMapping": "bar",
            },
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.create(
            project_id=0,
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Long Context Q&A",
            schema={
                "type": "bar",
                "properties": "bar",
                "fieldMapping": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.create(
            project_id=0,
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Long Context Q&A",
            schema={
                "type": "bar",
                "properties": "bar",
                "fieldMapping": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.update(
            testset_id=0,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.update(
            testset_id=0,
            description="Updated description for the Q&A testset.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Updated Q&A Testset",
            schema={"foo": "bar"},
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.update(
            testset_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.update(
            testset_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.list(
            project_id=0,
        )
        assert_matches_type(AsyncPaginatedResponse[Testset], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.list(
            project_id=0,
            cursor="cursor",
            limit=20,
        )
        assert_matches_type(AsyncPaginatedResponse[Testset], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.list(
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(AsyncPaginatedResponse[Testset], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.list(
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(AsyncPaginatedResponse[Testset], testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.delete(
            0,
        )
        assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_testcases(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.create_testcases(
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
        assert_matches_type(TestsetCreateTestcasesResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_testcases(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.create_testcases(
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
        testset = await response.parse()
        assert_matches_type(TestsetCreateTestcasesResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_testcases(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.create_testcases(
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

            testset = await response.parse()
            assert_matches_type(TestsetCreateTestcasesResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_testcases(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.delete_testcases(
            testset_id=0,
            ids=[123, 124, 125],
        )
        assert_matches_type(TestsetDeleteTestcasesResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_testcases(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.delete_testcases(
            testset_id=0,
            ids=[123, 124, 125],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(TestsetDeleteTestcasesResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_testcases(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.delete_testcases(
            testset_id=0,
            ids=[123, 124, 125],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(TestsetDeleteTestcasesResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.get(
            0,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_testcases(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.list_testcases(
            testset_id=0,
        )
        assert_matches_type(AsyncPaginatedResponse[Testcase], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_testcases_with_all_params(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.list_testcases(
            testset_id=0,
            cursor="cursor",
            limit=20,
        )
        assert_matches_type(AsyncPaginatedResponse[Testcase], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_testcases(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.list_testcases(
            testset_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(AsyncPaginatedResponse[Testcase], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_testcases(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.list_testcases(
            testset_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(AsyncPaginatedResponse[Testcase], testset, path=["response"])

        assert cast(Any, response.is_closed) is True
