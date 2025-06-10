# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ...types import system_list_params, system_create_params, system_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPaginatedResponse, AsyncPaginatedResponse
from ..._base_client import AsyncPaginator, make_request_options
from ...types.system import System
from ...types.system_delete_response import SystemDeleteResponse

__all__ = ["SystemsResource", "AsyncSystemsResource"]


class SystemsResource(SyncAPIResource):
    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SystemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return SystemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SystemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return SystemsResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        config_schema: Dict[str, object],
        description: str,
        input_schema: Dict[str, object],
        name: str,
        output_schema: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> System:
        """
        Create a new system definition that specifies the interface contracts for a
        component you want to evaluate.

        A system acts as a template that defines three key contracts through JSON
        Schemas:

        1. Input Schema: What data your system accepts (e.g., user queries, context
           documents)
        2. Output Schema: What data your system produces (e.g., responses, confidence
           scores)
        3. Config Schema: What parameters can be adjusted (e.g., model selection,
           temperature)

        This separation lets you evaluate any system as a black box, focusing on its
        interface rather than implementation details.

        Args:
          config_schema: The schema of the system's configuration.

          description: The description of the system.

          input_schema: The schema of the system's inputs.

          name: The name of the system.

          output_schema: The schema of the system's outputs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/projects/{project_id}/systems",
            body=maybe_transform(
                {
                    "config_schema": config_schema,
                    "description": description,
                    "input_schema": input_schema,
                    "name": name,
                    "output_schema": output_schema,
                },
                system_create_params.SystemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=System,
        )

    def update(
        self,
        system_id: str,
        *,
        config_schema: Dict[str, object] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        input_schema: Dict[str, object] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output_schema: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> System:
        """Update an existing system definition.

        Only the fields provided in the request
        body will be updated. If a field is provided, the new content will replace the
        existing content. If a field is not provided, the existing content will remain
        unchanged.

        When updating schemas:

        - The system will accept your changes regardless of compatibility with existing
          configurations
        - Schema updates won't invalidate existing evaluations or configurations
        - For significant redesigns, creating a new system definition provides a cleaner
          separation

        Args:
          config_schema: The schema of the system's configuration.

          description: The description of the system.

          input_schema: The schema of the system's inputs.

          name: The name of the system.

          output_schema: The schema of the system's outputs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not system_id:
            raise ValueError(f"Expected a non-empty value for `system_id` but received {system_id!r}")
        return self._patch(
            f"/systems/{system_id}",
            body=maybe_transform(
                {
                    "config_schema": config_schema,
                    "description": description,
                    "input_schema": input_schema,
                    "name": name,
                    "output_schema": output_schema,
                },
                system_update_params.SystemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=System,
        )

    def list(
        self,
        project_id: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPaginatedResponse[System]:
        """Retrieve a paginated list of all systems.

        Systems are ordered by creation date.

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
            f"/projects/{project_id}/systems",
            page=SyncPaginatedResponse[System],
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
                    system_list_params.SystemListParams,
                ),
            ),
            model=System,
        )

    def delete(
        self,
        system_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SystemDeleteResponse:
        """Delete a system definition by ID.

        This will not delete associated system
        versions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not system_id:
            raise ValueError(f"Expected a non-empty value for `system_id` but received {system_id!r}")
        return self._delete(
            f"/systems/{system_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SystemDeleteResponse,
        )

    def get(
        self,
        system_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> System:
        """
        Retrieve a specific system by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not system_id:
            raise ValueError(f"Expected a non-empty value for `system_id` but received {system_id!r}")
        return self._get(
            f"/systems/{system_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=System,
        )


class AsyncSystemsResource(AsyncAPIResource):
    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSystemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSystemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSystemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AsyncSystemsResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        config_schema: Dict[str, object],
        description: str,
        input_schema: Dict[str, object],
        name: str,
        output_schema: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> System:
        """
        Create a new system definition that specifies the interface contracts for a
        component you want to evaluate.

        A system acts as a template that defines three key contracts through JSON
        Schemas:

        1. Input Schema: What data your system accepts (e.g., user queries, context
           documents)
        2. Output Schema: What data your system produces (e.g., responses, confidence
           scores)
        3. Config Schema: What parameters can be adjusted (e.g., model selection,
           temperature)

        This separation lets you evaluate any system as a black box, focusing on its
        interface rather than implementation details.

        Args:
          config_schema: The schema of the system's configuration.

          description: The description of the system.

          input_schema: The schema of the system's inputs.

          name: The name of the system.

          output_schema: The schema of the system's outputs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/projects/{project_id}/systems",
            body=await async_maybe_transform(
                {
                    "config_schema": config_schema,
                    "description": description,
                    "input_schema": input_schema,
                    "name": name,
                    "output_schema": output_schema,
                },
                system_create_params.SystemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=System,
        )

    async def update(
        self,
        system_id: str,
        *,
        config_schema: Dict[str, object] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        input_schema: Dict[str, object] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output_schema: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> System:
        """Update an existing system definition.

        Only the fields provided in the request
        body will be updated. If a field is provided, the new content will replace the
        existing content. If a field is not provided, the existing content will remain
        unchanged.

        When updating schemas:

        - The system will accept your changes regardless of compatibility with existing
          configurations
        - Schema updates won't invalidate existing evaluations or configurations
        - For significant redesigns, creating a new system definition provides a cleaner
          separation

        Args:
          config_schema: The schema of the system's configuration.

          description: The description of the system.

          input_schema: The schema of the system's inputs.

          name: The name of the system.

          output_schema: The schema of the system's outputs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not system_id:
            raise ValueError(f"Expected a non-empty value for `system_id` but received {system_id!r}")
        return await self._patch(
            f"/systems/{system_id}",
            body=await async_maybe_transform(
                {
                    "config_schema": config_schema,
                    "description": description,
                    "input_schema": input_schema,
                    "name": name,
                    "output_schema": output_schema,
                },
                system_update_params.SystemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=System,
        )

    def list(
        self,
        project_id: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[System, AsyncPaginatedResponse[System]]:
        """Retrieve a paginated list of all systems.

        Systems are ordered by creation date.

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
            f"/projects/{project_id}/systems",
            page=AsyncPaginatedResponse[System],
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
                    system_list_params.SystemListParams,
                ),
            ),
            model=System,
        )

    async def delete(
        self,
        system_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SystemDeleteResponse:
        """Delete a system definition by ID.

        This will not delete associated system
        versions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not system_id:
            raise ValueError(f"Expected a non-empty value for `system_id` but received {system_id!r}")
        return await self._delete(
            f"/systems/{system_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SystemDeleteResponse,
        )

    async def get(
        self,
        system_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> System:
        """
        Retrieve a specific system by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not system_id:
            raise ValueError(f"Expected a non-empty value for `system_id` but received {system_id!r}")
        return await self._get(
            f"/systems/{system_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=System,
        )


class SystemsResourceWithRawResponse:
    def __init__(self, systems: SystemsResource) -> None:
        self._systems = systems

        self.create = to_raw_response_wrapper(
            systems.create,
        )
        self.update = to_raw_response_wrapper(
            systems.update,
        )
        self.list = to_raw_response_wrapper(
            systems.list,
        )
        self.delete = to_raw_response_wrapper(
            systems.delete,
        )
        self.get = to_raw_response_wrapper(
            systems.get,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._systems.versions)


class AsyncSystemsResourceWithRawResponse:
    def __init__(self, systems: AsyncSystemsResource) -> None:
        self._systems = systems

        self.create = async_to_raw_response_wrapper(
            systems.create,
        )
        self.update = async_to_raw_response_wrapper(
            systems.update,
        )
        self.list = async_to_raw_response_wrapper(
            systems.list,
        )
        self.delete = async_to_raw_response_wrapper(
            systems.delete,
        )
        self.get = async_to_raw_response_wrapper(
            systems.get,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._systems.versions)


class SystemsResourceWithStreamingResponse:
    def __init__(self, systems: SystemsResource) -> None:
        self._systems = systems

        self.create = to_streamed_response_wrapper(
            systems.create,
        )
        self.update = to_streamed_response_wrapper(
            systems.update,
        )
        self.list = to_streamed_response_wrapper(
            systems.list,
        )
        self.delete = to_streamed_response_wrapper(
            systems.delete,
        )
        self.get = to_streamed_response_wrapper(
            systems.get,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._systems.versions)


class AsyncSystemsResourceWithStreamingResponse:
    def __init__(self, systems: AsyncSystemsResource) -> None:
        self._systems = systems

        self.create = async_to_streamed_response_wrapper(
            systems.create,
        )
        self.update = async_to_streamed_response_wrapper(
            systems.update,
        )
        self.list = async_to_streamed_response_wrapper(
            systems.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            systems.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            systems.get,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._systems.versions)
