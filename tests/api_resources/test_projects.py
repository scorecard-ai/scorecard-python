# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types import Project
from scorecard_ai.pagination import SyncPaginatedResponse, AsyncPaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        project = client.projects.create(
            description="This is a test project",
            name="My Project",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.projects.with_raw_response.create(
            description="This is a test project",
            name="My Project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.projects.with_streaming_response.create(
            description="This is a test project",
            name="My Project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        project = client.projects.list()
        assert_matches_type(SyncPaginatedResponse[Project], project, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Scorecard) -> None:
        project = client.projects.list(
            cursor="123",
            limit=20,
        )
        assert_matches_type(SyncPaginatedResponse[Project], project, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.projects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(SyncPaginatedResponse[Project], project, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.projects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(SyncPaginatedResponse[Project], project, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        project = await async_client.projects.create(
            description="This is a test project",
            name="My Project",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.projects.with_raw_response.create(
            description="This is a test project",
            name="My Project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.projects.with_streaming_response.create(
            description="This is a test project",
            name="My Project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        project = await async_client.projects.list()
        assert_matches_type(AsyncPaginatedResponse[Project], project, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecard) -> None:
        project = await async_client.projects.list(
            cursor="123",
            limit=20,
        )
        assert_matches_type(AsyncPaginatedResponse[Project], project, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.projects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(AsyncPaginatedResponse[Project], project, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.projects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(AsyncPaginatedResponse[Project], project, path=["response"])

        assert cast(Any, response.is_closed) is True
