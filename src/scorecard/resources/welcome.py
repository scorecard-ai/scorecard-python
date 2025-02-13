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

__all__ = ["WelcomeResource", "AsyncWelcomeResource"]


class WelcomeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WelcomeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return WelcomeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WelcomeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return WelcomeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Root endpoint that returns a welcome message."""
        return self._get(
            "/v1/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncWelcomeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWelcomeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWelcomeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWelcomeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return AsyncWelcomeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Root endpoint that returns a welcome message."""
        return await self._get(
            "/v1/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class WelcomeResourceWithRawResponse:
    def __init__(self, welcome: WelcomeResource) -> None:
        self._welcome = welcome

        self.retrieve = to_raw_response_wrapper(
            welcome.retrieve,
        )


class AsyncWelcomeResourceWithRawResponse:
    def __init__(self, welcome: AsyncWelcomeResource) -> None:
        self._welcome = welcome

        self.retrieve = async_to_raw_response_wrapper(
            welcome.retrieve,
        )


class WelcomeResourceWithStreamingResponse:
    def __init__(self, welcome: WelcomeResource) -> None:
        self._welcome = welcome

        self.retrieve = to_streamed_response_wrapper(
            welcome.retrieve,
        )


class AsyncWelcomeResourceWithStreamingResponse:
    def __init__(self, welcome: AsyncWelcomeResource) -> None:
        self._welcome = welcome

        self.retrieve = async_to_streamed_response_wrapper(
            welcome.retrieve,
        )
