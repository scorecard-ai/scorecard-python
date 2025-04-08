# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    testset_list_params,
    testset_create_params,
    testset_update_params,
    testset_list_testcases_params,
    testset_create_testcases_params,
    testset_delete_testcases_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ..types.shared.testset import Testset
from ..types.testset_delete_response import TestsetDeleteResponse
from ..types.testset_list_testcases_response import TestsetListTestcasesResponse
from ..types.testset_create_testcases_response import TestsetCreateTestcasesResponse
from ..types.testset_delete_testcases_response import TestsetDeleteTestcasesResponse

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
    ) -> Testset:
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
            cast_to=Testset,
        )

    def update(
        self,
        testset_id: int,
        *,
        description: str | NotGiven = NOT_GIVEN,
        field_mapping: testset_update_params.FieldMapping | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        schema: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testset:
        """Update a testset.

        Only the fields provided in the request body will be updated.
        If a field is provided, the new content will replace the existing content. If a
        field is not provided, the existing content will remain unchanged.

        When updating the schema:

        - If field mappings are not provided and existing mappings reference fields that
          no longer exist, those mappings will be automatically removed
        - To preserve all existing mappings, ensure all referenced fields remain in the
          updated schema
        - For complete control, provide both schema and fieldMapping when updating the
          schema

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
        return self._patch(
            f"/testsets/{testset_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "field_mapping": field_mapping,
                    "name": name,
                    "schema": schema,
                },
                testset_update_params.TestsetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testset,
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
    ) -> SyncPaginatedResponse[Testset]:
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
            page=SyncPaginatedResponse[Testset],
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
            model=Testset,
        )

    def delete(
        self,
        testset_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestsetDeleteResponse:
        """
        Delete a testset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/testsets/{testset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestsetDeleteResponse,
        )

    def create_testcases(
        self,
        testset_id: int,
        *,
        items: Iterable[testset_create_testcases_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestsetCreateTestcasesResponse:
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
            body=maybe_transform({"items": items}, testset_create_testcases_params.TestsetCreateTestcasesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestsetCreateTestcasesResponse,
        )

    def delete_testcases(
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
    ) -> TestsetDeleteTestcasesResponse:
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
            body=maybe_transform({"ids": ids}, testset_delete_testcases_params.TestsetDeleteTestcasesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestsetDeleteTestcasesResponse,
        )

    def get(
        self,
        testset_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testset:
        """
        Get a testset by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/testsets/{testset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testset,
        )

    def list_testcases(
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
    ) -> TestsetListTestcasesResponse:
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
        return self._get(
            f"/testsets/{testset_id}/testcases",
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
                    testset_list_testcases_params.TestsetListTestcasesParams,
                ),
            ),
            cast_to=TestsetListTestcasesResponse,
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
    ) -> Testset:
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
            cast_to=Testset,
        )

    async def update(
        self,
        testset_id: int,
        *,
        description: str | NotGiven = NOT_GIVEN,
        field_mapping: testset_update_params.FieldMapping | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        schema: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testset:
        """Update a testset.

        Only the fields provided in the request body will be updated.
        If a field is provided, the new content will replace the existing content. If a
        field is not provided, the existing content will remain unchanged.

        When updating the schema:

        - If field mappings are not provided and existing mappings reference fields that
          no longer exist, those mappings will be automatically removed
        - To preserve all existing mappings, ensure all referenced fields remain in the
          updated schema
        - For complete control, provide both schema and fieldMapping when updating the
          schema

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
        return await self._patch(
            f"/testsets/{testset_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "field_mapping": field_mapping,
                    "name": name,
                    "schema": schema,
                },
                testset_update_params.TestsetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testset,
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
    ) -> AsyncPaginator[Testset, AsyncPaginatedResponse[Testset]]:
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
            page=AsyncPaginatedResponse[Testset],
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
            model=Testset,
        )

    async def delete(
        self,
        testset_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestsetDeleteResponse:
        """
        Delete a testset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/testsets/{testset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestsetDeleteResponse,
        )

    async def create_testcases(
        self,
        testset_id: int,
        *,
        items: Iterable[testset_create_testcases_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestsetCreateTestcasesResponse:
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
            body=await async_maybe_transform(
                {"items": items}, testset_create_testcases_params.TestsetCreateTestcasesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestsetCreateTestcasesResponse,
        )

    async def delete_testcases(
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
    ) -> TestsetDeleteTestcasesResponse:
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
            body=await async_maybe_transform(
                {"ids": ids}, testset_delete_testcases_params.TestsetDeleteTestcasesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestsetDeleteTestcasesResponse,
        )

    async def get(
        self,
        testset_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testset:
        """
        Get a testset by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/testsets/{testset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testset,
        )

    async def list_testcases(
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
    ) -> TestsetListTestcasesResponse:
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
        return await self._get(
            f"/testsets/{testset_id}/testcases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    testset_list_testcases_params.TestsetListTestcasesParams,
                ),
            ),
            cast_to=TestsetListTestcasesResponse,
        )


class TestsetsResourceWithRawResponse:
    __test__ = False

    def __init__(self, testsets: TestsetsResource) -> None:
        self._testsets = testsets

        self.create = to_raw_response_wrapper(
            testsets.create,
        )
        self.update = to_raw_response_wrapper(
            testsets.update,
        )
        self.list = to_raw_response_wrapper(
            testsets.list,
        )
        self.delete = to_raw_response_wrapper(
            testsets.delete,
        )
        self.create_testcases = to_raw_response_wrapper(
            testsets.create_testcases,
        )
        self.delete_testcases = to_raw_response_wrapper(
            testsets.delete_testcases,
        )
        self.get = to_raw_response_wrapper(
            testsets.get,
        )
        self.list_testcases = to_raw_response_wrapper(
            testsets.list_testcases,
        )


class AsyncTestsetsResourceWithRawResponse:
    def __init__(self, testsets: AsyncTestsetsResource) -> None:
        self._testsets = testsets

        self.create = async_to_raw_response_wrapper(
            testsets.create,
        )
        self.update = async_to_raw_response_wrapper(
            testsets.update,
        )
        self.list = async_to_raw_response_wrapper(
            testsets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            testsets.delete,
        )
        self.create_testcases = async_to_raw_response_wrapper(
            testsets.create_testcases,
        )
        self.delete_testcases = async_to_raw_response_wrapper(
            testsets.delete_testcases,
        )
        self.get = async_to_raw_response_wrapper(
            testsets.get,
        )
        self.list_testcases = async_to_raw_response_wrapper(
            testsets.list_testcases,
        )


class TestsetsResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, testsets: TestsetsResource) -> None:
        self._testsets = testsets

        self.create = to_streamed_response_wrapper(
            testsets.create,
        )
        self.update = to_streamed_response_wrapper(
            testsets.update,
        )
        self.list = to_streamed_response_wrapper(
            testsets.list,
        )
        self.delete = to_streamed_response_wrapper(
            testsets.delete,
        )
        self.create_testcases = to_streamed_response_wrapper(
            testsets.create_testcases,
        )
        self.delete_testcases = to_streamed_response_wrapper(
            testsets.delete_testcases,
        )
        self.get = to_streamed_response_wrapper(
            testsets.get,
        )
        self.list_testcases = to_streamed_response_wrapper(
            testsets.list_testcases,
        )


class AsyncTestsetsResourceWithStreamingResponse:
    def __init__(self, testsets: AsyncTestsetsResource) -> None:
        self._testsets = testsets

        self.create = async_to_streamed_response_wrapper(
            testsets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            testsets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            testsets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            testsets.delete,
        )
        self.create_testcases = async_to_streamed_response_wrapper(
            testsets.create_testcases,
        )
        self.delete_testcases = async_to_streamed_response_wrapper(
            testsets.delete_testcases,
        )
        self.get = async_to_streamed_response_wrapper(
            testsets.get,
        )
        self.list_testcases = async_to_streamed_response_wrapper(
            testsets.list_testcases,
        )
