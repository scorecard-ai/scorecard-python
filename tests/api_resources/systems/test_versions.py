# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types.systems import SystemVersion

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Scorecard) -> None:
        version = client.systems.versions.get(
            "87654321-4d3b-4ae4-8c7a-4b6e2a19ccf0",
        )
        assert_matches_type(SystemVersion, version, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Scorecard) -> None:
        response = client.systems.versions.with_raw_response.get(
            "87654321-4d3b-4ae4-8c7a-4b6e2a19ccf0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(SystemVersion, version, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Scorecard) -> None:
        with client.systems.versions.with_streaming_response.get(
            "87654321-4d3b-4ae4-8c7a-4b6e2a19ccf0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(SystemVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `system_version_id` but received ''"):
            client.systems.versions.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_upsert(self, client: Scorecard) -> None:
        version = client.systems.versions.upsert(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
            config={
                "temperature": "bar",
                "maxTokens": "bar",
                "model": "bar",
            },
        )
        assert_matches_type(SystemVersion, version, path=["response"])

    @parametrize
    def test_method_upsert_with_all_params(self, client: Scorecard) -> None:
        version = client.systems.versions.upsert(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
            config={
                "temperature": "bar",
                "maxTokens": "bar",
                "model": "bar",
            },
            name="Test model: Gemini",
        )
        assert_matches_type(SystemVersion, version, path=["response"])

    @parametrize
    def test_raw_response_upsert(self, client: Scorecard) -> None:
        response = client.systems.versions.with_raw_response.upsert(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
            config={
                "temperature": "bar",
                "maxTokens": "bar",
                "model": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(SystemVersion, version, path=["response"])

    @parametrize
    def test_streaming_response_upsert(self, client: Scorecard) -> None:
        with client.systems.versions.with_streaming_response.upsert(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
            config={
                "temperature": "bar",
                "maxTokens": "bar",
                "model": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(SystemVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upsert(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `system_id` but received ''"):
            client.systems.versions.with_raw_response.upsert(
                system_id="",
                config={
                    "temperature": "bar",
                    "maxTokens": "bar",
                    "model": "bar",
                },
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncScorecard) -> None:
        version = await async_client.systems.versions.get(
            "87654321-4d3b-4ae4-8c7a-4b6e2a19ccf0",
        )
        assert_matches_type(SystemVersion, version, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncScorecard) -> None:
        response = await async_client.systems.versions.with_raw_response.get(
            "87654321-4d3b-4ae4-8c7a-4b6e2a19ccf0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(SystemVersion, version, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncScorecard) -> None:
        async with async_client.systems.versions.with_streaming_response.get(
            "87654321-4d3b-4ae4-8c7a-4b6e2a19ccf0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(SystemVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `system_version_id` but received ''"):
            await async_client.systems.versions.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_upsert(self, async_client: AsyncScorecard) -> None:
        version = await async_client.systems.versions.upsert(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
            config={
                "temperature": "bar",
                "maxTokens": "bar",
                "model": "bar",
            },
        )
        assert_matches_type(SystemVersion, version, path=["response"])

    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncScorecard) -> None:
        version = await async_client.systems.versions.upsert(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
            config={
                "temperature": "bar",
                "maxTokens": "bar",
                "model": "bar",
            },
            name="Test model: Gemini",
        )
        assert_matches_type(SystemVersion, version, path=["response"])

    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncScorecard) -> None:
        response = await async_client.systems.versions.with_raw_response.upsert(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
            config={
                "temperature": "bar",
                "maxTokens": "bar",
                "model": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(SystemVersion, version, path=["response"])

    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncScorecard) -> None:
        async with async_client.systems.versions.with_streaming_response.upsert(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
            config={
                "temperature": "bar",
                "maxTokens": "bar",
                "model": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(SystemVersion, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `system_id` but received ''"):
            await async_client.systems.versions.with_raw_response.upsert(
                system_id="",
                config={
                    "temperature": "bar",
                    "maxTokens": "bar",
                    "model": "bar",
                },
            )
