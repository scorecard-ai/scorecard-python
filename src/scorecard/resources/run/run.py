# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ...types import run_create_params, run_update_status_params
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
from ...types.run.run import Run
from .testrecord.testrecord import (
    TestrecordResource,
    AsyncTestrecordResource,
    TestrecordResourceWithRawResponse,
    AsyncTestrecordResourceWithRawResponse,
    TestrecordResourceWithStreamingResponse,
    AsyncTestrecordResourceWithStreamingResponse,
)

__all__ = ["RunResource", "AsyncRunResource"]


class RunResource(SyncAPIResource):
    @cached_property
    def testrecord(self) -> TestrecordResource:
        return TestrecordResource(self._client)

    @cached_property
    def with_raw_response(self) -> RunResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return RunResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return RunResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        metrics: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        model_params: Optional[object] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_id: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_template: Optional[str] | NotGiven = NOT_GIVEN,
        scoring_config_id: Optional[int] | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        testset_id: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Run:
        """Create a new Run

        Args:
          model_params: Optional.

        The model parameters to use for this run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/run",
            body=maybe_transform(
                {
                    "metrics": metrics,
                    "model_params": model_params,
                    "notes": notes,
                    "prompt_id": prompt_id,
                    "prompt_template": prompt_template,
                    "scoring_config_id": scoring_config_id,
                    "source": source,
                    "status": status,
                    "testset_id": testset_id,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )

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
    ) -> Run:
        """
        Retrieve a Run metadata

        Args:
          run_id: The id of the run to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/run/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )

    def update_status(
        self,
        run_id: int,
        *,
        status: Literal[
            "pending",
            "awaiting_execution",
            "running_execution",
            "awaiting_scoring",
            "running_scoring",
            "awaiting_human_scoring",
            "completed",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Run:
        """
        Update the status of a run.

        Args:
          run_id: The id of the run to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/v1/run/{run_id}/status",
            body=maybe_transform({"status": status}, run_update_status_params.RunUpdateStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )


class AsyncRunResource(AsyncAPIResource):
    @cached_property
    def testrecord(self) -> AsyncTestrecordResource:
        return AsyncTestrecordResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRunResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return AsyncRunResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        metrics: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        model_params: Optional[object] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_id: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_template: Optional[str] | NotGiven = NOT_GIVEN,
        scoring_config_id: Optional[int] | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        testset_id: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Run:
        """Create a new Run

        Args:
          model_params: Optional.

        The model parameters to use for this run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/run",
            body=await async_maybe_transform(
                {
                    "metrics": metrics,
                    "model_params": model_params,
                    "notes": notes,
                    "prompt_id": prompt_id,
                    "prompt_template": prompt_template,
                    "scoring_config_id": scoring_config_id,
                    "source": source,
                    "status": status,
                    "testset_id": testset_id,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )

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
    ) -> Run:
        """
        Retrieve a Run metadata

        Args:
          run_id: The id of the run to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/run/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )

    async def update_status(
        self,
        run_id: int,
        *,
        status: Literal[
            "pending",
            "awaiting_execution",
            "running_execution",
            "awaiting_scoring",
            "running_scoring",
            "awaiting_human_scoring",
            "completed",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Run:
        """
        Update the status of a run.

        Args:
          run_id: The id of the run to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/v1/run/{run_id}/status",
            body=await async_maybe_transform({"status": status}, run_update_status_params.RunUpdateStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )


class RunResourceWithRawResponse:
    def __init__(self, run: RunResource) -> None:
        self._run = run

        self.create = to_raw_response_wrapper(
            run.create,
        )
        self.retrieve = to_raw_response_wrapper(
            run.retrieve,
        )
        self.update_status = to_raw_response_wrapper(
            run.update_status,
        )

    @cached_property
    def testrecord(self) -> TestrecordResourceWithRawResponse:
        return TestrecordResourceWithRawResponse(self._run.testrecord)


class AsyncRunResourceWithRawResponse:
    def __init__(self, run: AsyncRunResource) -> None:
        self._run = run

        self.create = async_to_raw_response_wrapper(
            run.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            run.retrieve,
        )
        self.update_status = async_to_raw_response_wrapper(
            run.update_status,
        )

    @cached_property
    def testrecord(self) -> AsyncTestrecordResourceWithRawResponse:
        return AsyncTestrecordResourceWithRawResponse(self._run.testrecord)


class RunResourceWithStreamingResponse:
    def __init__(self, run: RunResource) -> None:
        self._run = run

        self.create = to_streamed_response_wrapper(
            run.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            run.retrieve,
        )
        self.update_status = to_streamed_response_wrapper(
            run.update_status,
        )

    @cached_property
    def testrecord(self) -> TestrecordResourceWithStreamingResponse:
        return TestrecordResourceWithStreamingResponse(self._run.testrecord)


class AsyncRunResourceWithStreamingResponse:
    def __init__(self, run: AsyncRunResource) -> None:
        self._run = run

        self.create = async_to_streamed_response_wrapper(
            run.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            run.retrieve,
        )
        self.update_status = async_to_streamed_response_wrapper(
            run.update_status,
        )

    @cached_property
    def testrecord(self) -> AsyncTestrecordResourceWithStreamingResponse:
        return AsyncTestrecordResourceWithStreamingResponse(self._run.testrecord)
