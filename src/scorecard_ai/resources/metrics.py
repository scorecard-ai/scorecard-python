# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..types import metric_create_params, metric_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.metric import Metric

__all__ = ["MetricsResource", "AsyncMetricsResource"]


class MetricsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return MetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return MetricsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["ai"],
        name: str,
        output_type: Literal["int"],
        prompt_template: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_model_name: str | NotGiven = NOT_GIVEN,
        guidelines: Optional[str] | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Create a new Metric for evaluating system outputs.

        The structure of a metric
        depends on the evalType and outputType of the metric.

        Args:
          eval_type: AI-based evaluation type.

          name: The name of the Metric.

          output_type: Integer output type.

          prompt_template: The complete prompt template for AI evaluation. Should include placeholders for
              dynamic content.

          description: The description of the Metric.

          eval_model_name: The AI model to use for evaluation.

          guidelines: Guidelines for AI evaluation on how to score the metric.

          passing_threshold: The threshold for determining pass/fail from integer scores (1-5).

          temperature: The temperature for AI evaluation (0-2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["human"],
        name: str,
        output_type: Literal["int"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Create a new Metric for evaluating system outputs.

        The structure of a metric
        depends on the evalType and outputType of the metric.

        Args:
          eval_type: Human-based evaluation type.

          name: The name of the Metric.

          output_type: Integer output type.

          description: The description of the Metric.

          guidelines: Guidelines for human evaluators.

          passing_threshold: The threshold for determining pass/fail from integer scores (1-5).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["heuristic"],
        name: str,
        output_type: Literal["int"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Create a new Metric for evaluating system outputs.

        The structure of a metric
        depends on the evalType and outputType of the metric.

        Args:
          eval_type: Heuristic-based evaluation type.

          name: The name of the Metric.

          output_type: Integer output type.

          description: The description of the Metric.

          guidelines: Optional guidelines for heuristic evaluation logic.

          passing_threshold: The threshold for determining pass/fail from integer scores (1-5).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["ai"],
        name: str,
        output_type: Literal["boolean"],
        prompt_template: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_model_name: str | NotGiven = NOT_GIVEN,
        guidelines: Optional[str] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Create a new Metric for evaluating system outputs.

        The structure of a metric
        depends on the evalType and outputType of the metric.

        Args:
          eval_type: AI-based evaluation type.

          name: The name of the Metric.

          output_type: Boolean output type.

          prompt_template: The complete prompt template for AI evaluation. Should include placeholders for
              dynamic content.

          description: The description of the Metric.

          eval_model_name: The AI model to use for evaluation.

          guidelines: Guidelines for AI evaluation on how to score the metric.

          temperature: The temperature for AI evaluation (0-2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["human"],
        name: str,
        output_type: Literal["boolean"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Create a new Metric for evaluating system outputs.

        The structure of a metric
        depends on the evalType and outputType of the metric.

        Args:
          eval_type: Human-based evaluation type.

          name: The name of the Metric.

          output_type: Boolean output type.

          description: The description of the Metric.

          guidelines: Guidelines for human evaluators.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["heuristic"],
        name: str,
        output_type: Literal["boolean"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Create a new Metric for evaluating system outputs.

        The structure of a metric
        depends on the evalType and outputType of the metric.

        Args:
          eval_type: Heuristic-based evaluation type.

          name: The name of the Metric.

          output_type: Boolean output type.

          description: The description of the Metric.

          guidelines: Optional guidelines for heuristic evaluation logic.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["eval_type", "name", "output_type", "prompt_template"], ["eval_type", "name", "output_type"])
    def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["ai"] | Literal["human"] | Literal["heuristic"],
        name: str,
        output_type: Literal["int"] | Literal["boolean"],
        prompt_template: str | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_model_name: str | NotGiven = NOT_GIVEN,
        guidelines: Optional[str] | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return cast(
            Metric,
            self._post(
                f"/projects/{project_id}/metrics",
                body=maybe_transform(
                    {
                        "eval_type": eval_type,
                        "name": name,
                        "output_type": output_type,
                        "prompt_template": prompt_template,
                        "description": description,
                        "eval_model_name": eval_model_name,
                        "guidelines": guidelines,
                        "passing_threshold": passing_threshold,
                        "temperature": temperature,
                    },
                    metric_create_params.MetricCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Metric),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["ai"],
        output_type: Literal["int"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_model_name: str | NotGiven = NOT_GIVEN,
        guidelines: Optional[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        prompt_template: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Update an existing Metric.

        You must specify the evalType and outputType of the
        metric. The structure of a metric depends on the evalType and outputType of the
        metric.

        Args:
          eval_type: AI-based evaluation type.

          output_type: Integer output type.

          description: The description of the Metric.

          eval_model_name: The AI model to use for evaluation.

          guidelines: Guidelines for AI evaluation on how to score the metric.

          name: The name of the Metric.

          passing_threshold: The threshold for determining pass/fail from integer scores (1-5).

          prompt_template: The complete prompt template for AI evaluation. Should include placeholders for
              dynamic content.

          temperature: The temperature for AI evaluation (0-2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["human"],
        output_type: Literal["int"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Update an existing Metric.

        You must specify the evalType and outputType of the
        metric. The structure of a metric depends on the evalType and outputType of the
        metric.

        Args:
          eval_type: Human-based evaluation type.

          output_type: Integer output type.

          description: The description of the Metric.

          guidelines: Guidelines for human evaluators.

          name: The name of the Metric.

          passing_threshold: The threshold for determining pass/fail from integer scores (1-5).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["heuristic"],
        output_type: Literal["int"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Update an existing Metric.

        You must specify the evalType and outputType of the
        metric. The structure of a metric depends on the evalType and outputType of the
        metric.

        Args:
          eval_type: Heuristic-based evaluation type.

          output_type: Integer output type.

          description: The description of the Metric.

          guidelines: Optional guidelines for heuristic evaluation logic.

          name: The name of the Metric.

          passing_threshold: The threshold for determining pass/fail from integer scores (1-5).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["ai"],
        output_type: Literal["boolean"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_model_name: str | NotGiven = NOT_GIVEN,
        guidelines: Optional[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        prompt_template: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Update an existing Metric.

        You must specify the evalType and outputType of the
        metric. The structure of a metric depends on the evalType and outputType of the
        metric.

        Args:
          eval_type: AI-based evaluation type.

          output_type: Boolean output type.

          description: The description of the Metric.

          eval_model_name: The AI model to use for evaluation.

          guidelines: Guidelines for AI evaluation on how to score the metric.

          name: The name of the Metric.

          prompt_template: The complete prompt template for AI evaluation. Should include placeholders for
              dynamic content.

          temperature: The temperature for AI evaluation (0-2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["human"],
        output_type: Literal["boolean"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Update an existing Metric.

        You must specify the evalType and outputType of the
        metric. The structure of a metric depends on the evalType and outputType of the
        metric.

        Args:
          eval_type: Human-based evaluation type.

          output_type: Boolean output type.

          description: The description of the Metric.

          guidelines: Guidelines for human evaluators.

          name: The name of the Metric.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["heuristic"],
        output_type: Literal["boolean"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Update an existing Metric.

        You must specify the evalType and outputType of the
        metric. The structure of a metric depends on the evalType and outputType of the
        metric.

        Args:
          eval_type: Heuristic-based evaluation type.

          output_type: Boolean output type.

          description: The description of the Metric.

          guidelines: Optional guidelines for heuristic evaluation logic.

          name: The name of the Metric.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["eval_type", "output_type"])
    def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["ai"] | Literal["human"] | Literal["heuristic"],
        output_type: Literal["int"] | Literal["boolean"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_model_name: str | NotGiven = NOT_GIVEN,
        guidelines: Optional[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        prompt_template: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        if not metric_id:
            raise ValueError(f"Expected a non-empty value for `metric_id` but received {metric_id!r}")
        return cast(
            Metric,
            self._patch(
                f"/metrics/{metric_id}",
                body=maybe_transform(
                    {
                        "eval_type": eval_type,
                        "output_type": output_type,
                        "description": description,
                        "eval_model_name": eval_model_name,
                        "guidelines": guidelines,
                        "name": name,
                        "passing_threshold": passing_threshold,
                        "prompt_template": prompt_template,
                        "temperature": temperature,
                    },
                    metric_update_params.MetricUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Metric),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncMetricsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AsyncMetricsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["ai"],
        name: str,
        output_type: Literal["int"],
        prompt_template: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_model_name: str | NotGiven = NOT_GIVEN,
        guidelines: Optional[str] | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Create a new Metric for evaluating system outputs.

        The structure of a metric
        depends on the evalType and outputType of the metric.

        Args:
          eval_type: AI-based evaluation type.

          name: The name of the Metric.

          output_type: Integer output type.

          prompt_template: The complete prompt template for AI evaluation. Should include placeholders for
              dynamic content.

          description: The description of the Metric.

          eval_model_name: The AI model to use for evaluation.

          guidelines: Guidelines for AI evaluation on how to score the metric.

          passing_threshold: The threshold for determining pass/fail from integer scores (1-5).

          temperature: The temperature for AI evaluation (0-2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["human"],
        name: str,
        output_type: Literal["int"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Create a new Metric for evaluating system outputs.

        The structure of a metric
        depends on the evalType and outputType of the metric.

        Args:
          eval_type: Human-based evaluation type.

          name: The name of the Metric.

          output_type: Integer output type.

          description: The description of the Metric.

          guidelines: Guidelines for human evaluators.

          passing_threshold: The threshold for determining pass/fail from integer scores (1-5).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["heuristic"],
        name: str,
        output_type: Literal["int"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Create a new Metric for evaluating system outputs.

        The structure of a metric
        depends on the evalType and outputType of the metric.

        Args:
          eval_type: Heuristic-based evaluation type.

          name: The name of the Metric.

          output_type: Integer output type.

          description: The description of the Metric.

          guidelines: Optional guidelines for heuristic evaluation logic.

          passing_threshold: The threshold for determining pass/fail from integer scores (1-5).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["ai"],
        name: str,
        output_type: Literal["boolean"],
        prompt_template: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_model_name: str | NotGiven = NOT_GIVEN,
        guidelines: Optional[str] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Create a new Metric for evaluating system outputs.

        The structure of a metric
        depends on the evalType and outputType of the metric.

        Args:
          eval_type: AI-based evaluation type.

          name: The name of the Metric.

          output_type: Boolean output type.

          prompt_template: The complete prompt template for AI evaluation. Should include placeholders for
              dynamic content.

          description: The description of the Metric.

          eval_model_name: The AI model to use for evaluation.

          guidelines: Guidelines for AI evaluation on how to score the metric.

          temperature: The temperature for AI evaluation (0-2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["human"],
        name: str,
        output_type: Literal["boolean"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Create a new Metric for evaluating system outputs.

        The structure of a metric
        depends on the evalType and outputType of the metric.

        Args:
          eval_type: Human-based evaluation type.

          name: The name of the Metric.

          output_type: Boolean output type.

          description: The description of the Metric.

          guidelines: Guidelines for human evaluators.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["heuristic"],
        name: str,
        output_type: Literal["boolean"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Create a new Metric for evaluating system outputs.

        The structure of a metric
        depends on the evalType and outputType of the metric.

        Args:
          eval_type: Heuristic-based evaluation type.

          name: The name of the Metric.

          output_type: Boolean output type.

          description: The description of the Metric.

          guidelines: Optional guidelines for heuristic evaluation logic.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["eval_type", "name", "output_type", "prompt_template"], ["eval_type", "name", "output_type"])
    async def create(
        self,
        project_id: str,
        *,
        eval_type: Literal["ai"] | Literal["human"] | Literal["heuristic"],
        name: str,
        output_type: Literal["int"] | Literal["boolean"],
        prompt_template: str | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_model_name: str | NotGiven = NOT_GIVEN,
        guidelines: Optional[str] | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return cast(
            Metric,
            await self._post(
                f"/projects/{project_id}/metrics",
                body=await async_maybe_transform(
                    {
                        "eval_type": eval_type,
                        "name": name,
                        "output_type": output_type,
                        "prompt_template": prompt_template,
                        "description": description,
                        "eval_model_name": eval_model_name,
                        "guidelines": guidelines,
                        "passing_threshold": passing_threshold,
                        "temperature": temperature,
                    },
                    metric_create_params.MetricCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Metric),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["ai"],
        output_type: Literal["int"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_model_name: str | NotGiven = NOT_GIVEN,
        guidelines: Optional[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        prompt_template: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Update an existing Metric.

        You must specify the evalType and outputType of the
        metric. The structure of a metric depends on the evalType and outputType of the
        metric.

        Args:
          eval_type: AI-based evaluation type.

          output_type: Integer output type.

          description: The description of the Metric.

          eval_model_name: The AI model to use for evaluation.

          guidelines: Guidelines for AI evaluation on how to score the metric.

          name: The name of the Metric.

          passing_threshold: The threshold for determining pass/fail from integer scores (1-5).

          prompt_template: The complete prompt template for AI evaluation. Should include placeholders for
              dynamic content.

          temperature: The temperature for AI evaluation (0-2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["human"],
        output_type: Literal["int"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Update an existing Metric.

        You must specify the evalType and outputType of the
        metric. The structure of a metric depends on the evalType and outputType of the
        metric.

        Args:
          eval_type: Human-based evaluation type.

          output_type: Integer output type.

          description: The description of the Metric.

          guidelines: Guidelines for human evaluators.

          name: The name of the Metric.

          passing_threshold: The threshold for determining pass/fail from integer scores (1-5).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["heuristic"],
        output_type: Literal["int"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Update an existing Metric.

        You must specify the evalType and outputType of the
        metric. The structure of a metric depends on the evalType and outputType of the
        metric.

        Args:
          eval_type: Heuristic-based evaluation type.

          output_type: Integer output type.

          description: The description of the Metric.

          guidelines: Optional guidelines for heuristic evaluation logic.

          name: The name of the Metric.

          passing_threshold: The threshold for determining pass/fail from integer scores (1-5).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["ai"],
        output_type: Literal["boolean"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_model_name: str | NotGiven = NOT_GIVEN,
        guidelines: Optional[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        prompt_template: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Update an existing Metric.

        You must specify the evalType and outputType of the
        metric. The structure of a metric depends on the evalType and outputType of the
        metric.

        Args:
          eval_type: AI-based evaluation type.

          output_type: Boolean output type.

          description: The description of the Metric.

          eval_model_name: The AI model to use for evaluation.

          guidelines: Guidelines for AI evaluation on how to score the metric.

          name: The name of the Metric.

          prompt_template: The complete prompt template for AI evaluation. Should include placeholders for
              dynamic content.

          temperature: The temperature for AI evaluation (0-2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["human"],
        output_type: Literal["boolean"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Update an existing Metric.

        You must specify the evalType and outputType of the
        metric. The structure of a metric depends on the evalType and outputType of the
        metric.

        Args:
          eval_type: Human-based evaluation type.

          output_type: Boolean output type.

          description: The description of the Metric.

          guidelines: Guidelines for human evaluators.

          name: The name of the Metric.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["heuristic"],
        output_type: Literal["boolean"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        guidelines: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        """Update an existing Metric.

        You must specify the evalType and outputType of the
        metric. The structure of a metric depends on the evalType and outputType of the
        metric.

        Args:
          eval_type: Heuristic-based evaluation type.

          output_type: Boolean output type.

          description: The description of the Metric.

          guidelines: Optional guidelines for heuristic evaluation logic.

          name: The name of the Metric.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["eval_type", "output_type"])
    async def update(
        self,
        metric_id: str,
        *,
        eval_type: Literal["ai"] | Literal["human"] | Literal["heuristic"],
        output_type: Literal["int"] | Literal["boolean"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_model_name: str | NotGiven = NOT_GIVEN,
        guidelines: Optional[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        passing_threshold: int | NotGiven = NOT_GIVEN,
        prompt_template: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metric:
        if not metric_id:
            raise ValueError(f"Expected a non-empty value for `metric_id` but received {metric_id!r}")
        return cast(
            Metric,
            await self._patch(
                f"/metrics/{metric_id}",
                body=await async_maybe_transform(
                    {
                        "eval_type": eval_type,
                        "output_type": output_type,
                        "description": description,
                        "eval_model_name": eval_model_name,
                        "guidelines": guidelines,
                        "name": name,
                        "passing_threshold": passing_threshold,
                        "prompt_template": prompt_template,
                        "temperature": temperature,
                    },
                    metric_update_params.MetricUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Metric),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class MetricsResourceWithRawResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.create = to_raw_response_wrapper(
            metrics.create,
        )
        self.update = to_raw_response_wrapper(
            metrics.update,
        )


class AsyncMetricsResourceWithRawResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.create = async_to_raw_response_wrapper(
            metrics.create,
        )
        self.update = async_to_raw_response_wrapper(
            metrics.update,
        )


class MetricsResourceWithStreamingResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.create = to_streamed_response_wrapper(
            metrics.create,
        )
        self.update = to_streamed_response_wrapper(
            metrics.update,
        )


class AsyncMetricsResourceWithStreamingResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.create = async_to_streamed_response_wrapper(
            metrics.create,
        )
        self.update = async_to_streamed_response_wrapper(
            metrics.update,
        )
