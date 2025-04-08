# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import testcase_update_params
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
from .._base_client import make_request_options
from ..types.shared.testcase import Testcase

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

    def update(
        self,
        testcase_id: int,
        *,
        data: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testcase:
        """
        Replace the data of an existing testcase while keeping its ID.

        Args:
          data: The JSON data of the testcase, which is validated against the testset's schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/testcases/{testcase_id}",
            body=maybe_transform({"data": data}, testcase_update_params.TestcaseUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testcase,
        )

    def get(
        self,
        testcase_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testcase:
        """
        Retrieve a specific testcase by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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

    async def update(
        self,
        testcase_id: int,
        *,
        data: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testcase:
        """
        Replace the data of an existing testcase while keeping its ID.

        Args:
          data: The JSON data of the testcase, which is validated against the testset's schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/testcases/{testcase_id}",
            body=await async_maybe_transform({"data": data}, testcase_update_params.TestcaseUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Testcase,
        )

    async def get(
        self,
        testcase_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Testcase:
        """
        Retrieve a specific testcase by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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

        self.update = to_raw_response_wrapper(
            testcases.update,
        )
        self.get = to_raw_response_wrapper(
            testcases.get,
        )


class AsyncTestcasesResourceWithRawResponse:
    def __init__(self, testcases: AsyncTestcasesResource) -> None:
        self._testcases = testcases

        self.update = async_to_raw_response_wrapper(
            testcases.update,
        )
        self.get = async_to_raw_response_wrapper(
            testcases.get,
        )


class TestcasesResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, testcases: TestcasesResource) -> None:
        self._testcases = testcases

        self.update = to_streamed_response_wrapper(
            testcases.update,
        )
        self.get = to_streamed_response_wrapper(
            testcases.get,
        )


class AsyncTestcasesResourceWithStreamingResponse:
    def __init__(self, testcases: AsyncTestcasesResource) -> None:
        self._testcases = testcases

        self.update = async_to_streamed_response_wrapper(
            testcases.update,
        )
        self.get = async_to_streamed_response_wrapper(
            testcases.get,
        )
