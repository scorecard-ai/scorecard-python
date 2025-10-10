# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import record_list_params, record_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPaginatedResponse, AsyncPaginatedResponse
from .._base_client import AsyncPaginator, make_request_options
from ..types.record import Record
from ..types.record_list_response import RecordListResponse

__all__ = ["RecordsResource", "AsyncRecordsResource"]


class RecordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return RecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return RecordsResourceWithStreamingResponse(self)

    def create(
        self,
        run_id: str,
        *,
        expected: Dict[str, object],
        inputs: Dict[str, object],
        outputs: Dict[str, object],
        testcase_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Record:
        """
        Create a new Record in a Run.

        Args:
          expected: The expected outputs for the Testcase.

          inputs: The actual inputs sent to the system, which should match the system's input
              schema.

          outputs: The actual outputs from the system.

          testcase_id: The ID of the Testcase.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._post(
            f"/runs/{run_id}/records",
            body=maybe_transform(
                {
                    "expected": expected,
                    "inputs": inputs,
                    "outputs": outputs,
                    "testcase_id": testcase_id,
                },
                record_create_params.RecordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Record,
        )

    def list(
        self,
        run_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedResponse[RecordListResponse]:
        """
        Retrieve a paginated list of Records for a Run, including all scores for each
        record.

        Args:
          cursor: Cursor for pagination. Pass the `nextCursor` from the previous response to get
              the next page of results.

          limit: Maximum number of items to return (1-100). Use with `cursor` for pagination
              through large sets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get_api_list(
            f"/runs/{run_id}/records",
            page=SyncPaginatedResponse[RecordListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    record_list_params.RecordListParams,
                ),
            ),
            model=RecordListResponse,
        )


class AsyncRecordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AsyncRecordsResourceWithStreamingResponse(self)

    async def create(
        self,
        run_id: str,
        *,
        expected: Dict[str, object],
        inputs: Dict[str, object],
        outputs: Dict[str, object],
        testcase_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Record:
        """
        Create a new Record in a Run.

        Args:
          expected: The expected outputs for the Testcase.

          inputs: The actual inputs sent to the system, which should match the system's input
              schema.

          outputs: The actual outputs from the system.

          testcase_id: The ID of the Testcase.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._post(
            f"/runs/{run_id}/records",
            body=await async_maybe_transform(
                {
                    "expected": expected,
                    "inputs": inputs,
                    "outputs": outputs,
                    "testcase_id": testcase_id,
                },
                record_create_params.RecordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Record,
        )

    def list(
        self,
        run_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RecordListResponse, AsyncPaginatedResponse[RecordListResponse]]:
        """
        Retrieve a paginated list of Records for a Run, including all scores for each
        record.

        Args:
          cursor: Cursor for pagination. Pass the `nextCursor` from the previous response to get
              the next page of results.

          limit: Maximum number of items to return (1-100). Use with `cursor` for pagination
              through large sets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get_api_list(
            f"/runs/{run_id}/records",
            page=AsyncPaginatedResponse[RecordListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    record_list_params.RecordListParams,
                ),
            ),
            model=RecordListResponse,
        )


class RecordsResourceWithRawResponse:
    def __init__(self, records: RecordsResource) -> None:
        self._records = records

        self.create = to_raw_response_wrapper(
            records.create,
        )
        self.list = to_raw_response_wrapper(
            records.list,
        )


class AsyncRecordsResourceWithRawResponse:
    def __init__(self, records: AsyncRecordsResource) -> None:
        self._records = records

        self.create = async_to_raw_response_wrapper(
            records.create,
        )
        self.list = async_to_raw_response_wrapper(
            records.list,
        )


class RecordsResourceWithStreamingResponse:
    def __init__(self, records: RecordsResource) -> None:
        self._records = records

        self.create = to_streamed_response_wrapper(
            records.create,
        )
        self.list = to_streamed_response_wrapper(
            records.list,
        )


class AsyncRecordsResourceWithStreamingResponse:
    def __init__(self, records: AsyncRecordsResource) -> None:
        self._records = records

        self.create = async_to_streamed_response_wrapper(
            records.create,
        )
        self.list = async_to_streamed_response_wrapper(
            records.list,
        )
