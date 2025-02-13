# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecard import Scorecard, AsyncScorecard
from tests.utils import assert_matches_type
from scorecard.types import (
    Prompt,
    PromptListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompt:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        prompt = client.prompt.create(
            prompt_template="<system>\nYou are a helpful assistant. Use the provided context to answer the user's query.\n\nContext: {context}\n</system>\n\n<user>\n{user_query}\n</user>",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Scorecard) -> None:
        prompt = client.prompt.create(
            prompt_template="<system>\nYou are a helpful assistant. Use the provided context to answer the user's query.\n\nContext: {context}\n</system>\n\n<user>\n{user_query}\n</user>",
            description="Description of the prompt",
            is_prod=True,
            model_params={
                "param1": "value1",
                "param2": 0.1,
                "param3": 100,
                "param4": True,
            },
            name="Prompt Name",
            parent_id="parent_id",
            project_id=0,
            tag="1.0",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.prompt.with_raw_response.create(
            prompt_template="<system>\nYou are a helpful assistant. Use the provided context to answer the user's query.\n\nContext: {context}\n</system>\n\n<user>\n{user_query}\n</user>",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.prompt.with_streaming_response.create(
            prompt_template="<system>\nYou are a helpful assistant. Use the provided context to answer the user's query.\n\nContext: {context}\n</system>\n\n<user>\n{user_query}\n</user>",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Scorecard) -> None:
        prompt = client.prompt.update(
            id="7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Scorecard) -> None:
        prompt = client.prompt.update(
            id="7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
            is_prod=True,
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Scorecard) -> None:
        response = client.prompt.with_raw_response.update(
            id="7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Scorecard) -> None:
        with client.prompt.with_streaming_response.update(
            id="7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompt.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        prompt = client.prompt.list()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Scorecard) -> None:
        prompt = client.prompt.list(
            cursor="cursor",
            project_id=99,
            size=0,
        )
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.prompt.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.prompt.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_root(self, client: Scorecard) -> None:
        prompt = client.prompt.delete_root(
            "7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        )
        assert_matches_type(object, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_root(self, client: Scorecard) -> None:
        response = client.prompt.with_raw_response.delete_root(
            "7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(object, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_root(self, client: Scorecard) -> None:
        with client.prompt.with_streaming_response.delete_root(
            "7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(object, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_root(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompt.with_raw_response.delete_root(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_by_id(self, client: Scorecard) -> None:
        prompt = client.prompt.retrieve_by_id(
            "7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_by_id(self, client: Scorecard) -> None:
        response = client.prompt.with_raw_response.retrieve_by_id(
            "7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_by_id(self, client: Scorecard) -> None:
        with client.prompt.with_streaming_response.retrieve_by_id(
            "7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_by_id(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompt.with_raw_response.retrieve_by_id(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_by_name(self, client: Scorecard) -> None:
        prompt = client.prompt.retrieve_by_name(
            name="name",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_by_name_with_all_params(self, client: Scorecard) -> None:
        prompt = client.prompt.retrieve_by_name(
            name="name",
            tag="tag",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_by_name(self, client: Scorecard) -> None:
        response = client.prompt.with_raw_response.retrieve_by_name(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_by_name(self, client: Scorecard) -> None:
        with client.prompt.with_streaming_response.retrieve_by_name(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrompt:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        prompt = await async_client.prompt.create(
            prompt_template="<system>\nYou are a helpful assistant. Use the provided context to answer the user's query.\n\nContext: {context}\n</system>\n\n<user>\n{user_query}\n</user>",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncScorecard) -> None:
        prompt = await async_client.prompt.create(
            prompt_template="<system>\nYou are a helpful assistant. Use the provided context to answer the user's query.\n\nContext: {context}\n</system>\n\n<user>\n{user_query}\n</user>",
            description="Description of the prompt",
            is_prod=True,
            model_params={
                "param1": "value1",
                "param2": 0.1,
                "param3": 100,
                "param4": True,
            },
            name="Prompt Name",
            parent_id="parent_id",
            project_id=0,
            tag="1.0",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.prompt.with_raw_response.create(
            prompt_template="<system>\nYou are a helpful assistant. Use the provided context to answer the user's query.\n\nContext: {context}\n</system>\n\n<user>\n{user_query}\n</user>",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.prompt.with_streaming_response.create(
            prompt_template="<system>\nYou are a helpful assistant. Use the provided context to answer the user's query.\n\nContext: {context}\n</system>\n\n<user>\n{user_query}\n</user>",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncScorecard) -> None:
        prompt = await async_client.prompt.update(
            id="7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncScorecard) -> None:
        prompt = await async_client.prompt.update(
            id="7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
            is_prod=True,
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecard) -> None:
        response = await async_client.prompt.with_raw_response.update(
            id="7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecard) -> None:
        async with async_client.prompt.with_streaming_response.update(
            id="7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompt.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        prompt = await async_client.prompt.list()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecard) -> None:
        prompt = await async_client.prompt.list(
            cursor="cursor",
            project_id=99,
            size=0,
        )
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.prompt.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.prompt.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_root(self, async_client: AsyncScorecard) -> None:
        prompt = await async_client.prompt.delete_root(
            "7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        )
        assert_matches_type(object, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_root(self, async_client: AsyncScorecard) -> None:
        response = await async_client.prompt.with_raw_response.delete_root(
            "7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(object, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_root(self, async_client: AsyncScorecard) -> None:
        async with async_client.prompt.with_streaming_response.delete_root(
            "7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(object, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_root(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompt.with_raw_response.delete_root(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_by_id(self, async_client: AsyncScorecard) -> None:
        prompt = await async_client.prompt.retrieve_by_id(
            "7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_by_id(self, async_client: AsyncScorecard) -> None:
        response = await async_client.prompt.with_raw_response.retrieve_by_id(
            "7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_by_id(self, async_client: AsyncScorecard) -> None:
        async with async_client.prompt.with_streaming_response.retrieve_by_id(
            "7ac3cbd5-3b99-4e72-97f3-9cd2e749cace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_by_id(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompt.with_raw_response.retrieve_by_id(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_by_name(self, async_client: AsyncScorecard) -> None:
        prompt = await async_client.prompt.retrieve_by_name(
            name="name",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_by_name_with_all_params(self, async_client: AsyncScorecard) -> None:
        prompt = await async_client.prompt.retrieve_by_name(
            name="name",
            tag="tag",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_by_name(self, async_client: AsyncScorecard) -> None:
        response = await async_client.prompt.with_raw_response.retrieve_by_name(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_by_name(self, async_client: AsyncScorecard) -> None:
        async with async_client.prompt.with_streaming_response.retrieve_by_name(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True
