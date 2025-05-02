# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types import (
    System,
    SystemDeleteResponse,
)
from scorecard_ai.pagination import SyncPaginatedResponse, AsyncPaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSystems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        system = client.systems.create(
            project_id="314",
            config_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
            description="Production chatbot powered by GPT-4",
            input_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
            name="GPT-4 Chatbot",
            output_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
        )
        assert_matches_type(System, system, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.systems.with_raw_response.create(
            project_id="314",
            config_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
            description="Production chatbot powered by GPT-4",
            input_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
            name="GPT-4 Chatbot",
            output_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        system = response.parse()
        assert_matches_type(System, system, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.systems.with_streaming_response.create(
            project_id="314",
            config_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
            description="Production chatbot powered by GPT-4",
            input_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
            name="GPT-4 Chatbot",
            output_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            system = response.parse()
            assert_matches_type(System, system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.systems.with_raw_response.create(
                project_id="",
                config_schema={
                    "type": "bar",
                    "properties": "bar",
                    "required": "bar",
                },
                description="Production chatbot powered by GPT-4",
                input_schema={
                    "type": "bar",
                    "properties": "bar",
                    "required": "bar",
                },
                name="GPT-4 Chatbot",
                output_schema={
                    "type": "bar",
                    "properties": "bar",
                    "required": "bar",
                },
            )

    @parametrize
    def test_method_update(self, client: Scorecard) -> None:
        system = client.systems.update(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
        )
        assert_matches_type(System, system, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Scorecard) -> None:
        system = client.systems.update(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
            config_schema={"foo": "bar"},
            description="Updated production chatbot powered by GPT-4 Turbo",
            input_schema={"foo": "bar"},
            name="GPT-4 Turbo Chatbot",
            output_schema={"foo": "bar"},
        )
        assert_matches_type(System, system, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Scorecard) -> None:
        response = client.systems.with_raw_response.update(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        system = response.parse()
        assert_matches_type(System, system, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Scorecard) -> None:
        with client.systems.with_streaming_response.update(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            system = response.parse()
            assert_matches_type(System, system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `system_id` but received ''"):
            client.systems.with_raw_response.update(
                system_id="",
            )

    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        system = client.systems.list(
            project_id="314",
        )
        assert_matches_type(SyncPaginatedResponse[System], system, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Scorecard) -> None:
        system = client.systems.list(
            project_id="314",
            cursor="eyJvZmZzZXQiOjAsInBhZ2VJZCI6ImNvZGUifQ",
            limit=20,
        )
        assert_matches_type(SyncPaginatedResponse[System], system, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.systems.with_raw_response.list(
            project_id="314",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        system = response.parse()
        assert_matches_type(SyncPaginatedResponse[System], system, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.systems.with_streaming_response.list(
            project_id="314",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            system = response.parse()
            assert_matches_type(SyncPaginatedResponse[System], system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.systems.with_raw_response.list(
                project_id="",
            )

    @parametrize
    def test_method_delete(self, client: Scorecard) -> None:
        system = client.systems.delete(
            "12345678-0a8b-4f66-b6f3-2ddcfa097257",
        )
        assert_matches_type(SystemDeleteResponse, system, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Scorecard) -> None:
        response = client.systems.with_raw_response.delete(
            "12345678-0a8b-4f66-b6f3-2ddcfa097257",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        system = response.parse()
        assert_matches_type(SystemDeleteResponse, system, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Scorecard) -> None:
        with client.systems.with_streaming_response.delete(
            "12345678-0a8b-4f66-b6f3-2ddcfa097257",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            system = response.parse()
            assert_matches_type(SystemDeleteResponse, system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `system_id` but received ''"):
            client.systems.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Scorecard) -> None:
        system = client.systems.get(
            "12345678-0a8b-4f66-b6f3-2ddcfa097257",
        )
        assert_matches_type(System, system, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Scorecard) -> None:
        response = client.systems.with_raw_response.get(
            "12345678-0a8b-4f66-b6f3-2ddcfa097257",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        system = response.parse()
        assert_matches_type(System, system, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Scorecard) -> None:
        with client.systems.with_streaming_response.get(
            "12345678-0a8b-4f66-b6f3-2ddcfa097257",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            system = response.parse()
            assert_matches_type(System, system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `system_id` but received ''"):
            client.systems.with_raw_response.get(
                "",
            )


class TestAsyncSystems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        system = await async_client.systems.create(
            project_id="314",
            config_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
            description="Production chatbot powered by GPT-4",
            input_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
            name="GPT-4 Chatbot",
            output_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
        )
        assert_matches_type(System, system, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.systems.with_raw_response.create(
            project_id="314",
            config_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
            description="Production chatbot powered by GPT-4",
            input_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
            name="GPT-4 Chatbot",
            output_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        system = await response.parse()
        assert_matches_type(System, system, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.systems.with_streaming_response.create(
            project_id="314",
            config_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
            description="Production chatbot powered by GPT-4",
            input_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
            name="GPT-4 Chatbot",
            output_schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            system = await response.parse()
            assert_matches_type(System, system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.systems.with_raw_response.create(
                project_id="",
                config_schema={
                    "type": "bar",
                    "properties": "bar",
                    "required": "bar",
                },
                description="Production chatbot powered by GPT-4",
                input_schema={
                    "type": "bar",
                    "properties": "bar",
                    "required": "bar",
                },
                name="GPT-4 Chatbot",
                output_schema={
                    "type": "bar",
                    "properties": "bar",
                    "required": "bar",
                },
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncScorecard) -> None:
        system = await async_client.systems.update(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
        )
        assert_matches_type(System, system, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncScorecard) -> None:
        system = await async_client.systems.update(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
            config_schema={"foo": "bar"},
            description="Updated production chatbot powered by GPT-4 Turbo",
            input_schema={"foo": "bar"},
            name="GPT-4 Turbo Chatbot",
            output_schema={"foo": "bar"},
        )
        assert_matches_type(System, system, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecard) -> None:
        response = await async_client.systems.with_raw_response.update(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        system = await response.parse()
        assert_matches_type(System, system, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecard) -> None:
        async with async_client.systems.with_streaming_response.update(
            system_id="12345678-0a8b-4f66-b6f3-2ddcfa097257",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            system = await response.parse()
            assert_matches_type(System, system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `system_id` but received ''"):
            await async_client.systems.with_raw_response.update(
                system_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        system = await async_client.systems.list(
            project_id="314",
        )
        assert_matches_type(AsyncPaginatedResponse[System], system, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecard) -> None:
        system = await async_client.systems.list(
            project_id="314",
            cursor="eyJvZmZzZXQiOjAsInBhZ2VJZCI6ImNvZGUifQ",
            limit=20,
        )
        assert_matches_type(AsyncPaginatedResponse[System], system, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.systems.with_raw_response.list(
            project_id="314",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        system = await response.parse()
        assert_matches_type(AsyncPaginatedResponse[System], system, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.systems.with_streaming_response.list(
            project_id="314",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            system = await response.parse()
            assert_matches_type(AsyncPaginatedResponse[System], system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.systems.with_raw_response.list(
                project_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncScorecard) -> None:
        system = await async_client.systems.delete(
            "12345678-0a8b-4f66-b6f3-2ddcfa097257",
        )
        assert_matches_type(SystemDeleteResponse, system, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScorecard) -> None:
        response = await async_client.systems.with_raw_response.delete(
            "12345678-0a8b-4f66-b6f3-2ddcfa097257",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        system = await response.parse()
        assert_matches_type(SystemDeleteResponse, system, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScorecard) -> None:
        async with async_client.systems.with_streaming_response.delete(
            "12345678-0a8b-4f66-b6f3-2ddcfa097257",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            system = await response.parse()
            assert_matches_type(SystemDeleteResponse, system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `system_id` but received ''"):
            await async_client.systems.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncScorecard) -> None:
        system = await async_client.systems.get(
            "12345678-0a8b-4f66-b6f3-2ddcfa097257",
        )
        assert_matches_type(System, system, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncScorecard) -> None:
        response = await async_client.systems.with_raw_response.get(
            "12345678-0a8b-4f66-b6f3-2ddcfa097257",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        system = await response.parse()
        assert_matches_type(System, system, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncScorecard) -> None:
        async with async_client.systems.with_streaming_response.get(
            "12345678-0a8b-4f66-b6f3-2ddcfa097257",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            system = await response.parse()
            assert_matches_type(System, system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `system_id` but received ''"):
            await async_client.systems.with_raw_response.get(
                "",
            )
