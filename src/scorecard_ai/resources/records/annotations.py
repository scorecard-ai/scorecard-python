# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.records.annotation_list_response import AnnotationListResponse

__all__ = ["AnnotationsResource", "AsyncAnnotationsResource"]


class AnnotationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnnotationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnnotationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AnnotationsResourceWithStreamingResponse(self)

    def list(
        self,
        record_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnnotationListResponse:
        """
        List all annotations (ratings and comments) for a specific Record.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return self._get(
            f"/records/{record_id}/annotations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationListResponse,
        )


class AsyncAnnotationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnnotationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnnotationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AsyncAnnotationsResourceWithStreamingResponse(self)

    async def list(
        self,
        record_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnnotationListResponse:
        """
        List all annotations (ratings and comments) for a specific Record.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return await self._get(
            f"/records/{record_id}/annotations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationListResponse,
        )


class AnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

        self.list = to_raw_response_wrapper(
            annotations.list,
        )


class AsyncAnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

        self.list = async_to_raw_response_wrapper(
            annotations.list,
        )


class AnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

        self.list = to_streamed_response_wrapper(
            annotations.list,
        )


class AsyncAnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

        self.list = async_to_streamed_response_wrapper(
            annotations.list,
        )
