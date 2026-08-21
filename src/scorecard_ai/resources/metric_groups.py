# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import metric_group_list_params, metric_group_create_params, metric_group_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPaginatedResponse, AsyncPaginatedResponse
from .._base_client import AsyncPaginator, make_request_options
from ..types.metric_group import MetricGroup
from ..types.metric_group_delete_response import MetricGroupDeleteResponse

__all__ = ["MetricGroupsResource", "AsyncMetricGroupsResource"]


class MetricGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return MetricGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return MetricGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        metric_ids: SequenceNotStr[str],
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGroup:
        """
        Create a new Metric Group referencing Metrics in the same Project.

        Args:
          metric_ids: The IDs of the Metrics to include in the group. Every Metric must belong to the
              same Project as the group.

          name: The name of the Metric Group.

          description: The description of the Metric Group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/projects/{project_id}/metric-groups", project_id=project_id),
            body=maybe_transform(
                {
                    "metric_ids": metric_ids,
                    "name": name,
                    "description": description,
                },
                metric_group_create_params.MetricGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricGroup,
        )

    def update(
        self,
        metric_group_id: str,
        *,
        description: str | Omit = omit,
        metric_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGroup:
        """Update a Metric Group's name, description, or member Metrics.

        The `metricIds`
        array replaces the group's current set of Metrics.

        Args:
          description: The new description of the Metric Group.

          metric_ids: The new set of Metric IDs for the group, replacing the current set. Every Metric
              must belong to the same Project as the group.

          name: The new name of the Metric Group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_group_id:
            raise ValueError(f"Expected a non-empty value for `metric_group_id` but received {metric_group_id!r}")
        return self._patch(
            path_template("/metric-groups/{metric_group_id}", metric_group_id=metric_group_id),
            body=maybe_transform(
                {
                    "description": description,
                    "metric_ids": metric_ids,
                    "name": name,
                },
                metric_group_update_params.MetricGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricGroup,
        )

    def list(
        self,
        project_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedResponse[MetricGroup]:
        """List Metric Groups configured for the specified Project.

        Metric Groups are
        returned in reverse chronological order.

        Args:
          cursor: Cursor for pagination. Pass the `nextCursor` from the previous response to get
              the next page of results.

          limit: Maximum number of items to return (1-100). Use with `cursor` for pagination
              through large sets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            path_template("/projects/{project_id}/metric-groups", project_id=project_id),
            page=SyncPaginatedResponse[MetricGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    metric_group_list_params.MetricGroupListParams,
                ),
            ),
            model=MetricGroup,
        )

    def delete(
        self,
        metric_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGroupDeleteResponse:
        """Delete a specific Metric Group by ID.

        The Metrics in the group are not deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_group_id:
            raise ValueError(f"Expected a non-empty value for `metric_group_id` but received {metric_group_id!r}")
        return self._delete(
            path_template("/metric-groups/{metric_group_id}", metric_group_id=metric_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricGroupDeleteResponse,
        )

    def get(
        self,
        metric_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGroup:
        """
        Retrieve a specific Metric Group by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_group_id:
            raise ValueError(f"Expected a non-empty value for `metric_group_id` but received {metric_group_id!r}")
        return self._get(
            path_template("/metric-groups/{metric_group_id}", metric_group_id=metric_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricGroup,
        )


class AsyncMetricGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AsyncMetricGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        metric_ids: SequenceNotStr[str],
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGroup:
        """
        Create a new Metric Group referencing Metrics in the same Project.

        Args:
          metric_ids: The IDs of the Metrics to include in the group. Every Metric must belong to the
              same Project as the group.

          name: The name of the Metric Group.

          description: The description of the Metric Group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/projects/{project_id}/metric-groups", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "metric_ids": metric_ids,
                    "name": name,
                    "description": description,
                },
                metric_group_create_params.MetricGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricGroup,
        )

    async def update(
        self,
        metric_group_id: str,
        *,
        description: str | Omit = omit,
        metric_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGroup:
        """Update a Metric Group's name, description, or member Metrics.

        The `metricIds`
        array replaces the group's current set of Metrics.

        Args:
          description: The new description of the Metric Group.

          metric_ids: The new set of Metric IDs for the group, replacing the current set. Every Metric
              must belong to the same Project as the group.

          name: The new name of the Metric Group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_group_id:
            raise ValueError(f"Expected a non-empty value for `metric_group_id` but received {metric_group_id!r}")
        return await self._patch(
            path_template("/metric-groups/{metric_group_id}", metric_group_id=metric_group_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metric_ids": metric_ids,
                    "name": name,
                },
                metric_group_update_params.MetricGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricGroup,
        )

    def list(
        self,
        project_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MetricGroup, AsyncPaginatedResponse[MetricGroup]]:
        """List Metric Groups configured for the specified Project.

        Metric Groups are
        returned in reverse chronological order.

        Args:
          cursor: Cursor for pagination. Pass the `nextCursor` from the previous response to get
              the next page of results.

          limit: Maximum number of items to return (1-100). Use with `cursor` for pagination
              through large sets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            path_template("/projects/{project_id}/metric-groups", project_id=project_id),
            page=AsyncPaginatedResponse[MetricGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    metric_group_list_params.MetricGroupListParams,
                ),
            ),
            model=MetricGroup,
        )

    async def delete(
        self,
        metric_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGroupDeleteResponse:
        """Delete a specific Metric Group by ID.

        The Metrics in the group are not deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_group_id:
            raise ValueError(f"Expected a non-empty value for `metric_group_id` but received {metric_group_id!r}")
        return await self._delete(
            path_template("/metric-groups/{metric_group_id}", metric_group_id=metric_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricGroupDeleteResponse,
        )

    async def get(
        self,
        metric_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGroup:
        """
        Retrieve a specific Metric Group by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_group_id:
            raise ValueError(f"Expected a non-empty value for `metric_group_id` but received {metric_group_id!r}")
        return await self._get(
            path_template("/metric-groups/{metric_group_id}", metric_group_id=metric_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricGroup,
        )


class MetricGroupsResourceWithRawResponse:
    def __init__(self, metric_groups: MetricGroupsResource) -> None:
        self._metric_groups = metric_groups

        self.create = to_raw_response_wrapper(
            metric_groups.create,
        )
        self.update = to_raw_response_wrapper(
            metric_groups.update,
        )
        self.list = to_raw_response_wrapper(
            metric_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            metric_groups.delete,
        )
        self.get = to_raw_response_wrapper(
            metric_groups.get,
        )


class AsyncMetricGroupsResourceWithRawResponse:
    def __init__(self, metric_groups: AsyncMetricGroupsResource) -> None:
        self._metric_groups = metric_groups

        self.create = async_to_raw_response_wrapper(
            metric_groups.create,
        )
        self.update = async_to_raw_response_wrapper(
            metric_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            metric_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            metric_groups.delete,
        )
        self.get = async_to_raw_response_wrapper(
            metric_groups.get,
        )


class MetricGroupsResourceWithStreamingResponse:
    def __init__(self, metric_groups: MetricGroupsResource) -> None:
        self._metric_groups = metric_groups

        self.create = to_streamed_response_wrapper(
            metric_groups.create,
        )
        self.update = to_streamed_response_wrapper(
            metric_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            metric_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            metric_groups.delete,
        )
        self.get = to_streamed_response_wrapper(
            metric_groups.get,
        )


class AsyncMetricGroupsResourceWithStreamingResponse:
    def __init__(self, metric_groups: AsyncMetricGroupsResource) -> None:
        self._metric_groups = metric_groups

        self.create = async_to_streamed_response_wrapper(
            metric_groups.create,
        )
        self.update = async_to_streamed_response_wrapper(
            metric_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            metric_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            metric_groups.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            metric_groups.get,
        )
