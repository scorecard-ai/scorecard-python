# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types import (
    Testset,
    TestsetDeleteResponse,
)
from scorecard_ai.pagination import SyncPaginatedResponse, AsyncPaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestsets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        testset = client.testsets.create(
            project_id="314",
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "expected": ["idealAnswer"],
                "inputs": ["question"],
                "metadata": ["string"],
            },
            json_schema={
                "type": "bar",
                "properties": "bar",
            },
            name="Long Context Q&A",
        )
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.create(
            project_id="314",
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "expected": ["idealAnswer"],
                "inputs": ["question"],
                "metadata": ["string"],
            },
            json_schema={
                "type": "bar",
                "properties": "bar",
            },
            name="Long Context Q&A",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.create(
            project_id="314",
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "expected": ["idealAnswer"],
                "inputs": ["question"],
                "metadata": ["string"],
            },
            json_schema={
                "type": "bar",
                "properties": "bar",
            },
            name="Long Context Q&A",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.testsets.with_raw_response.create(
                project_id="",
                description="Testset for long context Q&A chatbot.",
                field_mapping={
                    "expected": ["idealAnswer"],
                    "inputs": ["question"],
                    "metadata": ["string"],
                },
                json_schema={
                    "type": "bar",
                    "properties": "bar",
                },
                name="Long Context Q&A",
            )

    @parametrize
    def test_method_update(self, client: Scorecard) -> None:
        testset = client.testsets.update(
            testset_id="246",
        )
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Scorecard) -> None:
        testset = client.testsets.update(
            testset_id="246",
            description="Updated description for the Q&A Testset.",
            field_mapping={
                "expected": ["string"],
                "inputs": ["string"],
                "metadata": ["string"],
            },
            json_schema={"foo": "bar"},
            name="Updated Q&A Testset",
        )
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.update(
            testset_id="246",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.update(
            testset_id="246",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testset_id` but received ''"):
            client.testsets.with_raw_response.update(
                testset_id="",
            )

    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        testset = client.testsets.list(
            project_id="314",
        )
        assert_matches_type(SyncPaginatedResponse[Testset], testset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Scorecard) -> None:
        testset = client.testsets.list(
            project_id="314",
            cursor="123",
            limit=20,
        )
        assert_matches_type(SyncPaginatedResponse[Testset], testset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.list(
            project_id="314",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(SyncPaginatedResponse[Testset], testset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.list(
            project_id="314",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(SyncPaginatedResponse[Testset], testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.testsets.with_raw_response.list(
                project_id="",
            )

    @parametrize
    def test_method_delete(self, client: Scorecard) -> None:
        testset = client.testsets.delete(
            "246",
        )
        assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.delete(
            "246",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.delete(
            "246",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testset_id` but received ''"):
            client.testsets.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Scorecard) -> None:
        testset = client.testsets.get(
            "246",
        )
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Scorecard) -> None:
        response = client.testsets.with_raw_response.get(
            "246",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Scorecard) -> None:
        with client.testsets.with_streaming_response.get(
            "246",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testset_id` but received ''"):
            client.testsets.with_raw_response.get(
                "",
            )


class TestAsyncTestsets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.create(
            project_id="314",
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "expected": ["idealAnswer"],
                "inputs": ["question"],
                "metadata": ["string"],
            },
            json_schema={
                "type": "bar",
                "properties": "bar",
            },
            name="Long Context Q&A",
        )
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.create(
            project_id="314",
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "expected": ["idealAnswer"],
                "inputs": ["question"],
                "metadata": ["string"],
            },
            json_schema={
                "type": "bar",
                "properties": "bar",
            },
            name="Long Context Q&A",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.create(
            project_id="314",
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "expected": ["idealAnswer"],
                "inputs": ["question"],
                "metadata": ["string"],
            },
            json_schema={
                "type": "bar",
                "properties": "bar",
            },
            name="Long Context Q&A",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.testsets.with_raw_response.create(
                project_id="",
                description="Testset for long context Q&A chatbot.",
                field_mapping={
                    "expected": ["idealAnswer"],
                    "inputs": ["question"],
                    "metadata": ["string"],
                },
                json_schema={
                    "type": "bar",
                    "properties": "bar",
                },
                name="Long Context Q&A",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.update(
            testset_id="246",
        )
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.update(
            testset_id="246",
            description="Updated description for the Q&A Testset.",
            field_mapping={
                "expected": ["string"],
                "inputs": ["string"],
                "metadata": ["string"],
            },
            json_schema={"foo": "bar"},
            name="Updated Q&A Testset",
        )
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.update(
            testset_id="246",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.update(
            testset_id="246",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testset_id` but received ''"):
            await async_client.testsets.with_raw_response.update(
                testset_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.list(
            project_id="314",
        )
        assert_matches_type(AsyncPaginatedResponse[Testset], testset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.list(
            project_id="314",
            cursor="123",
            limit=20,
        )
        assert_matches_type(AsyncPaginatedResponse[Testset], testset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.list(
            project_id="314",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(AsyncPaginatedResponse[Testset], testset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.list(
            project_id="314",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(AsyncPaginatedResponse[Testset], testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.testsets.with_raw_response.list(
                project_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.delete(
            "246",
        )
        assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.delete(
            "246",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.delete(
            "246",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testset_id` but received ''"):
            await async_client.testsets.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testsets.get(
            "246",
        )
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testsets.with_raw_response.get(
            "246",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncScorecard) -> None:
        async with async_client.testsets.with_streaming_response.get(
            "246",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testset_id` but received ''"):
            await async_client.testsets.with_raw_response.get(
                "",
            )
