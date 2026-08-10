# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types import (
    Attachment,
    AttachmentGetResponse,
    AttachmentDeleteResponse,
    AttachmentInitiateResponse,
)
from scorecard_ai.pagination import SyncPaginatedResponse, AsyncPaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttachments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        attachment = client.attachments.list(
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
        )
        assert_matches_type(SyncPaginatedResponse[Attachment], attachment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Scorecard) -> None:
        attachment = client.attachments.list(
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
            cursor="eyJvZmZzZXQiOjAsInBhZ2VJZCI6ImNvZGUifQ",
            limit=20,
        )
        assert_matches_type(SyncPaginatedResponse[Attachment], attachment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.attachments.with_raw_response.list(
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(SyncPaginatedResponse[Attachment], attachment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.attachments.with_streaming_response.list(
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(SyncPaginatedResponse[Attachment], attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.attachments.with_raw_response.list(
                session_id="",
            )

    @parametrize
    def test_method_delete(self, client: Scorecard) -> None:
        attachment = client.attachments.delete(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Scorecard) -> None:
        response = client.attachments.with_raw_response.delete(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Scorecard) -> None:
        with client.attachments.with_streaming_response.delete(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attachment_id` but received ''"):
            client.attachments.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_commit(self, client: Scorecard) -> None:
        attachment = client.attachments.commit(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(Attachment, attachment, path=["response"])

    @parametrize
    def test_raw_response_commit(self, client: Scorecard) -> None:
        response = client.attachments.with_raw_response.commit(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(Attachment, attachment, path=["response"])

    @parametrize
    def test_streaming_response_commit(self, client: Scorecard) -> None:
        with client.attachments.with_streaming_response.commit(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(Attachment, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_commit(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attachment_id` but received ''"):
            client.attachments.with_raw_response.commit(
                "",
            )

    @parametrize
    def test_method_get(self, client: Scorecard) -> None:
        attachment = client.attachments.get(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(AttachmentGetResponse, attachment, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Scorecard) -> None:
        response = client.attachments.with_raw_response.get(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(AttachmentGetResponse, attachment, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Scorecard) -> None:
        with client.attachments.with_streaming_response.get(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(AttachmentGetResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attachment_id` but received ''"):
            client.attachments.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_initiate(self, client: Scorecard) -> None:
        attachment = client.attachments.initiate(
            content_type="application/pdf",
            file_path="/tmp/report.pdf",
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
            sha256="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            size_bytes=482133,
        )
        assert_matches_type(AttachmentInitiateResponse, attachment, path=["response"])

    @parametrize
    def test_method_initiate_with_all_params(self, client: Scorecard) -> None:
        attachment = client.attachments.initiate(
            content_type="application/pdf",
            file_path="/tmp/report.pdf",
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
            sha256="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            size_bytes=482133,
            filename="report.pdf",
            metadata={"foo": "bar"},
        )
        assert_matches_type(AttachmentInitiateResponse, attachment, path=["response"])

    @parametrize
    def test_raw_response_initiate(self, client: Scorecard) -> None:
        response = client.attachments.with_raw_response.initiate(
            content_type="application/pdf",
            file_path="/tmp/report.pdf",
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
            sha256="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            size_bytes=482133,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(AttachmentInitiateResponse, attachment, path=["response"])

    @parametrize
    def test_streaming_response_initiate(self, client: Scorecard) -> None:
        with client.attachments.with_streaming_response.initiate(
            content_type="application/pdf",
            file_path="/tmp/report.pdf",
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
            sha256="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            size_bytes=482133,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(AttachmentInitiateResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAttachments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        attachment = await async_client.attachments.list(
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
        )
        assert_matches_type(AsyncPaginatedResponse[Attachment], attachment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecard) -> None:
        attachment = await async_client.attachments.list(
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
            cursor="eyJvZmZzZXQiOjAsInBhZ2VJZCI6ImNvZGUifQ",
            limit=20,
        )
        assert_matches_type(AsyncPaginatedResponse[Attachment], attachment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.attachments.with_raw_response.list(
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(AsyncPaginatedResponse[Attachment], attachment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.attachments.with_streaming_response.list(
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(AsyncPaginatedResponse[Attachment], attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.attachments.with_raw_response.list(
                session_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncScorecard) -> None:
        attachment = await async_client.attachments.delete(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScorecard) -> None:
        response = await async_client.attachments.with_raw_response.delete(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScorecard) -> None:
        async with async_client.attachments.with_streaming_response.delete(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attachment_id` but received ''"):
            await async_client.attachments.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_commit(self, async_client: AsyncScorecard) -> None:
        attachment = await async_client.attachments.commit(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(Attachment, attachment, path=["response"])

    @parametrize
    async def test_raw_response_commit(self, async_client: AsyncScorecard) -> None:
        response = await async_client.attachments.with_raw_response.commit(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(Attachment, attachment, path=["response"])

    @parametrize
    async def test_streaming_response_commit(self, async_client: AsyncScorecard) -> None:
        async with async_client.attachments.with_streaming_response.commit(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(Attachment, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_commit(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attachment_id` but received ''"):
            await async_client.attachments.with_raw_response.commit(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncScorecard) -> None:
        attachment = await async_client.attachments.get(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )
        assert_matches_type(AttachmentGetResponse, attachment, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncScorecard) -> None:
        response = await async_client.attachments.with_raw_response.get(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(AttachmentGetResponse, attachment, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncScorecard) -> None:
        async with async_client.attachments.with_streaming_response.get(
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(AttachmentGetResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attachment_id` but received ''"):
            await async_client.attachments.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_initiate(self, async_client: AsyncScorecard) -> None:
        attachment = await async_client.attachments.initiate(
            content_type="application/pdf",
            file_path="/tmp/report.pdf",
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
            sha256="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            size_bytes=482133,
        )
        assert_matches_type(AttachmentInitiateResponse, attachment, path=["response"])

    @parametrize
    async def test_method_initiate_with_all_params(self, async_client: AsyncScorecard) -> None:
        attachment = await async_client.attachments.initiate(
            content_type="application/pdf",
            file_path="/tmp/report.pdf",
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
            sha256="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            size_bytes=482133,
            filename="report.pdf",
            metadata={"foo": "bar"},
        )
        assert_matches_type(AttachmentInitiateResponse, attachment, path=["response"])

    @parametrize
    async def test_raw_response_initiate(self, async_client: AsyncScorecard) -> None:
        response = await async_client.attachments.with_raw_response.initiate(
            content_type="application/pdf",
            file_path="/tmp/report.pdf",
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
            sha256="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            size_bytes=482133,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(AttachmentInitiateResponse, attachment, path=["response"])

    @parametrize
    async def test_streaming_response_initiate(self, async_client: AsyncScorecard) -> None:
        async with async_client.attachments.with_streaming_response.initiate(
            content_type="application/pdf",
            file_path="/tmp/report.pdf",
            session_id="c59e5bd0-e5eb-4bf0-a08a-01f7e8f712c7",
            sha256="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            size_bytes=482133,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(AttachmentInitiateResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True
