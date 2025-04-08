# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecardpy import ScorecardDev, AsyncScorecardDev
from tests.utils import assert_matches_type
from scorecardpy.types import (
    TestsetDeleteResponse,
    TestsetUpdateResponse,
    TestsetRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestsets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: ScorecardDev) -> None:
        testset = client.testsets.retrieve(
            0,
        )
        assert_matches_type(TestsetRetrieveResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: ScorecardDev) -> None:
        response = client.testsets.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(TestsetRetrieveResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: ScorecardDev) -> None:
        with client.testsets.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(TestsetRetrieveResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: ScorecardDev) -> None:
        testset = client.testsets.update(
            testset_id=0,
        )
        assert_matches_type(TestsetUpdateResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: ScorecardDev) -> None:
        testset = client.testsets.update(
            testset_id=0,
            description="Updated description for the Q&A testset.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Updated Q&A Testset",
            schema={},
        )
        assert_matches_type(TestsetUpdateResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: ScorecardDev) -> None:
        response = client.testsets.with_raw_response.update(
            testset_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(TestsetUpdateResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: ScorecardDev) -> None:
        with client.testsets.with_streaming_response.update(
            testset_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(TestsetUpdateResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: ScorecardDev) -> None:
        testset = client.testsets.delete(
            0,
        )
        assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: ScorecardDev) -> None:
        response = client.testsets.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: ScorecardDev) -> None:
        with client.testsets.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTestsets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncScorecardDev) -> None:
        testset = await async_client.testsets.retrieve(
            0,
        )
        assert_matches_type(TestsetRetrieveResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncScorecardDev) -> None:
        response = await async_client.testsets.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(TestsetRetrieveResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncScorecardDev) -> None:
        async with async_client.testsets.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(TestsetRetrieveResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncScorecardDev) -> None:
        testset = await async_client.testsets.update(
            testset_id=0,
        )
        assert_matches_type(TestsetUpdateResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncScorecardDev) -> None:
        testset = await async_client.testsets.update(
            testset_id=0,
            description="Updated description for the Q&A testset.",
            field_mapping={
                "inputs": ["string"],
                "labels": ["string"],
                "metadata": ["string"],
            },
            name="Updated Q&A Testset",
            schema={},
        )
        assert_matches_type(TestsetUpdateResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecardDev) -> None:
        response = await async_client.testsets.with_raw_response.update(
            testset_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(TestsetUpdateResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecardDev) -> None:
        async with async_client.testsets.with_streaming_response.update(
            testset_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(TestsetUpdateResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncScorecardDev) -> None:
        testset = await async_client.testsets.delete(
            0,
        )
        assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScorecardDev) -> None:
        response = await async_client.testsets.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScorecardDev) -> None:
        async with async_client.testsets.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(TestsetDeleteResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True
