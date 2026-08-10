# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types.records import (
    RecordAssignment,
    AssigneeListResponse,
    AssigneeDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssignees:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        assignee = client.records.assignees.create(
            record_id="777",
            assignee_user_id="user_2abc123",
        )
        assert_matches_type(RecordAssignment, assignee, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.records.assignees.with_raw_response.create(
            record_id="777",
            assignee_user_id="user_2abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignee = response.parse()
        assert_matches_type(RecordAssignment, assignee, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.records.assignees.with_streaming_response.create(
            record_id="777",
            assignee_user_id="user_2abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignee = response.parse()
            assert_matches_type(RecordAssignment, assignee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.records.assignees.with_raw_response.create(
                record_id="",
                assignee_user_id="user_2abc123",
            )

    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        assignee = client.records.assignees.list(
            "777",
        )
        assert_matches_type(AssigneeListResponse, assignee, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.records.assignees.with_raw_response.list(
            "777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignee = response.parse()
        assert_matches_type(AssigneeListResponse, assignee, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.records.assignees.with_streaming_response.list(
            "777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignee = response.parse()
            assert_matches_type(AssigneeListResponse, assignee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.records.assignees.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Scorecard) -> None:
        assignee = client.records.assignees.delete(
            assignee_user_id="user_2abc123",
            record_id="777",
        )
        assert_matches_type(AssigneeDeleteResponse, assignee, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Scorecard) -> None:
        response = client.records.assignees.with_raw_response.delete(
            assignee_user_id="user_2abc123",
            record_id="777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignee = response.parse()
        assert_matches_type(AssigneeDeleteResponse, assignee, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Scorecard) -> None:
        with client.records.assignees.with_streaming_response.delete(
            assignee_user_id="user_2abc123",
            record_id="777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignee = response.parse()
            assert_matches_type(AssigneeDeleteResponse, assignee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.records.assignees.with_raw_response.delete(
                assignee_user_id="user_2abc123",
                record_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assignee_user_id` but received ''"):
            client.records.assignees.with_raw_response.delete(
                assignee_user_id="",
                record_id="777",
            )


class TestAsyncAssignees:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        assignee = await async_client.records.assignees.create(
            record_id="777",
            assignee_user_id="user_2abc123",
        )
        assert_matches_type(RecordAssignment, assignee, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.records.assignees.with_raw_response.create(
            record_id="777",
            assignee_user_id="user_2abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignee = await response.parse()
        assert_matches_type(RecordAssignment, assignee, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.records.assignees.with_streaming_response.create(
            record_id="777",
            assignee_user_id="user_2abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignee = await response.parse()
            assert_matches_type(RecordAssignment, assignee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.records.assignees.with_raw_response.create(
                record_id="",
                assignee_user_id="user_2abc123",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        assignee = await async_client.records.assignees.list(
            "777",
        )
        assert_matches_type(AssigneeListResponse, assignee, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.records.assignees.with_raw_response.list(
            "777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignee = await response.parse()
        assert_matches_type(AssigneeListResponse, assignee, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.records.assignees.with_streaming_response.list(
            "777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignee = await response.parse()
            assert_matches_type(AssigneeListResponse, assignee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.records.assignees.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncScorecard) -> None:
        assignee = await async_client.records.assignees.delete(
            assignee_user_id="user_2abc123",
            record_id="777",
        )
        assert_matches_type(AssigneeDeleteResponse, assignee, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScorecard) -> None:
        response = await async_client.records.assignees.with_raw_response.delete(
            assignee_user_id="user_2abc123",
            record_id="777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignee = await response.parse()
        assert_matches_type(AssigneeDeleteResponse, assignee, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScorecard) -> None:
        async with async_client.records.assignees.with_streaming_response.delete(
            assignee_user_id="user_2abc123",
            record_id="777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignee = await response.parse()
            assert_matches_type(AssigneeDeleteResponse, assignee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.records.assignees.with_raw_response.delete(
                assignee_user_id="user_2abc123",
                record_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assignee_user_id` but received ''"):
            await async_client.records.assignees.with_raw_response.delete(
                assignee_user_id="",
                record_id="777",
            )
