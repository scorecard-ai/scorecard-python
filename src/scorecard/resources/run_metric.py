# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.run_metric_retrieve_response import RunMetricRetrieveResponse

__all__ = ["RunMetricResource", "AsyncRunMetricResource"]


class RunMetricResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunMetricResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return RunMetricResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunMetricResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return RunMetricResourceWithStreamingResponse(self)

    def retrieve(
        self,
        run_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunMetricRetrieveResponse:
        """
        Retrieve metrics associated with a run

        Args:
          run_id: The id of the run to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/run_metric/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunMetricRetrieveResponse,
        )


class AsyncRunMetricResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunMetricResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunMetricResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunMetricResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return AsyncRunMetricResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        run_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunMetricRetrieveResponse:
        """
        Retrieve metrics associated with a run

        Args:
          run_id: The id of the run to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/run_metric/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunMetricRetrieveResponse,
        )


class RunMetricResourceWithRawResponse:
    def __init__(self, run_metric: RunMetricResource) -> None:
        self._run_metric = run_metric

        self.retrieve = to_raw_response_wrapper(
            run_metric.retrieve,
        )


class AsyncRunMetricResourceWithRawResponse:
    def __init__(self, run_metric: AsyncRunMetricResource) -> None:
        self._run_metric = run_metric

        self.retrieve = async_to_raw_response_wrapper(
            run_metric.retrieve,
        )


class RunMetricResourceWithStreamingResponse:
    def __init__(self, run_metric: RunMetricResource) -> None:
        self._run_metric = run_metric

        self.retrieve = to_streamed_response_wrapper(
            run_metric.retrieve,
        )


class AsyncRunMetricResourceWithStreamingResponse:
    def __init__(self, run_metric: AsyncRunMetricResource) -> None:
        self._run_metric = run_metric

        self.retrieve = async_to_streamed_response_wrapper(
            run_metric.retrieve,
        )
