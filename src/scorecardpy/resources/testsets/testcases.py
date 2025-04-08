# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPaginatedResponse, AsyncPaginatedResponse
from ..._base_client import AsyncPaginator, make_request_options
from ...types.testsets import testcase_list_params, testcase_create_params, testcase_delete_params
from ...types.testsets.testcase_list_response import TestcaseListResponse
from ...types.testsets.testcase_create_response import TestcaseCreateResponse
from ...types.testsets.testcase_delete_response import TestcaseDeleteResponse

__all__ = ["TestcasesResource", "AsyncTestcasesResource"]


class TestcasesResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def with_raw_response(self) -> TestcasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return TestcasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestcasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return TestcasesResourceWithStreamingResponse(self)

    def create(
        self,
        testset_id: int,
        *,
        items: Iterable[testcase_create_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseCreateResponse:
        """
        Create multiple testcases in the specified testset.

        Args:
          items: Testcases to create (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/testsets/{testset_id}/testcases",
            body=maybe_transform({"items": items}, testcase_create_params.TestcaseCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseCreateResponse,
        )

    def list(
        self,
        testset_id: int,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPaginatedResponse[TestcaseListResponse]:
        """
        Retrieve a paginated list of testcases belonging to a testset.

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
        return self._get_api_list(
            f"/testsets/{testset_id}/testcases",
            page=SyncPaginatedResponse[TestcaseListResponse],
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
                    testcase_list_params.TestcaseListParams,
                ),
            ),
            model=TestcaseListResponse,
        )

    def delete(
        self,
        testset_id: int,
        *,
        ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseDeleteResponse:
        """
        Delete multiple testcases from the specified testset.

        Args:
          ids: IDs of testcases to delete (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/testsets/{testset_id}/testcases",
            body=maybe_transform({"ids": ids}, testcase_delete_params.TestcaseDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseDeleteResponse,
        )


class AsyncTestcasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTestcasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestcasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestcasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return AsyncTestcasesResourceWithStreamingResponse(self)

    async def create(
        self,
        testset_id: int,
        *,
        items: Iterable[testcase_create_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseCreateResponse:
        """
        Create multiple testcases in the specified testset.

        Args:
          items: Testcases to create (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/testsets/{testset_id}/testcases",
            body=await async_maybe_transform({"items": items}, testcase_create_params.TestcaseCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseCreateResponse,
        )

    def list(
        self,
        testset_id: int,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TestcaseListResponse, AsyncPaginatedResponse[TestcaseListResponse]]:
        """
        Retrieve a paginated list of testcases belonging to a testset.

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
        return self._get_api_list(
            f"/testsets/{testset_id}/testcases",
            page=AsyncPaginatedResponse[TestcaseListResponse],
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
                    testcase_list_params.TestcaseListParams,
                ),
            ),
            model=TestcaseListResponse,
        )

    async def delete(
        self,
        testset_id: int,
        *,
        ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseDeleteResponse:
        """
        Delete multiple testcases from the specified testset.

        Args:
          ids: IDs of testcases to delete (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/testsets/{testset_id}/testcases",
            body=await async_maybe_transform({"ids": ids}, testcase_delete_params.TestcaseDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseDeleteResponse,
        )


class TestcasesResourceWithRawResponse:
    __test__ = False

    def __init__(self, testcases: TestcasesResource) -> None:
        self._testcases = testcases

        self.create = to_raw_response_wrapper(
            testcases.create,
        )
        self.list = to_raw_response_wrapper(
            testcases.list,
        )
        self.delete = to_raw_response_wrapper(
            testcases.delete,
        )


class AsyncTestcasesResourceWithRawResponse:
    def __init__(self, testcases: AsyncTestcasesResource) -> None:
        self._testcases = testcases

        self.create = async_to_raw_response_wrapper(
            testcases.create,
        )
        self.list = async_to_raw_response_wrapper(
            testcases.list,
        )
        self.delete = async_to_raw_response_wrapper(
            testcases.delete,
        )


class TestcasesResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, testcases: TestcasesResource) -> None:
        self._testcases = testcases

        self.create = to_streamed_response_wrapper(
            testcases.create,
        )
        self.list = to_streamed_response_wrapper(
            testcases.list,
        )
        self.delete = to_streamed_response_wrapper(
            testcases.delete,
        )


class AsyncTestcasesResourceWithStreamingResponse:
    def __init__(self, testcases: AsyncTestcasesResource) -> None:
        self._testcases = testcases

        self.create = async_to_streamed_response_wrapper(
            testcases.create,
        )
        self.list = async_to_streamed_response_wrapper(
            testcases.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            testcases.delete,
        )
