# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types import (
    Testcase,
    TestcaseCreateResponse,
    TestcaseDeleteResponse,
)
from scorecard_ai.pagination import SyncPaginatedResponse, AsyncPaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestcases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        testcase = client.testcases.create(
            testset_id="246",
            items=[
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
            ],
        )
        assert_matches_type(TestcaseCreateResponse, testcase, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.testcases.with_raw_response.create(
            testset_id="246",
            items=[
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(TestcaseCreateResponse, testcase, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.testcases.with_streaming_response.create(
            testset_id="246",
            items=[
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(TestcaseCreateResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testset_id` but received ''"):
            client.testcases.with_raw_response.create(
                testset_id="",
                items=[
                    {
                        "json_data": {
                            "question": "bar",
                            "idealAnswer": "bar",
                            "provenance": "bar",
                        }
                    },
                    {
                        "json_data": {
                            "question": "bar",
                            "idealAnswer": "bar",
                            "provenance": "bar",
                        }
                    },
                    {
                        "json_data": {
                            "question": "bar",
                            "idealAnswer": "bar",
                            "provenance": "bar",
                        }
                    },
                ],
            )

    @parametrize
    def test_method_update(self, client: Scorecard) -> None:
        testcase = client.testcases.update(
            testcase_id="248",
            json_data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        )
        assert_matches_type(Testcase, testcase, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Scorecard) -> None:
        response = client.testcases.with_raw_response.update(
            testcase_id="248",
            json_data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(Testcase, testcase, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Scorecard) -> None:
        with client.testcases.with_streaming_response.update(
            testcase_id="248",
            json_data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(Testcase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testcase_id` but received ''"):
            client.testcases.with_raw_response.update(
                testcase_id="",
                json_data={
                    "question": "bar",
                    "idealAnswer": "bar",
                    "provenance": "bar",
                },
            )

    @parametrize
    def test_method_list(self, client: Scorecard) -> None:
        testcase = client.testcases.list(
            testset_id="246",
        )
        assert_matches_type(SyncPaginatedResponse[Testcase], testcase, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Scorecard) -> None:
        testcase = client.testcases.list(
            testset_id="246",
            cursor="123",
            limit=20,
        )
        assert_matches_type(SyncPaginatedResponse[Testcase], testcase, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Scorecard) -> None:
        response = client.testcases.with_raw_response.list(
            testset_id="246",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(SyncPaginatedResponse[Testcase], testcase, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Scorecard) -> None:
        with client.testcases.with_streaming_response.list(
            testset_id="246",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(SyncPaginatedResponse[Testcase], testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testset_id` but received ''"):
            client.testcases.with_raw_response.list(
                testset_id="",
            )

    @parametrize
    def test_method_delete(self, client: Scorecard) -> None:
        testcase = client.testcases.delete(
            ids=["123", "124", "125"],
        )
        assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Scorecard) -> None:
        response = client.testcases.with_raw_response.delete(
            ids=["123", "124", "125"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Scorecard) -> None:
        with client.testcases.with_streaming_response.delete(
            ids=["123", "124", "125"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Scorecard) -> None:
        testcase = client.testcases.get(
            "248",
        )
        assert_matches_type(Testcase, testcase, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Scorecard) -> None:
        response = client.testcases.with_raw_response.get(
            "248",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = response.parse()
        assert_matches_type(Testcase, testcase, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Scorecard) -> None:
        with client.testcases.with_streaming_response.get(
            "248",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = response.parse()
            assert_matches_type(Testcase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testcase_id` but received ''"):
            client.testcases.with_raw_response.get(
                "",
            )


class TestAsyncTestcases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testcases.create(
            testset_id="246",
            items=[
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
            ],
        )
        assert_matches_type(TestcaseCreateResponse, testcase, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testcases.with_raw_response.create(
            testset_id="246",
            items=[
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(TestcaseCreateResponse, testcase, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.testcases.with_streaming_response.create(
            testset_id="246",
            items=[
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
                {
                    "json_data": {
                        "question": "bar",
                        "idealAnswer": "bar",
                        "provenance": "bar",
                    }
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(TestcaseCreateResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testset_id` but received ''"):
            await async_client.testcases.with_raw_response.create(
                testset_id="",
                items=[
                    {
                        "json_data": {
                            "question": "bar",
                            "idealAnswer": "bar",
                            "provenance": "bar",
                        }
                    },
                    {
                        "json_data": {
                            "question": "bar",
                            "idealAnswer": "bar",
                            "provenance": "bar",
                        }
                    },
                    {
                        "json_data": {
                            "question": "bar",
                            "idealAnswer": "bar",
                            "provenance": "bar",
                        }
                    },
                ],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testcases.update(
            testcase_id="248",
            json_data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        )
        assert_matches_type(Testcase, testcase, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testcases.with_raw_response.update(
            testcase_id="248",
            json_data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(Testcase, testcase, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncScorecard) -> None:
        async with async_client.testcases.with_streaming_response.update(
            testcase_id="248",
            json_data={
                "question": "bar",
                "idealAnswer": "bar",
                "provenance": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(Testcase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testcase_id` but received ''"):
            await async_client.testcases.with_raw_response.update(
                testcase_id="",
                json_data={
                    "question": "bar",
                    "idealAnswer": "bar",
                    "provenance": "bar",
                },
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testcases.list(
            testset_id="246",
        )
        assert_matches_type(AsyncPaginatedResponse[Testcase], testcase, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testcases.list(
            testset_id="246",
            cursor="123",
            limit=20,
        )
        assert_matches_type(AsyncPaginatedResponse[Testcase], testcase, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testcases.with_raw_response.list(
            testset_id="246",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(AsyncPaginatedResponse[Testcase], testcase, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScorecard) -> None:
        async with async_client.testcases.with_streaming_response.list(
            testset_id="246",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(AsyncPaginatedResponse[Testcase], testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testset_id` but received ''"):
            await async_client.testcases.with_raw_response.list(
                testset_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testcases.delete(
            ids=["123", "124", "125"],
        )
        assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testcases.with_raw_response.delete(
            ids=["123", "124", "125"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScorecard) -> None:
        async with async_client.testcases.with_streaming_response.delete(
            ids=["123", "124", "125"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(TestcaseDeleteResponse, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncScorecard) -> None:
        testcase = await async_client.testcases.get(
            "248",
        )
        assert_matches_type(Testcase, testcase, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncScorecard) -> None:
        response = await async_client.testcases.with_raw_response.get(
            "248",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        testcase = await response.parse()
        assert_matches_type(Testcase, testcase, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncScorecard) -> None:
        async with async_client.testcases.with_streaming_response.get(
            "248",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            testcase = await response.parse()
            assert_matches_type(Testcase, testcase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `testcase_id` but received ''"):
            await async_client.testcases.with_raw_response.get(
                "",
            )
