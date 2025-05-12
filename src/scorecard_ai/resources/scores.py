# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import score_upsert_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.score import Score
from .._base_client import make_request_options

__all__ = ["ScoresResource", "AsyncScoresResource"]


class ScoresResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return ScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return ScoresResourceWithStreamingResponse(self)

    def upsert(
        self,
        metric_config_id: str,
        *,
        record_id: str,
        score: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Score:
        """Create or update a Score for a given Record and MetricConfig.

        If a Score with
        the specified Record ID and MetricConfig ID already exists, it will be updated.
        Otherwise, a new Score will be created. The score provided should conform to the
        schema defined by the MetricConfig; otherwise, validation errors will be
        reported.

        Args:
          score: The score of the Record, as arbitrary JSON. This data should ideally conform to
              the output schema defined by the associated MetricConfig. If it doesn't,
              validation errors will be captured in the `validationErrors` field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        if not metric_config_id:
            raise ValueError(f"Expected a non-empty value for `metric_config_id` but received {metric_config_id!r}")
        return self._put(
            f"/records/{record_id}/scores/{metric_config_id}",
            body=maybe_transform({"score": score}, score_upsert_params.ScoreUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Score,
        )


class AsyncScoresResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AsyncScoresResourceWithStreamingResponse(self)

    async def upsert(
        self,
        metric_config_id: str,
        *,
        record_id: str,
        score: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Score:
        """Create or update a Score for a given Record and MetricConfig.

        If a Score with
        the specified Record ID and MetricConfig ID already exists, it will be updated.
        Otherwise, a new Score will be created. The score provided should conform to the
        schema defined by the MetricConfig; otherwise, validation errors will be
        reported.

        Args:
          score: The score of the Record, as arbitrary JSON. This data should ideally conform to
              the output schema defined by the associated MetricConfig. If it doesn't,
              validation errors will be captured in the `validationErrors` field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        if not metric_config_id:
            raise ValueError(f"Expected a non-empty value for `metric_config_id` but received {metric_config_id!r}")
        return await self._put(
            f"/records/{record_id}/scores/{metric_config_id}",
            body=await async_maybe_transform({"score": score}, score_upsert_params.ScoreUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Score,
        )


class ScoresResourceWithRawResponse:
    def __init__(self, scores: ScoresResource) -> None:
        self._scores = scores

        self.upsert = to_raw_response_wrapper(
            scores.upsert,
        )


class AsyncScoresResourceWithRawResponse:
    def __init__(self, scores: AsyncScoresResource) -> None:
        self._scores = scores

        self.upsert = async_to_raw_response_wrapper(
            scores.upsert,
        )


class ScoresResourceWithStreamingResponse:
    def __init__(self, scores: ScoresResource) -> None:
        self._scores = scores

        self.upsert = to_streamed_response_wrapper(
            scores.upsert,
        )


class AsyncScoresResourceWithStreamingResponse:
    def __init__(self, scores: AsyncScoresResource) -> None:
        self._scores = scores

        self.upsert = async_to_streamed_response_wrapper(
            scores.upsert,
        )
