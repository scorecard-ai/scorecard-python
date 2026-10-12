# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types import Whoami

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_whoami(self, client: Scorecard) -> None:
        client_ = client.whoami()
        assert_matches_type(Whoami, client_, path=["response"])

    @parametrize
    def test_raw_response_whoami(self, client: Scorecard) -> None:
        response = client.with_raw_response.whoami()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(Whoami, client_, path=["response"])

    @parametrize
    def test_streaming_response_whoami(self, client: Scorecard) -> None:
        with client.with_streaming_response.whoami() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(Whoami, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_whoami(self, async_client: AsyncScorecard) -> None:
        client = await async_client.whoami()
        assert_matches_type(Whoami, client, path=["response"])

    @parametrize
    async def test_raw_response_whoami(self, async_client: AsyncScorecard) -> None:
        response = await async_client.with_raw_response.whoami()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(Whoami, client, path=["response"])

    @parametrize
    async def test_streaming_response_whoami(self, async_client: AsyncScorecard) -> None:
        async with async_client.with_streaming_response.whoami() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(Whoami, client, path=["response"])

        assert cast(Any, response.is_closed) is True
