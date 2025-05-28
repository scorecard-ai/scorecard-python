# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types import Record

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Scorecard) -> None:
        record = client.records.create(
            run_id="135",
            expected={"idealAnswer": "bar"},
            inputs={"question": "bar"},
            outputs={"response": "bar"},
        )
        assert_matches_type(Record, record, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Scorecard) -> None:
        record = client.records.create(
            run_id="135",
            expected={"idealAnswer": "bar"},
            inputs={"question": "bar"},
            outputs={"response": "bar"},
            testcase_id="248",
        )
        assert_matches_type(Record, record, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Scorecard) -> None:
        response = client.records.with_raw_response.create(
            run_id="135",
            expected={"idealAnswer": "bar"},
            inputs={"question": "bar"},
            outputs={"response": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Record, record, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Scorecard) -> None:
        with client.records.with_streaming_response.create(
            run_id="135",
            expected={"idealAnswer": "bar"},
            inputs={"question": "bar"},
            outputs={"response": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Record, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Scorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.records.with_raw_response.create(
                run_id="",
                expected={"idealAnswer": "bar"},
                inputs={"question": "bar"},
                outputs={"response": "bar"},
            )


class TestAsyncRecords:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncScorecard) -> None:
        record = await async_client.records.create(
            run_id="135",
            expected={"idealAnswer": "bar"},
            inputs={"question": "bar"},
            outputs={"response": "bar"},
        )
        assert_matches_type(Record, record, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncScorecard) -> None:
        record = await async_client.records.create(
            run_id="135",
            expected={"idealAnswer": "bar"},
            inputs={"question": "bar"},
            outputs={"response": "bar"},
            testcase_id="248",
        )
        assert_matches_type(Record, record, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScorecard) -> None:
        response = await async_client.records.with_raw_response.create(
            run_id="135",
            expected={"idealAnswer": "bar"},
            inputs={"question": "bar"},
            outputs={"response": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Record, record, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScorecard) -> None:
        async with async_client.records.with_streaming_response.create(
            run_id="135",
            expected={"idealAnswer": "bar"},
            inputs={"question": "bar"},
            outputs={"response": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Record, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncScorecard) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.records.with_raw_response.create(
                run_id="",
                expected={"idealAnswer": "bar"},
                inputs={"question": "bar"},
                outputs={"response": "bar"},
            )
