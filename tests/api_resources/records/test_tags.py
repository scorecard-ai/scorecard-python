# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types.records import RecordTag, TagListResponse, TagDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        tag = client.records.tags.create(
            record_id="777",
            text="urgent",
        )
        assert_matches_type(RecordTag, tag, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.records.tags.with_raw_response.create(
            record_id="777",
            text="urgent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(RecordTag, tag, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.records.tags.with_streaming_response.create(
            record_id="777",
            text="urgent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(RecordTag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.records.tags.with_raw_response.create(
                record_id="",
                text="urgent",
            )

    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        tag = client.records.tags.list(
            "777",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.records.tags.with_raw_response.list(
            "777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.records.tags.with_streaming_response.list(
            "777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.records.tags.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Scorecard) -> None:
        tag = client.records.tags.delete(
            text="urgent",
            record_id="777",
        )
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Scorecard) -> None:
        response = client.records.tags.with_raw_response.delete(
            text="urgent",
            record_id="777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Scorecard) -> None:
        with client.records.tags.with_streaming_response.delete(
            text="urgent",
            record_id="777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagDeleteResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.records.tags.with_raw_response.delete(
                text="urgent",
                record_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `text` but received ''"):
            client.records.tags.with_raw_response.delete(
                text="",
                record_id="777",
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        tag = await async_client.records.tags.create(
            record_id="777",
            text="urgent",
        )
        assert_matches_type(RecordTag, tag, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.records.tags.with_raw_response.create(
            record_id="777",
            text="urgent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(RecordTag, tag, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.records.tags.with_streaming_response.create(
            record_id="777",
            text="urgent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(RecordTag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.records.tags.with_raw_response.create(
                record_id="",
                text="urgent",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        tag = await async_client.records.tags.list(
            "777",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.records.tags.with_raw_response.list(
            "777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.records.tags.with_streaming_response.list(
            "777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.records.tags.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncScorecard) -> None:
        tag = await async_client.records.tags.delete(
            text="urgent",
            record_id="777",
        )
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScorecard) -> None:
        response = await async_client.records.tags.with_raw_response.delete(
            text="urgent",
            record_id="777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScorecard) -> None:
        async with async_client.records.tags.with_streaming_response.delete(
            text="urgent",
            record_id="777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagDeleteResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.records.tags.with_raw_response.delete(
                text="urgent",
                record_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `text` but received ''"):
            await async_client.records.tags.with_raw_response.delete(
                text="",
                record_id="777",
            )
