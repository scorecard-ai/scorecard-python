# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import execution_record_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.execution_record import ExecutionRecord

__all__ = ["ExecutionRecordsResource", "AsyncExecutionRecordsResource"]


class ExecutionRecordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExecutionRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return ExecutionRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecutionRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return ExecutionRecordsResourceWithStreamingResponse(self)

    def create(
        self,
        run_id: str,
        *,
        inputs: Dict[str, object],
        labels: Dict[str, object],
        outputs: Dict[str, object],
        testcase_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionRecord:
        """
        Create a new execution record.

        Args:
          inputs: The actual inputs sent to the system, which should match the system's input
              schema

          labels: The expected outputs for the testcase

          outputs: The actual outputs from the system

          testcase_id: The ID of the testcase

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._post(
            f"/runs/{run_id}/executionrecords",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "labels": labels,
                    "outputs": outputs,
                    "testcase_id": testcase_id,
                },
                execution_record_create_params.ExecutionRecordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionRecord,
        )


class AsyncExecutionRecordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExecutionRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExecutionRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecutionRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AsyncExecutionRecordsResourceWithStreamingResponse(self)

    async def create(
        self,
        run_id: str,
        *,
        inputs: Dict[str, object],
        labels: Dict[str, object],
        outputs: Dict[str, object],
        testcase_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionRecord:
        """
        Create a new execution record.

        Args:
          inputs: The actual inputs sent to the system, which should match the system's input
              schema

          labels: The expected outputs for the testcase

          outputs: The actual outputs from the system

          testcase_id: The ID of the testcase

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._post(
            f"/runs/{run_id}/executionrecords",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "labels": labels,
                    "outputs": outputs,
                    "testcase_id": testcase_id,
                },
                execution_record_create_params.ExecutionRecordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionRecord,
        )


class ExecutionRecordsResourceWithRawResponse:
    def __init__(self, execution_records: ExecutionRecordsResource) -> None:
        self._execution_records = execution_records

        self.create = to_raw_response_wrapper(
            execution_records.create,
        )


class AsyncExecutionRecordsResourceWithRawResponse:
    def __init__(self, execution_records: AsyncExecutionRecordsResource) -> None:
        self._execution_records = execution_records

        self.create = async_to_raw_response_wrapper(
            execution_records.create,
        )


class ExecutionRecordsResourceWithStreamingResponse:
    def __init__(self, execution_records: ExecutionRecordsResource) -> None:
        self._execution_records = execution_records

        self.create = to_streamed_response_wrapper(
            execution_records.create,
        )


class AsyncExecutionRecordsResourceWithStreamingResponse:
    def __init__(self, execution_records: AsyncExecutionRecordsResource) -> None:
        self._execution_records = execution_records

        self.create = async_to_streamed_response_wrapper(
            execution_records.create,
        )
