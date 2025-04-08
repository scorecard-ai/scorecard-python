# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecardpy import Scorecard, AsyncScorecard
from tests.utils import assert_matches_type
from scorecardpy.pagination import SyncPaginatedResponse, AsyncPaginatedResponse
from scorecardpy.types.projects import (
    TestsetListResponse,
    TestsetCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestsets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        testset = client.projects.testsets.create(
            project_id=0,
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Long Context Q&A",
            schema={
                "type": "object",
                "properties": {
                    "question": {"type": "string"},
                    "idealAnswer": {"type": "string"},
                    "provenance": {"type": "string"},
                    "geo": {"type": "string"},
                },
                "fieldMapping": {
                    "inputs": ["question"],
                    "labels": ["idealAnswer"],
                    "metadata": [],
                },
            },
        )
        assert_matches_type(TestsetCreateResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.projects.testsets.with_raw_response.create(
            project_id=0,
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Long Context Q&A",
            schema={
                "type": "object",
                "properties": {
                    "question": {"type": "string"},
                    "idealAnswer": {"type": "string"},
                    "provenance": {"type": "string"},
                    "geo": {"type": "string"},
                },
                "fieldMapping": {
                    "inputs": ["question"],
                    "labels": ["idealAnswer"],
                    "metadata": [],
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(TestsetCreateResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.projects.testsets.with_streaming_response.create(
            project_id=0,
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Long Context Q&A",
            schema={
                "type": "object",
                "properties": {
                    "question": {"type": "string"},
                    "idealAnswer": {"type": "string"},
                    "provenance": {"type": "string"},
                    "geo": {"type": "string"},
                },
                "fieldMapping": {
                    "inputs": ["question"],
                    "labels": ["idealAnswer"],
                    "metadata": [],
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(TestsetCreateResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        testset = client.projects.testsets.list(
            project_id=0,
        )
        assert_matches_type(SyncPaginatedResponse[TestsetListResponse], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Scorecard) -> None:
        testset = client.projects.testsets.list(
            project_id=0,
            cursor="cursor",
            limit=20,
        )
        assert_matches_type(SyncPaginatedResponse[TestsetListResponse], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.projects.testsets.with_raw_response.list(
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(SyncPaginatedResponse[TestsetListResponse], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.projects.testsets.with_streaming_response.list(
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(SyncPaginatedResponse[TestsetListResponse], testset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTestsets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.projects.testsets.create(
            project_id=0,
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Long Context Q&A",
            schema={
                "type": "object",
                "properties": {
                    "question": {"type": "string"},
                    "idealAnswer": {"type": "string"},
                    "provenance": {"type": "string"},
                    "geo": {"type": "string"},
                },
                "fieldMapping": {
                    "inputs": ["question"],
                    "labels": ["idealAnswer"],
                    "metadata": [],
                },
            },
        )
        assert_matches_type(TestsetCreateResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.projects.testsets.with_raw_response.create(
            project_id=0,
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Long Context Q&A",
            schema={
                "type": "object",
                "properties": {
                    "question": {"type": "string"},
                    "idealAnswer": {"type": "string"},
                    "provenance": {"type": "string"},
                    "geo": {"type": "string"},
                },
                "fieldMapping": {
                    "inputs": ["question"],
                    "labels": ["idealAnswer"],
                    "metadata": [],
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(TestsetCreateResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.projects.testsets.with_streaming_response.create(
            project_id=0,
            description="Testset for long context Q&A chatbot.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Long Context Q&A",
            schema={
                "type": "object",
                "properties": {
                    "question": {"type": "string"},
                    "idealAnswer": {"type": "string"},
                    "provenance": {"type": "string"},
                    "geo": {"type": "string"},
                },
                "fieldMapping": {
                    "inputs": ["question"],
                    "labels": ["idealAnswer"],
                    "metadata": [],
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(TestsetCreateResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.projects.testsets.list(
            project_id=0,
        )
        assert_matches_type(AsyncPaginatedResponse[TestsetListResponse], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.projects.testsets.list(
            project_id=0,
            cursor="cursor",
            limit=20,
        )
        assert_matches_type(AsyncPaginatedResponse[TestsetListResponse], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.projects.testsets.with_raw_response.list(
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(AsyncPaginatedResponse[TestsetListResponse], testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.projects.testsets.with_streaming_response.list(
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(AsyncPaginatedResponse[TestsetListResponse], testset, path=["response"])

        assert cast(Any, response.is_closed) is True
