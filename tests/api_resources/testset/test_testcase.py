# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scorecard import Scorecard, AsyncScorecard
from tests.utils import assert_matches_type
from scorecard.types.testset import (
    TestCase,
    TestcaseListResponse,
    TestcaseDeleteResponse,
    TestcaseBatchCopyResponse,
    TestcaseBatchDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestcase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        testcase = client.testset.testcase.create(
            testset_id=123,
        )
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Scorecard) -> None:
        testcase = client.testset.testcase.create(
            testset_id=123,
            context="After the Apollo missions, we know the moon is made of cheese.",
            custom_inputs={"foo": "Here is some example text"},
            custom_labels={"foo": "Here is some example text"},
            ideal="The moon is made of rock.",
            user_query="What is the moon made of?",
        )
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.testset.testcase.with_raw_response.create(
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.testset.testcase.with_streaming_response.create(
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(TestCase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Scorecard) -> None:
        testcase = client.testset.testcase.retrieve(
            testcase_id=100,
            testset_id=123,
        )
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Scorecard) -> None:
        response = client.testset.testcase.with_raw_response.retrieve(
            testcase_id=100,
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Scorecard) -> None:
        with client.testset.testcase.with_streaming_response.retrieve(
            testcase_id=100,
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(TestCase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Scorecard) -> None:
        testcase = client.testset.testcase.update(
            testcase_id=123,
            testset_id=123,
        )
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Scorecard) -> None:
        testcase = client.testset.testcase.update(
            testcase_id=123,
            testset_id=123,
            context="After the Apollo missions, we know the moon is made of cheese.",
            custom_inputs={
                "additionalProp1": "Here is some example text",
                "additionalProp2": "Here is some example text",
                "additionalProp3": "Here is some example text",
            },
            custom_labels={
                "additionalProp1": "Here is some example text",
                "additionalProp2": "Here is some example text",
                "additionalProp3": "Here is some example text",
            },
            ideal="The moon is made of rock.",
            user_query="What is the moon made of?",
        )
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Scorecard) -> None:
        response = client.testset.testcase.with_raw_response.update(
            testcase_id=123,
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Scorecard) -> None:
        with client.testset.testcase.with_streaming_response.update(
            testcase_id=123,
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(TestCase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        testcase = client.testset.testcase.list(
            testset_id=1,
        )
        assert_matches_type(TestcaseListResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Scorecard) -> None:
        testcase = client.testset.testcase.list(
            testset_id=1,
            limit=100,
            offset=0,
        )
        assert_matches_type(TestcaseListResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.testset.testcase.with_raw_response.list(
            testset_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(TestcaseListResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.testset.testcase.with_streaming_response.list(
            testset_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(TestcaseListResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Scorecard) -> None:
        testcase = client.testset.testcase.delete(
            testcase_id=100,
            testset_id=123,
        )
        assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Scorecard) -> None:
        response = client.testset.testcase.with_raw_response.delete(
            testcase_id=100,
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Scorecard) -> None:
        with client.testset.testcase.with_streaming_response.delete(
            testcase_id=100,
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_batch_copy(self, client: Scorecard) -> None:
        testcase = client.testset.testcase.batch_copy(
            testset_id=123,
        )
        assert_matches_type(TestcaseBatchCopyResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_batch_copy_with_all_params(self, client: Scorecard) -> None:
        testcase = client.testset.testcase.batch_copy(
            testset_id=123,
            ids=[1, 2, 3, 4],
        )
        assert_matches_type(TestcaseBatchCopyResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_batch_copy(self, client: Scorecard) -> None:
        response = client.testset.testcase.with_raw_response.batch_copy(
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(TestcaseBatchCopyResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_batch_copy(self, client: Scorecard) -> None:
        with client.testset.testcase.with_streaming_response.batch_copy(
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(TestcaseBatchCopyResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_batch_delete(self, client: Scorecard) -> None:
        testcase = client.testset.testcase.batch_delete(
            testset_id=123,
        )
        assert_matches_type(TestcaseBatchDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_batch_delete_with_all_params(self, client: Scorecard) -> None:
        testcase = client.testset.testcase.batch_delete(
            testset_id=123,
            ids=[1, 2, 3, 4],
        )
        assert_matches_type(TestcaseBatchDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_batch_delete(self, client: Scorecard) -> None:
        response = client.testset.testcase.with_raw_response.batch_delete(
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(TestcaseBatchDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_batch_delete(self, client: Scorecard) -> None:
        with client.testset.testcase.with_streaming_response.batch_delete(
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(TestcaseBatchDeleteResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTestcase:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testset.testcase.create(
            testset_id=123,
        )
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testset.testcase.create(
            testset_id=123,
            context="After the Apollo missions, we know the moon is made of cheese.",
            custom_inputs={"foo": "Here is some example text"},
            custom_labels={"foo": "Here is some example text"},
            ideal="The moon is made of rock.",
            user_query="What is the moon made of?",
        )
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.testcase.with_raw_response.create(
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.testcase.with_streaming_response.create(
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(TestCase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testset.testcase.retrieve(
            testcase_id=100,
            testset_id=123,
        )
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.testcase.with_raw_response.retrieve(
            testcase_id=100,
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.testcase.with_streaming_response.retrieve(
            testcase_id=100,
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(TestCase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testset.testcase.update(
            testcase_id=123,
            testset_id=123,
        )
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testset.testcase.update(
            testcase_id=123,
            testset_id=123,
            context="After the Apollo missions, we know the moon is made of cheese.",
            custom_inputs={
                "additionalProp1": "Here is some example text",
                "additionalProp2": "Here is some example text",
                "additionalProp3": "Here is some example text",
            },
            custom_labels={
                "additionalProp1": "Here is some example text",
                "additionalProp2": "Here is some example text",
                "additionalProp3": "Here is some example text",
            },
            ideal="The moon is made of rock.",
            user_query="What is the moon made of?",
        )
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.testcase.with_raw_response.update(
            testcase_id=123,
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(TestCase, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.testcase.with_streaming_response.update(
            testcase_id=123,
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(TestCase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testset.testcase.list(
            testset_id=1,
        )
        assert_matches_type(TestcaseListResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testset.testcase.list(
            testset_id=1,
            limit=100,
            offset=0,
        )
        assert_matches_type(TestcaseListResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.testcase.with_raw_response.list(
            testset_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(TestcaseListResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.testcase.with_streaming_response.list(
            testset_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(TestcaseListResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testset.testcase.delete(
            testcase_id=100,
            testset_id=123,
        )
        assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.testcase.with_raw_response.delete(
            testcase_id=100,
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.testcase.with_streaming_response.delete(
            testcase_id=100,
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_batch_copy(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testset.testcase.batch_copy(
            testset_id=123,
        )
        assert_matches_type(TestcaseBatchCopyResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_batch_copy_with_all_params(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testset.testcase.batch_copy(
            testset_id=123,
            ids=[1, 2, 3, 4],
        )
        assert_matches_type(TestcaseBatchCopyResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_batch_copy(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.testcase.with_raw_response.batch_copy(
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(TestcaseBatchCopyResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_batch_copy(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.testcase.with_streaming_response.batch_copy(
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(TestcaseBatchCopyResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_batch_delete(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testset.testcase.batch_delete(
            testset_id=123,
        )
        assert_matches_type(TestcaseBatchDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_batch_delete_with_all_params(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testset.testcase.batch_delete(
            testset_id=123,
            ids=[1, 2, 3, 4],
        )
        assert_matches_type(TestcaseBatchDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_batch_delete(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testset.testcase.with_raw_response.batch_delete(
            testset_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(TestcaseBatchDeleteResponse, testcase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_batch_delete(self, async_client: AsyncScorecard) -> None:
        async with async_client.testset.testcase.with_streaming_response.batch_delete(
            testset_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(TestcaseBatchDeleteResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True
