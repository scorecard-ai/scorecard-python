# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

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
from ..._base_client import make_request_options
from ...types.testset import (
    testcase_list_params,
    testcase_create_params,
    testcase_update_params,
    testcase_batch_copy_params,
    testcase_batch_delete_params,
)
from ...types.testset.test_case import TestCase
from ...types.testset.testcase_list_response import TestcaseListResponse
from ...types.testset.testcase_delete_response import TestcaseDeleteResponse
from ...types.testset.testcase_batch_copy_response import TestcaseBatchCopyResponse
from ...types.testset.testcase_batch_delete_response import TestcaseBatchDeleteResponse

__all__ = ["TestcaseResource", "AsyncTestcaseResource"]


class TestcaseResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def with_raw_response(self) -> TestcaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return TestcaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestcaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return TestcaseResourceWithStreamingResponse(self)

    def create(
        self,
        testset_id: int,
        *,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        custom_inputs: Optional[Dict[str, Optional[testcase_create_params.CustomInputs]]] | NotGiven = NOT_GIVEN,
        custom_labels: Optional[Dict[str, Optional[testcase_create_params.CustomLabels]]] | NotGiven = NOT_GIVEN,
        ideal: Optional[str] | NotGiven = NOT_GIVEN,
        user_query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestCase:
        """
        Create a new Testcase

        Args:
          testset_id: The ID of the Testset to create the Testcase in.

          context: The context to be used while generating the testcase.

          ideal: The ideal response to the user query.

          user_query: The user query to be executed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/v1/testset/{testset_id}/testcase",
            body=maybe_transform(
                {
                    "context": context,
                    "custom_inputs": custom_inputs,
                    "custom_labels": custom_labels,
                    "ideal": ideal,
                    "user_query": user_query,
                },
                testcase_create_params.TestcaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCase,
        )

    def retrieve(
        self,
        testcase_id: int,
        *,
        testset_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestCase:
        """
        Retrieve Testcase data

        Args:
          testset_id: The ID of the Testset to retrieve the Testcase from.

          testcase_id: The ID of the Testcase to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/testset/{testset_id}/testcase/{testcase_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCase,
        )

    def update(
        self,
        testcase_id: int,
        *,
        testset_id: int,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        custom_inputs: Optional[Dict[str, Optional[testcase_update_params.CustomInputs]]] | NotGiven = NOT_GIVEN,
        custom_labels: Optional[Dict[str, Optional[testcase_update_params.CustomLabels]]] | NotGiven = NOT_GIVEN,
        ideal: Optional[str] | NotGiven = NOT_GIVEN,
        user_query: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestCase:
        """
        Update a Testcase.

        Args:
          testset_id: The ID of the Testset to retrieve the Testcase from.

          testcase_id: The ID of the Testcase to update.

          context: The context to be used while generating the testcase.

          ideal: The ideal response to the user query.

          user_query: The user query to be executed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/v1/testset/{testset_id}/testcase/{testcase_id}",
            body=maybe_transform(
                {
                    "context": context,
                    "custom_inputs": custom_inputs,
                    "custom_labels": custom_labels,
                    "ideal": ideal,
                    "user_query": user_query,
                },
                testcase_update_params.TestcaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCase,
        )

    def list(
        self,
        testset_id: int,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseListResponse:
        """
        Retrieve all Testcases from a Testset

        Args:
          testset_id: The Testset ID to retrieve testcases from.

          limit: The number of testcases to return.

          offset: The offset to start from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/testset/{testset_id}/testcase",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    testcase_list_params.TestcaseListParams,
                ),
            ),
            cast_to=TestcaseListResponse,
        )

    def delete(
        self,
        testcase_id: int,
        *,
        testset_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseDeleteResponse:
        """
        Delete a Testcase

        Args:
          testset_id: The ID of the Testset to delete the Testcase from.

          testcase_id: The ID of the Testcase to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/v1/testset/{testset_id}/testcase/{testcase_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseDeleteResponse,
        )

    def batch_copy(
        self,
        testset_id: int,
        *,
        ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseBatchCopyResponse:
        """
        Batch copy Testcases

        Args:
          testset_id: The ID of the Testset to create the Testcase in.

          ids: List of Testcase IDs to copy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/v1/testset/{testset_id}/testcase/batch_copy",
            body=maybe_transform({"ids": ids}, testcase_batch_copy_params.TestcaseBatchCopyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseBatchCopyResponse,
        )

    def batch_delete(
        self,
        testset_id: int,
        *,
        ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseBatchDeleteResponse:
        """
        Batch delete Testcases

        Args:
          testset_id: The ID of the Testset from which the Testcases will be deleted.

          ids: List of Testcase IDs to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/v1/testset/{testset_id}/testcase/batch_delete",
            body=maybe_transform({"ids": ids}, testcase_batch_delete_params.TestcaseBatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseBatchDeleteResponse,
        )


class AsyncTestcaseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTestcaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestcaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestcaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return AsyncTestcaseResourceWithStreamingResponse(self)

    async def create(
        self,
        testset_id: int,
        *,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        custom_inputs: Optional[Dict[str, Optional[testcase_create_params.CustomInputs]]] | NotGiven = NOT_GIVEN,
        custom_labels: Optional[Dict[str, Optional[testcase_create_params.CustomLabels]]] | NotGiven = NOT_GIVEN,
        ideal: Optional[str] | NotGiven = NOT_GIVEN,
        user_query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestCase:
        """
        Create a new Testcase

        Args:
          testset_id: The ID of the Testset to create the Testcase in.

          context: The context to be used while generating the testcase.

          ideal: The ideal response to the user query.

          user_query: The user query to be executed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/v1/testset/{testset_id}/testcase",
            body=await async_maybe_transform(
                {
                    "context": context,
                    "custom_inputs": custom_inputs,
                    "custom_labels": custom_labels,
                    "ideal": ideal,
                    "user_query": user_query,
                },
                testcase_create_params.TestcaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCase,
        )

    async def retrieve(
        self,
        testcase_id: int,
        *,
        testset_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestCase:
        """
        Retrieve Testcase data

        Args:
          testset_id: The ID of the Testset to retrieve the Testcase from.

          testcase_id: The ID of the Testcase to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/testset/{testset_id}/testcase/{testcase_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCase,
        )

    async def update(
        self,
        testcase_id: int,
        *,
        testset_id: int,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        custom_inputs: Optional[Dict[str, Optional[testcase_update_params.CustomInputs]]] | NotGiven = NOT_GIVEN,
        custom_labels: Optional[Dict[str, Optional[testcase_update_params.CustomLabels]]] | NotGiven = NOT_GIVEN,
        ideal: Optional[str] | NotGiven = NOT_GIVEN,
        user_query: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestCase:
        """
        Update a Testcase.

        Args:
          testset_id: The ID of the Testset to retrieve the Testcase from.

          testcase_id: The ID of the Testcase to update.

          context: The context to be used while generating the testcase.

          ideal: The ideal response to the user query.

          user_query: The user query to be executed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/v1/testset/{testset_id}/testcase/{testcase_id}",
            body=await async_maybe_transform(
                {
                    "context": context,
                    "custom_inputs": custom_inputs,
                    "custom_labels": custom_labels,
                    "ideal": ideal,
                    "user_query": user_query,
                },
                testcase_update_params.TestcaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCase,
        )

    async def list(
        self,
        testset_id: int,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseListResponse:
        """
        Retrieve all Testcases from a Testset

        Args:
          testset_id: The Testset ID to retrieve testcases from.

          limit: The number of testcases to return.

          offset: The offset to start from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/testset/{testset_id}/testcase",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    testcase_list_params.TestcaseListParams,
                ),
            ),
            cast_to=TestcaseListResponse,
        )

    async def delete(
        self,
        testcase_id: int,
        *,
        testset_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseDeleteResponse:
        """
        Delete a Testcase

        Args:
          testset_id: The ID of the Testset to delete the Testcase from.

          testcase_id: The ID of the Testcase to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/v1/testset/{testset_id}/testcase/{testcase_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseDeleteResponse,
        )

    async def batch_copy(
        self,
        testset_id: int,
        *,
        ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseBatchCopyResponse:
        """
        Batch copy Testcases

        Args:
          testset_id: The ID of the Testset to create the Testcase in.

          ids: List of Testcase IDs to copy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/v1/testset/{testset_id}/testcase/batch_copy",
            body=await async_maybe_transform({"ids": ids}, testcase_batch_copy_params.TestcaseBatchCopyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseBatchCopyResponse,
        )

    async def batch_delete(
        self,
        testset_id: int,
        *,
        ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestcaseBatchDeleteResponse:
        """
        Batch delete Testcases

        Args:
          testset_id: The ID of the Testset from which the Testcases will be deleted.

          ids: List of Testcase IDs to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/v1/testset/{testset_id}/testcase/batch_delete",
            body=await async_maybe_transform({"ids": ids}, testcase_batch_delete_params.TestcaseBatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestcaseBatchDeleteResponse,
        )


class TestcaseResourceWithRawResponse:
    __test__ = False

    def __init__(self, testcase: TestcaseResource) -> None:
        self._testcase = testcase

        self.create = to_raw_response_wrapper(
            testcase.create,
        )
        self.retrieve = to_raw_response_wrapper(
            testcase.retrieve,
        )
        self.update = to_raw_response_wrapper(
            testcase.update,
        )
        self.list = to_raw_response_wrapper(
            testcase.list,
        )
        self.delete = to_raw_response_wrapper(
            testcase.delete,
        )
        self.batch_copy = to_raw_response_wrapper(
            testcase.batch_copy,
        )
        self.batch_delete = to_raw_response_wrapper(
            testcase.batch_delete,
        )


class AsyncTestcaseResourceWithRawResponse:
    def __init__(self, testcase: AsyncTestcaseResource) -> None:
        self._testcase = testcase

        self.create = async_to_raw_response_wrapper(
            testcase.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            testcase.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            testcase.update,
        )
        self.list = async_to_raw_response_wrapper(
            testcase.list,
        )
        self.delete = async_to_raw_response_wrapper(
            testcase.delete,
        )
        self.batch_copy = async_to_raw_response_wrapper(
            testcase.batch_copy,
        )
        self.batch_delete = async_to_raw_response_wrapper(
            testcase.batch_delete,
        )


class TestcaseResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, testcase: TestcaseResource) -> None:
        self._testcase = testcase

        self.create = to_streamed_response_wrapper(
            testcase.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            testcase.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            testcase.update,
        )
        self.list = to_streamed_response_wrapper(
            testcase.list,
        )
        self.delete = to_streamed_response_wrapper(
            testcase.delete,
        )
        self.batch_copy = to_streamed_response_wrapper(
            testcase.batch_copy,
        )
        self.batch_delete = to_streamed_response_wrapper(
            testcase.batch_delete,
        )


class AsyncTestcaseResourceWithStreamingResponse:
    def __init__(self, testcase: AsyncTestcaseResource) -> None:
        self._testcase = testcase

        self.create = async_to_streamed_response_wrapper(
            testcase.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            testcase.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            testcase.update,
        )
        self.list = async_to_streamed_response_wrapper(
            testcase.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            testcase.delete,
        )
        self.batch_copy = async_to_streamed_response_wrapper(
            testcase.batch_copy,
        )
        self.batch_delete = async_to_streamed_response_wrapper(
            testcase.batch_delete,
        )
