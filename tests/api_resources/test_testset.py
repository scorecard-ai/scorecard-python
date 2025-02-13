# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecard import Scorecard, AsyncScorecard
from tests.utils import assert_matches_type
from scorecard.types import (
    TestsetListResponse,
    TestsetGetSchemaResponse,
)
from scorecard.types.testset import Testset

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        testset = client.testset.create(
            name="Example Testset",
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Scorecard) -> None:
        testset = client.testset.create(
            name="Example Testset",
            created_by_playground=True,
            custom_schema={
                "variables": [
                    {
                        "data_type": "text",
                        "name": "example_file_url",
                        "role": "input",
                        "description": "example file url",
                    },
                    {
                        "data_type": "text",
                        "name": "example_json_object",
                        "role": "input",
                        "description": "example json object",
                    },
                    {
                        "data_type": "text",
                        "name": "example_text",
                        "role": "input",
                        "description": "example text",
                    },
                ]
            },
            description="A testset to finally confirm if the moon is made of cheese.",
            ingestion_method="csv",
            project_id=123,
            published=True,
            using_retrieval=True,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.testset.with_raw_response.create(
            name="Example Testset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.testset.with_streaming_response.create(
            name="Example Testset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Scorecard) -> None:
        testset = client.testset.retrieve(
            123,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Scorecard) -> None:
        response = client.testset.with_raw_response.retrieve(
            123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Scorecard) -> None:
        with client.testset.with_streaming_response.retrieve(
            123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Scorecard) -> None:
        testset = client.testset.update(
            testset_id=123,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Scorecard) -> None:
        testset = client.testset.update(
            testset_id=123,
            custom_schema={
                "variables": [
                    {
                        "data_type": "text",
                        "name": "example_file_url",
                        "role": "input",
                        "description": "example file url",
                    },
                    {
                        "data_type": "text",
                        "name": "example_json_object",
                        "role": "input",
                        "description": "example json object",
                    },
                    {
                        "data_type": "text",
                        "name": "example_text",
                        "role": "input",
                        "description": "example text",
                    },
                ]
            },
            description="A testset to finally confirm if the moon is made of cheese.",
            name="Example Testset",
            using_retrieval=True,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Scorecard) -> None:
        response = client.testset.with_raw_response.update(
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Scorecard) -> None:
        with client.testset.with_streaming_response.update(
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        testset = client.testset.list()
        assert_matches_type(TestsetListResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Scorecard) -> None:
        testset = client.testset.list(
            cursor="cursor",
            size=0,
        )
        assert_matches_type(TestsetListResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.testset.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(TestsetListResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.testset.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(TestsetListResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Scorecard) -> None:
        testset = client.testset.delete(
            123,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Scorecard) -> None:
        response = client.testset.with_raw_response.delete(
            123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Scorecard) -> None:
        with client.testset.with_streaming_response.delete(
            123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_schema(self, client: Scorecard) -> None:
        testset = client.testset.get_schema(
            123,
        )
        assert_matches_type(TestsetGetSchemaResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_schema(self, client: Scorecard) -> None:
        response = client.testset.with_raw_response.get_schema(
            123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = response.parse()
        assert_matches_type(TestsetGetSchemaResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_schema(self, client: Scorecard) -> None:
        with client.testset.with_streaming_response.get_schema(
            123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = response.parse()
            assert_matches_type(TestsetGetSchemaResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTestset:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testset.create(
            name="Example Testset",
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testset.create(
            name="Example Testset",
            created_by_playground=True,
            custom_schema={
                "variables": [
                    {
                        "data_type": "text",
                        "name": "example_file_url",
                        "role": "input",
                        "description": "example file url",
                    },
                    {
                        "data_type": "text",
                        "name": "example_json_object",
                        "role": "input",
                        "description": "example json object",
                    },
                    {
                        "data_type": "text",
                        "name": "example_text",
                        "role": "input",
                        "description": "example text",
                    },
                ]
            },
            description="A testset to finally confirm if the moon is made of cheese.",
            ingestion_method="csv",
            project_id=123,
            published=True,
            using_retrieval=True,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.with_raw_response.create(
            name="Example Testset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.with_streaming_response.create(
            name="Example Testset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testset.retrieve(
            123,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.with_raw_response.retrieve(
            123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.with_streaming_response.retrieve(
            123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testset.update(
            testset_id=123,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testset.update(
            testset_id=123,
            custom_schema={
                "variables": [
                    {
                        "data_type": "text",
                        "name": "example_file_url",
                        "role": "input",
                        "description": "example file url",
                    },
                    {
                        "data_type": "text",
                        "name": "example_json_object",
                        "role": "input",
                        "description": "example json object",
                    },
                    {
                        "data_type": "text",
                        "name": "example_text",
                        "role": "input",
                        "description": "example text",
                    },
                ]
            },
            description="A testset to finally confirm if the moon is made of cheese.",
            name="Example Testset",
            using_retrieval=True,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.with_raw_response.update(
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.with_streaming_response.update(
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testset.list()
        assert_matches_type(TestsetListResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testset.list(
            cursor="cursor",
            size=0,
        )
        assert_matches_type(TestsetListResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(TestsetListResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(TestsetListResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testset.delete(
            123,
        )
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.with_raw_response.delete(
            123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(Testset, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.with_streaming_response.delete(
            123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(Testset, testset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_schema(self, async_client: AsyncScorecard) -> None:
        testset = await async_client.testset.get_schema(
            123,
        )
        assert_matches_type(TestsetGetSchemaResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_schema(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.with_raw_response.get_schema(
            123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testset = await response.parse()
        assert_matches_type(TestsetGetSchemaResponse, testset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_schema(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.with_streaming_response.get_schema(
            123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testset = await response.parse()
            assert_matches_type(TestsetGetSchemaResponse, testset, path=["response"])

        assert cast(Any, response.is_closed) is True
