# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.records import assignee_create_params
from ...types.records.record_assignment import RecordAssignment
from ...types.records.assignee_list_response import AssigneeListResponse
from ...types.records.assignee_delete_response import AssigneeDeleteResponse

__all__ = ["AssigneesResource", "AsyncAssigneesResource"]


class AssigneesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssigneesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AssigneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssigneesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AssigneesResourceWithStreamingResponse(self)

    def create(
        self,
        record_id: str,
        *,
        assignee_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordAssignment:
        """Assign an organization member to a Record.

        Idempotent: re-assigning an existing
        member returns the existing assignment.

        Args:
          assignee_user_id: The ID of the organization member to assign. Idempotent: re-assigning an
              existing member returns the existing assignment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return self._post(
            path_template("/records/{record_id}/assignees", record_id=record_id),
            body=maybe_transform({"assignee_user_id": assignee_user_id}, assignee_create_params.AssigneeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordAssignment,
        )

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
    ) -> AssigneeListResponse:
        """
        List the organization members assigned to a Record.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return self._get(
            path_template("/records/{record_id}/assignees", record_id=record_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssigneeListResponse,
        )

    def delete(
        self,
        assignee_user_id: str,
        *,
        record_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssigneeDeleteResponse:
        """
        Remove an assignee from a Record.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        if not assignee_user_id:
            raise ValueError(f"Expected a non-empty value for `assignee_user_id` but received {assignee_user_id!r}")
        return self._delete(
            path_template(
                "/records/{record_id}/assignees/{assignee_user_id}",
                record_id=record_id,
                assignee_user_id=assignee_user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssigneeDeleteResponse,
        )


class AsyncAssigneesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssigneesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssigneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssigneesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AsyncAssigneesResourceWithStreamingResponse(self)

    async def create(
        self,
        record_id: str,
        *,
        assignee_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordAssignment:
        """Assign an organization member to a Record.

        Idempotent: re-assigning an existing
        member returns the existing assignment.

        Args:
          assignee_user_id: The ID of the organization member to assign. Idempotent: re-assigning an
              existing member returns the existing assignment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return await self._post(
            path_template("/records/{record_id}/assignees", record_id=record_id),
            body=await async_maybe_transform(
                {"assignee_user_id": assignee_user_id}, assignee_create_params.AssigneeCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordAssignment,
        )

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
    ) -> AssigneeListResponse:
        """
        List the organization members assigned to a Record.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return await self._get(
            path_template("/records/{record_id}/assignees", record_id=record_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssigneeListResponse,
        )

    async def delete(
        self,
        assignee_user_id: str,
        *,
        record_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssigneeDeleteResponse:
        """
        Remove an assignee from a Record.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        if not assignee_user_id:
            raise ValueError(f"Expected a non-empty value for `assignee_user_id` but received {assignee_user_id!r}")
        return await self._delete(
            path_template(
                "/records/{record_id}/assignees/{assignee_user_id}",
                record_id=record_id,
                assignee_user_id=assignee_user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssigneeDeleteResponse,
        )


class AssigneesResourceWithRawResponse:
    def __init__(self, assignees: AssigneesResource) -> None:
        self._assignees = assignees

        self.create = to_raw_response_wrapper(
            assignees.create,
        )
        self.list = to_raw_response_wrapper(
            assignees.list,
        )
        self.delete = to_raw_response_wrapper(
            assignees.delete,
        )


class AsyncAssigneesResourceWithRawResponse:
    def __init__(self, assignees: AsyncAssigneesResource) -> None:
        self._assignees = assignees

        self.create = async_to_raw_response_wrapper(
            assignees.create,
        )
        self.list = async_to_raw_response_wrapper(
            assignees.list,
        )
        self.delete = async_to_raw_response_wrapper(
            assignees.delete,
        )


class AssigneesResourceWithStreamingResponse:
    def __init__(self, assignees: AssigneesResource) -> None:
        self._assignees = assignees

        self.create = to_streamed_response_wrapper(
            assignees.create,
        )
        self.list = to_streamed_response_wrapper(
            assignees.list,
        )
        self.delete = to_streamed_response_wrapper(
            assignees.delete,
        )


class AsyncAssigneesResourceWithStreamingResponse:
    def __init__(self, assignees: AsyncAssigneesResource) -> None:
        self._assignees = assignees

        self.create = async_to_streamed_response_wrapper(
            assignees.create,
        )
        self.list = async_to_streamed_response_wrapper(
            assignees.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            assignees.delete,
        )
