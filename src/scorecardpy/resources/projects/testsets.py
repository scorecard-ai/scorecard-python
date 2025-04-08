# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.projects import testset_list_params, testset_create_params
from ...types.projects.testset_list_response import TestsetListResponse
from ...types.projects.testset_create_response import TestsetCreateResponse

__all__ = ["TestsetsResource", "AsyncTestsetsResource"]


class TestsetsResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def with_raw_response(self) -> TestsetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return TestsetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestsetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return TestsetsResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: int,
        *,
        description: str,
        field_mapping: testset_create_params.FieldMapping,
        name: str,
        schema: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestsetCreateResponse:
        """Create a new testset for a project.

        The testset will be created in the project
        specified in the path.

        Args:
          description: The description of the testset

          field_mapping: Maps top-level keys of the testcase schema to their roles (input/label).
              Unmapped fields are treated as metadata.

          name: The name of the testset

          schema: The JSON schema for each testcase in the testset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/projects/{project_id}/testsets",
            body=maybe_transform(
                {
                    "description": description,
                    "field_mapping": field_mapping,
                    "name": name,
                    "schema": schema,
                },
                testset_create_params.TestsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestsetCreateResponse,
        )

    def list(
        self,
        project_id: int,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPaginatedResponse[TestsetListResponse]:
        """
        Retrieve a paginated list of testsets belonging to a project.

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
            f"/projects/{project_id}/testsets",
            page=SyncPaginatedResponse[TestsetListResponse],
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
                    testset_list_params.TestsetListParams,
                ),
            ),
            model=TestsetListResponse,
        )


class AsyncTestsetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTestsetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestsetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestsetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return AsyncTestsetsResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: int,
        *,
        description: str,
        field_mapping: testset_create_params.FieldMapping,
        name: str,
        schema: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestsetCreateResponse:
        """Create a new testset for a project.

        The testset will be created in the project
        specified in the path.

        Args:
          description: The description of the testset

          field_mapping: Maps top-level keys of the testcase schema to their roles (input/label).
              Unmapped fields are treated as metadata.

          name: The name of the testset

          schema: The JSON schema for each testcase in the testset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/projects/{project_id}/testsets",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "field_mapping": field_mapping,
                    "name": name,
                    "schema": schema,
                },
                testset_create_params.TestsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestsetCreateResponse,
        )

    def list(
        self,
        project_id: int,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TestsetListResponse, AsyncPaginatedResponse[TestsetListResponse]]:
        """
        Retrieve a paginated list of testsets belonging to a project.

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
            f"/projects/{project_id}/testsets",
            page=AsyncPaginatedResponse[TestsetListResponse],
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
                    testset_list_params.TestsetListParams,
                ),
            ),
            model=TestsetListResponse,
        )


class TestsetsResourceWithRawResponse:
    __test__ = False

    def __init__(self, testsets: TestsetsResource) -> None:
        self._testsets = testsets

        self.create = to_raw_response_wrapper(
            testsets.create,
        )
        self.list = to_raw_response_wrapper(
            testsets.list,
        )


class AsyncTestsetsResourceWithRawResponse:
    def __init__(self, testsets: AsyncTestsetsResource) -> None:
        self._testsets = testsets

        self.create = async_to_raw_response_wrapper(
            testsets.create,
        )
        self.list = async_to_raw_response_wrapper(
            testsets.list,
        )


class TestsetsResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, testsets: TestsetsResource) -> None:
        self._testsets = testsets

        self.create = to_streamed_response_wrapper(
            testsets.create,
        )
        self.list = to_streamed_response_wrapper(
            testsets.list,
        )


class AsyncTestsetsResourceWithStreamingResponse:
    def __init__(self, testsets: AsyncTestsetsResource) -> None:
        self._testsets = testsets

        self.create = async_to_streamed_response_wrapper(
            testsets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            testsets.list,
        )
