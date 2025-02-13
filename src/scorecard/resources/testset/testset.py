# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import testset_list_params, testset_create_params, testset_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .testcase import (
    TestcaseResource,
    AsyncTestcaseResource,
    TestcaseResourceWithRawResponse,
    AsyncTestcaseResourceWithRawResponse,
    TestcaseResourceWithStreamingResponse,
    AsyncTestcaseResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.testset.testset import Testset
from ...types.testset_list_response import TestsetListResponse
from ...types.testset_get_schema_response import TestsetGetSchemaResponse

__all__ = ["TestsetResource", "AsyncTestsetResource"]


class TestsetResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def testcase(self) -> TestcaseResource:
        return TestcaseResource(self._client)

    @cached_property
    def with_raw_response(self) -> TestsetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return TestsetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestsetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return TestsetResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        created_by_playground: Optional[bool] | NotGiven = NOT_GIVEN,
        custom_schema: Optional[testset_create_params.CustomSchema] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ingestion_method: Optional[Literal["csv", "logging"]] | NotGiven = NOT_GIVEN,
        project_id: Optional[int] | NotGiven = NOT_GIVEN,
        published: Optional[bool] | NotGiven = NOT_GIVEN,
        using_retrieval: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testset:
        """
        Create a new Testset

        Args:
          created_by_playground: Whether or not the testset was created by the playground.

          custom_schema: Custom schema model with an ordered list of custom variables.

          description: A description for the testset.

          ingestion_method: The method of ingestion for the testset.

          project_id: The ID of the project to create the testset in. Omitting this optional argument
              will create the testset inside your Organization's default project.

          published: Whether or not the testset is published.

          using_retrieval: Whether or not the testset uses retrieval.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/testset",
            body=maybe_transform(
                {
                    "name": name,
                    "created_by_playground": created_by_playground,
                    "custom_schema": custom_schema,
                    "description": description,
                    "ingestion_method": ingestion_method,
                    "project_id": project_id,
                    "published": published,
                    "using_retrieval": using_retrieval,
                },
                testset_create_params.TestsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testset,
        )

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
    ) -> Testset:
        """
        Retrieve Testset metadata without Testcase data

        Args:
          testset_id: The ID of the Testset to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/testset/{testset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testset,
        )

    def update(
        self,
        testset_id: int,
        *,
        custom_schema: Optional[testset_update_params.CustomSchema] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        using_retrieval: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testset:
        """
        Update a Testset.

        Args:
          testset_id: The ID of the Testset to update.

          custom_schema: Custom schema model with an ordered list of custom variables.

          description: A description for the testset.

          using_retrieval: Whether or not the testset uses retrieval.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/v1/testset/{testset_id}",
            body=maybe_transform(
                {
                    "custom_schema": custom_schema,
                    "description": description,
                    "name": name,
                    "using_retrieval": using_retrieval,
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
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestsetListResponse:
        """
        Retrieve all Testsets with cursor-based pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/testset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "size": size,
                    },
                    testset_list_params.TestsetListParams,
                ),
            ),
            cast_to=TestsetListResponse,
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
    ) -> Testset:
        """
        Delete a Testset

        Args:
          testset_id: The ID of the Testset to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/v1/testset/{testset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testset,
        )

    def get_schema(
        self,
        testset_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestsetGetSchemaResponse:
        """
        Read the schema of a Testset

        Args:
          testset_id: The ID of the Testset to retrieve the schema from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/testset/{testset_id}/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestsetGetSchemaResponse,
        )


class AsyncTestsetResource(AsyncAPIResource):
    @cached_property
    def testcase(self) -> AsyncTestcaseResource:
        return AsyncTestcaseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTestsetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestsetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestsetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return AsyncTestsetResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        created_by_playground: Optional[bool] | NotGiven = NOT_GIVEN,
        custom_schema: Optional[testset_create_params.CustomSchema] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ingestion_method: Optional[Literal["csv", "logging"]] | NotGiven = NOT_GIVEN,
        project_id: Optional[int] | NotGiven = NOT_GIVEN,
        published: Optional[bool] | NotGiven = NOT_GIVEN,
        using_retrieval: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testset:
        """
        Create a new Testset

        Args:
          created_by_playground: Whether or not the testset was created by the playground.

          custom_schema: Custom schema model with an ordered list of custom variables.

          description: A description for the testset.

          ingestion_method: The method of ingestion for the testset.

          project_id: The ID of the project to create the testset in. Omitting this optional argument
              will create the testset inside your Organization's default project.

          published: Whether or not the testset is published.

          using_retrieval: Whether or not the testset uses retrieval.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/testset",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "created_by_playground": created_by_playground,
                    "custom_schema": custom_schema,
                    "description": description,
                    "ingestion_method": ingestion_method,
                    "project_id": project_id,
                    "published": published,
                    "using_retrieval": using_retrieval,
                },
                testset_create_params.TestsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testset,
        )

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
    ) -> Testset:
        """
        Retrieve Testset metadata without Testcase data

        Args:
          testset_id: The ID of the Testset to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/testset/{testset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testset,
        )

    async def update(
        self,
        testset_id: int,
        *,
        custom_schema: Optional[testset_update_params.CustomSchema] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        using_retrieval: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testset:
        """
        Update a Testset.

        Args:
          testset_id: The ID of the Testset to update.

          custom_schema: Custom schema model with an ordered list of custom variables.

          description: A description for the testset.

          using_retrieval: Whether or not the testset uses retrieval.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/v1/testset/{testset_id}",
            body=await async_maybe_transform(
                {
                    "custom_schema": custom_schema,
                    "description": description,
                    "name": name,
                    "using_retrieval": using_retrieval,
                },
                testset_update_params.TestsetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testset,
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestsetListResponse:
        """
        Retrieve all Testsets with cursor-based pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/testset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "size": size,
                    },
                    testset_list_params.TestsetListParams,
                ),
            ),
            cast_to=TestsetListResponse,
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
    ) -> Testset:
        """
        Delete a Testset

        Args:
          testset_id: The ID of the Testset to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/v1/testset/{testset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testset,
        )

    async def get_schema(
        self,
        testset_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestsetGetSchemaResponse:
        """
        Read the schema of a Testset

        Args:
          testset_id: The ID of the Testset to retrieve the schema from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/testset/{testset_id}/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestsetGetSchemaResponse,
        )


class TestsetResourceWithRawResponse:
    __test__ = False

    def __init__(self, testset: TestsetResource) -> None:
        self._testset = testset

        self.create = to_raw_response_wrapper(
            testset.create,
        )
        self.retrieve = to_raw_response_wrapper(
            testset.retrieve,
        )
        self.update = to_raw_response_wrapper(
            testset.update,
        )
        self.list = to_raw_response_wrapper(
            testset.list,
        )
        self.delete = to_raw_response_wrapper(
            testset.delete,
        )
        self.get_schema = to_raw_response_wrapper(
            testset.get_schema,
        )

    @cached_property
    def testcase(self) -> TestcaseResourceWithRawResponse:
        return TestcaseResourceWithRawResponse(self._testset.testcase)


class AsyncTestsetResourceWithRawResponse:
    def __init__(self, testset: AsyncTestsetResource) -> None:
        self._testset = testset

        self.create = async_to_raw_response_wrapper(
            testset.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            testset.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            testset.update,
        )
        self.list = async_to_raw_response_wrapper(
            testset.list,
        )
        self.delete = async_to_raw_response_wrapper(
            testset.delete,
        )
        self.get_schema = async_to_raw_response_wrapper(
            testset.get_schema,
        )

    @cached_property
    def testcase(self) -> AsyncTestcaseResourceWithRawResponse:
        return AsyncTestcaseResourceWithRawResponse(self._testset.testcase)


class TestsetResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, testset: TestsetResource) -> None:
        self._testset = testset

        self.create = to_streamed_response_wrapper(
            testset.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            testset.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            testset.update,
        )
        self.list = to_streamed_response_wrapper(
            testset.list,
        )
        self.delete = to_streamed_response_wrapper(
            testset.delete,
        )
        self.get_schema = to_streamed_response_wrapper(
            testset.get_schema,
        )

    @cached_property
    def testcase(self) -> TestcaseResourceWithStreamingResponse:
        return TestcaseResourceWithStreamingResponse(self._testset.testcase)


class AsyncTestsetResourceWithStreamingResponse:
    def __init__(self, testset: AsyncTestsetResource) -> None:
        self._testset = testset

        self.create = async_to_streamed_response_wrapper(
            testset.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            testset.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            testset.update,
        )
        self.list = async_to_streamed_response_wrapper(
            testset.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            testset.delete,
        )
        self.get_schema = async_to_streamed_response_wrapper(
            testset.get_schema,
        )

    @cached_property
    def testcase(self) -> AsyncTestcaseResourceWithStreamingResponse:
        return AsyncTestcaseResourceWithStreamingResponse(self._testset.testcase)
