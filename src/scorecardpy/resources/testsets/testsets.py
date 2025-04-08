# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import testset_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .testcases import (
    TestcasesResource,
    AsyncTestcasesResource,
    TestcasesResourceWithRawResponse,
    AsyncTestcasesResourceWithRawResponse,
    TestcasesResourceWithStreamingResponse,
    AsyncTestcasesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.testset_delete_response import TestsetDeleteResponse
from ...types.testset_update_response import TestsetUpdateResponse
from ...types.testset_retrieve_response import TestsetRetrieveResponse

__all__ = ["TestsetsResource", "AsyncTestsetsResource"]


class TestsetsResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def testcases(self) -> TestcasesResource:
        return TestcasesResource(self._client)

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

    def retrieve(
        self,
        testset_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestsetRetrieveResponse:
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
            cast_to=TestsetRetrieveResponse,
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
    ) -> TestsetUpdateResponse:
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
            cast_to=TestsetUpdateResponse,
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


class AsyncTestsetsResource(AsyncAPIResource):
    @cached_property
    def testcases(self) -> AsyncTestcasesResource:
        return AsyncTestcasesResource(self._client)

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

    async def retrieve(
        self,
        testset_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestsetRetrieveResponse:
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
            cast_to=TestsetRetrieveResponse,
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
    ) -> TestsetUpdateResponse:
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
            cast_to=TestsetUpdateResponse,
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


class TestsetsResourceWithRawResponse:
    __test__ = False

    def __init__(self, testsets: TestsetsResource) -> None:
        self._testsets = testsets

        self.retrieve = to_raw_response_wrapper(
            testsets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            testsets.update,
        )
        self.delete = to_raw_response_wrapper(
            testsets.delete,
        )

    @cached_property
    def testcases(self) -> TestcasesResourceWithRawResponse:
        return TestcasesResourceWithRawResponse(self._testsets.testcases)


class AsyncTestsetsResourceWithRawResponse:
    def __init__(self, testsets: AsyncTestsetsResource) -> None:
        self._testsets = testsets

        self.retrieve = async_to_raw_response_wrapper(
            testsets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            testsets.update,
        )
        self.delete = async_to_raw_response_wrapper(
            testsets.delete,
        )

    @cached_property
    def testcases(self) -> AsyncTestcasesResourceWithRawResponse:
        return AsyncTestcasesResourceWithRawResponse(self._testsets.testcases)


class TestsetsResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, testsets: TestsetsResource) -> None:
        self._testsets = testsets

        self.retrieve = to_streamed_response_wrapper(
            testsets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            testsets.update,
        )
        self.delete = to_streamed_response_wrapper(
            testsets.delete,
        )

    @cached_property
    def testcases(self) -> TestcasesResourceWithStreamingResponse:
        return TestcasesResourceWithStreamingResponse(self._testsets.testcases)


class AsyncTestsetsResourceWithStreamingResponse:
    def __init__(self, testsets: AsyncTestsetsResource) -> None:
        self._testsets = testsets

        self.retrieve = async_to_streamed_response_wrapper(
            testsets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            testsets.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            testsets.delete,
        )

    @cached_property
    def testcases(self) -> AsyncTestcasesResourceWithStreamingResponse:
        return AsyncTestcasesResourceWithStreamingResponse(self._testsets.testcases)
