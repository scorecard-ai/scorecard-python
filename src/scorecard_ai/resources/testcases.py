# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable

import httpx

from ..types import testcase_list_params, testcase_create_params, testcase_delete_params, testcase_update_params
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
from ..pagination import SyncPaginatedResponse, AsyncPaginatedResponse
from .._base_client import AsyncPaginator, make_request_options
from ..types.testcase import Testcase
from ..types.testcase_create_response import TestcaseCreateResponse
from ..types.testcase_delete_response import TestcaseDeleteResponse

__all__ = ["TestcasesResource", "AsyncTestcasesResource"]


class TestcasesResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def with_raw_response(self) -> TestcasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return TestcasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestcasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return TestcasesResourceWithStreamingResponse(self)

    def create(
        self,
        testset_id: str,
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
        Create multiple Testcases in the specified Testset.

        Args:
          items: Testcases to create (max 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not testset_id:
            raise ValueError(f"Expected a non-empty value for `testset_id` but received {testset_id!r}")
        return self._post(
            f"/testsets/{testset_id}/testcases",
            body=maybe_transform({"items": items}, testcase_create_params.TestcaseCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseCreateResponse,
        )

    def update(
        self,
        testcase_id: str,
        *,
        json_data: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testcase:
        """
        Replace the data of an existing Testcase while keeping its ID.

        Args:
          json_data: The JSON data of the Testcase, which is validated against the Testset's schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not testcase_id:
            raise ValueError(f"Expected a non-empty value for `testcase_id` but received {testcase_id!r}")
        return self._put(
            f"/testcases/{testcase_id}",
            body=maybe_transform({"json_data": json_data}, testcase_update_params.TestcaseUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testcase,
        )

    def list(
        self,
        testset_id: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPaginatedResponse[Testcase]:
        """
        Retrieve a paginated list of Testcases belonging to a Testset.

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
        if not testset_id:
            raise ValueError(f"Expected a non-empty value for `testset_id` but received {testset_id!r}")
        return self._get_api_list(
            f"/testsets/{testset_id}/testcases",
            page=SyncPaginatedResponse[Testcase],
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
            model=Testcase,
        )

    def delete(
        self,
        *,
        ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseDeleteResponse:
        """
        Delete multiple Testcases by their IDs.

        Args:
          ids: IDs of Testcases to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/testcases/bulk-delete",
            body=maybe_transform({"ids": ids}, testcase_delete_params.TestcaseDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseDeleteResponse,
        )

    def get(
        self,
        testcase_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testcase:
        """
        Retrieve a specific Testcase by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not testcase_id:
            raise ValueError(f"Expected a non-empty value for `testcase_id` but received {testcase_id!r}")
        return self._get(
            f"/testcases/{testcase_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testcase,
        )


class AsyncTestcasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTestcasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestcasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestcasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AsyncTestcasesResourceWithStreamingResponse(self)

    async def create(
        self,
        testset_id: str,
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
        Create multiple Testcases in the specified Testset.

        Args:
          items: Testcases to create (max 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not testset_id:
            raise ValueError(f"Expected a non-empty value for `testset_id` but received {testset_id!r}")
        return await self._post(
            f"/testsets/{testset_id}/testcases",
            body=await async_maybe_transform({"items": items}, testcase_create_params.TestcaseCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseCreateResponse,
        )

    async def update(
        self,
        testcase_id: str,
        *,
        json_data: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testcase:
        """
        Replace the data of an existing Testcase while keeping its ID.

        Args:
          json_data: The JSON data of the Testcase, which is validated against the Testset's schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not testcase_id:
            raise ValueError(f"Expected a non-empty value for `testcase_id` but received {testcase_id!r}")
        return await self._put(
            f"/testcases/{testcase_id}",
            body=await async_maybe_transform({"json_data": json_data}, testcase_update_params.TestcaseUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testcase,
        )

    def list(
        self,
        testset_id: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Testcase, AsyncPaginatedResponse[Testcase]]:
        """
        Retrieve a paginated list of Testcases belonging to a Testset.

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
        if not testset_id:
            raise ValueError(f"Expected a non-empty value for `testset_id` but received {testset_id!r}")
        return self._get_api_list(
            f"/testsets/{testset_id}/testcases",
            page=AsyncPaginatedResponse[Testcase],
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
            model=Testcase,
        )

    async def delete(
        self,
        *,
        ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseDeleteResponse:
        """
        Delete multiple Testcases by their IDs.

        Args:
          ids: IDs of Testcases to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/testcases/bulk-delete",
            body=await async_maybe_transform({"ids": ids}, testcase_delete_params.TestcaseDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseDeleteResponse,
        )

    async def get(
        self,
        testcase_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testcase:
        """
        Retrieve a specific Testcase by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not testcase_id:
            raise ValueError(f"Expected a non-empty value for `testcase_id` but received {testcase_id!r}")
        return await self._get(
            f"/testcases/{testcase_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testcase,
        )


class TestcasesResourceWithRawResponse:
    __test__ = False

    def __init__(self, testcases: TestcasesResource) -> None:
        self._testcases = testcases

        self.create = to_raw_response_wrapper(
            testcases.create,
        )
        self.update = to_raw_response_wrapper(
            testcases.update,
        )
        self.list = to_raw_response_wrapper(
            testcases.list,
        )
        self.delete = to_raw_response_wrapper(
            testcases.delete,
        )
        self.get = to_raw_response_wrapper(
            testcases.get,
        )


class AsyncTestcasesResourceWithRawResponse:
    def __init__(self, testcases: AsyncTestcasesResource) -> None:
        self._testcases = testcases

        self.create = async_to_raw_response_wrapper(
            testcases.create,
        )
        self.update = async_to_raw_response_wrapper(
            testcases.update,
        )
        self.list = async_to_raw_response_wrapper(
            testcases.list,
        )
        self.delete = async_to_raw_response_wrapper(
            testcases.delete,
        )
        self.get = async_to_raw_response_wrapper(
            testcases.get,
        )


class TestcasesResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, testcases: TestcasesResource) -> None:
        self._testcases = testcases

        self.create = to_streamed_response_wrapper(
            testcases.create,
        )
        self.update = to_streamed_response_wrapper(
            testcases.update,
        )
        self.list = to_streamed_response_wrapper(
            testcases.list,
        )
        self.delete = to_streamed_response_wrapper(
            testcases.delete,
        )
        self.get = to_streamed_response_wrapper(
            testcases.get,
        )


class AsyncTestcasesResourceWithStreamingResponse:
    def __init__(self, testcases: AsyncTestcasesResource) -> None:
        self._testcases = testcases

        self.create = async_to_streamed_response_wrapper(
            testcases.create,
        )
        self.update = async_to_streamed_response_wrapper(
            testcases.update,
        )
        self.list = async_to_streamed_response_wrapper(
            testcases.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            testcases.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            testcases.get,
        )
