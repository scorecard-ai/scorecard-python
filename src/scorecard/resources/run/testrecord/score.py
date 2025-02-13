# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.run.testrecord import score_create_params, score_update_params
from ....types.run.testrecord.grade import Grade

__all__ = ["ScoreResource", "AsyncScoreResource"]


class ScoreResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return ScoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return ScoreResourceWithStreamingResponse(self)

    def create(
        self,
        testrecord_id: int,
        *,
        run_id: int,
        binary_score: Optional[bool],
        int_score: Optional[int],
        metric_id: int,
        reasoning: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Grade:
        """
        Create a score

        Args:
          run_id: The ID of the run that created the testrecord to be scored.

          testrecord_id: The ID of the testrecord to be scored.

          binary_score: Specify boolean scores.

          int_score: Specify integer scores.

          metric_id: The ID of the metric

          reasoning: The reasoning for the assigned score.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/v1/run/{run_id}/testrecord/{testrecord_id}/score",
            body=maybe_transform(
                {
                    "binary_score": binary_score,
                    "int_score": int_score,
                    "metric_id": metric_id,
                    "reasoning": reasoning,
                },
                score_create_params.ScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Grade,
        )

    def update(
        self,
        score_id: int,
        *,
        run_id: int,
        testrecord_id: int,
        binary_score: Optional[bool],
        int_score: Optional[int],
        reasoning: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Grade:
        """
        Update a score

        Args:
          run_id: The run ID that created the test record to be scored.

          testrecord_id: The ID of the testrecord whose score will be updated.

          score_id: The ID of the score to be updated.

          binary_score: The new boolean score to assign.

          int_score: The new integer score to assign.

          reasoning: The reasoning for the score update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/v1/run/{run_id}/testrecord/{testrecord_id}/score/{score_id}",
            body=maybe_transform(
                {
                    "binary_score": binary_score,
                    "int_score": int_score,
                    "reasoning": reasoning,
                },
                score_update_params.ScoreUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Grade,
        )


class AsyncScoreResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return AsyncScoreResourceWithStreamingResponse(self)

    async def create(
        self,
        testrecord_id: int,
        *,
        run_id: int,
        binary_score: Optional[bool],
        int_score: Optional[int],
        metric_id: int,
        reasoning: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Grade:
        """
        Create a score

        Args:
          run_id: The ID of the run that created the testrecord to be scored.

          testrecord_id: The ID of the testrecord to be scored.

          binary_score: Specify boolean scores.

          int_score: Specify integer scores.

          metric_id: The ID of the metric

          reasoning: The reasoning for the assigned score.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/v1/run/{run_id}/testrecord/{testrecord_id}/score",
            body=await async_maybe_transform(
                {
                    "binary_score": binary_score,
                    "int_score": int_score,
                    "metric_id": metric_id,
                    "reasoning": reasoning,
                },
                score_create_params.ScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Grade,
        )

    async def update(
        self,
        score_id: int,
        *,
        run_id: int,
        testrecord_id: int,
        binary_score: Optional[bool],
        int_score: Optional[int],
        reasoning: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Grade:
        """
        Update a score

        Args:
          run_id: The run ID that created the test record to be scored.

          testrecord_id: The ID of the testrecord whose score will be updated.

          score_id: The ID of the score to be updated.

          binary_score: The new boolean score to assign.

          int_score: The new integer score to assign.

          reasoning: The reasoning for the score update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/v1/run/{run_id}/testrecord/{testrecord_id}/score/{score_id}",
            body=await async_maybe_transform(
                {
                    "binary_score": binary_score,
                    "int_score": int_score,
                    "reasoning": reasoning,
                },
                score_update_params.ScoreUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Grade,
        )


class ScoreResourceWithRawResponse:
    def __init__(self, score: ScoreResource) -> None:
        self._score = score

        self.create = to_raw_response_wrapper(
            score.create,
        )
        self.update = to_raw_response_wrapper(
            score.update,
        )


class AsyncScoreResourceWithRawResponse:
    def __init__(self, score: AsyncScoreResource) -> None:
        self._score = score

        self.create = async_to_raw_response_wrapper(
            score.create,
        )
        self.update = async_to_raw_response_wrapper(
            score.update,
        )


class ScoreResourceWithStreamingResponse:
    def __init__(self, score: ScoreResource) -> None:
        self._score = score

        self.create = to_streamed_response_wrapper(
            score.create,
        )
        self.update = to_streamed_response_wrapper(
            score.update,
        )


class AsyncScoreResourceWithStreamingResponse:
    def __init__(self, score: AsyncScoreResource) -> None:
        self._score = score

        self.create = async_to_streamed_response_wrapper(
            score.create,
        )
        self.update = async_to_streamed_response_wrapper(
            score.update,
        )
