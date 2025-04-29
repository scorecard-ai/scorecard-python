# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..types import system_config_list_params, system_config_create_params
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
from ..pagination import SyncPaginatedResponse, AsyncPaginatedResponse
from .._base_client import AsyncPaginator, make_request_options
from ..types.system_config import SystemConfig

__all__ = ["SystemConfigsResource", "AsyncSystemConfigsResource"]


class SystemConfigsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SystemConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return SystemConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SystemConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return SystemConfigsResourceWithStreamingResponse(self)

    def create(
        self,
        system_id: str,
        *,
        config: Dict[str, object],
        name: str,
        validation_errors: Iterable[system_config_create_params.ValidationError] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SystemConfig:
        """
        Create a new configuration for a system.

        Each configuration contains specific parameter values that match the system's
        configSchema - things like model parameters, thresholds, or processing options.
        Once created, configurations cannot be modified, ensuring stable reference
        points for evaluations.

        When creating a configuration:

        - The 'config' object is validated against the parent system's configSchema
        - Configurations with validation errors are still stored, with errors included
          in the response
        - Validation errors indicate fields that don't match the schema but don't
          prevent creation
        - Having validation errors may affect how some evaluation metrics are calculated

        Args:
          config: The configuration of the system.

          name: The name of the system configuration.

          validation_errors: Validation errors found in the configuration. If present, the configuration
              doesn't fully conform to its system's configSchema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not system_id:
            raise ValueError(f"Expected a non-empty value for `system_id` but received {system_id!r}")
        return self._post(
            f"/systems/{system_id}/configs",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "validation_errors": validation_errors,
                },
                system_config_create_params.SystemConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SystemConfig,
        )

    def list(
        self,
        system_id: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPaginatedResponse[SystemConfig]:
        """
        Retrieve a paginated list of configurations for a specific system.

        System configurations provide concrete parameter values for a System Under Test,
        defining exactly how the system should be configured during an evaluation run.

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
        if not system_id:
            raise ValueError(f"Expected a non-empty value for `system_id` but received {system_id!r}")
        return self._get_api_list(
            f"/systems/{system_id}/configs",
            page=SyncPaginatedResponse[SystemConfig],
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
                    system_config_list_params.SystemConfigListParams,
                ),
            ),
            model=SystemConfig,
        )

    def get(
        self,
        system_config_id: str,
        *,
        system_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SystemConfig:
        """
        Retrieve a specific system configuration by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not system_id:
            raise ValueError(f"Expected a non-empty value for `system_id` but received {system_id!r}")
        if not system_config_id:
            raise ValueError(f"Expected a non-empty value for `system_config_id` but received {system_config_id!r}")
        return self._get(
            f"/systems/{system_id}/configs/{system_config_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SystemConfig,
        )


class AsyncSystemConfigsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSystemConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSystemConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSystemConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AsyncSystemConfigsResourceWithStreamingResponse(self)

    async def create(
        self,
        system_id: str,
        *,
        config: Dict[str, object],
        name: str,
        validation_errors: Iterable[system_config_create_params.ValidationError] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SystemConfig:
        """
        Create a new configuration for a system.

        Each configuration contains specific parameter values that match the system's
        configSchema - things like model parameters, thresholds, or processing options.
        Once created, configurations cannot be modified, ensuring stable reference
        points for evaluations.

        When creating a configuration:

        - The 'config' object is validated against the parent system's configSchema
        - Configurations with validation errors are still stored, with errors included
          in the response
        - Validation errors indicate fields that don't match the schema but don't
          prevent creation
        - Having validation errors may affect how some evaluation metrics are calculated

        Args:
          config: The configuration of the system.

          name: The name of the system configuration.

          validation_errors: Validation errors found in the configuration. If present, the configuration
              doesn't fully conform to its system's configSchema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not system_id:
            raise ValueError(f"Expected a non-empty value for `system_id` but received {system_id!r}")
        return await self._post(
            f"/systems/{system_id}/configs",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "validation_errors": validation_errors,
                },
                system_config_create_params.SystemConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SystemConfig,
        )

    def list(
        self,
        system_id: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SystemConfig, AsyncPaginatedResponse[SystemConfig]]:
        """
        Retrieve a paginated list of configurations for a specific system.

        System configurations provide concrete parameter values for a System Under Test,
        defining exactly how the system should be configured during an evaluation run.

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
        if not system_id:
            raise ValueError(f"Expected a non-empty value for `system_id` but received {system_id!r}")
        return self._get_api_list(
            f"/systems/{system_id}/configs",
            page=AsyncPaginatedResponse[SystemConfig],
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
                    system_config_list_params.SystemConfigListParams,
                ),
            ),
            model=SystemConfig,
        )

    async def get(
        self,
        system_config_id: str,
        *,
        system_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SystemConfig:
        """
        Retrieve a specific system configuration by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not system_id:
            raise ValueError(f"Expected a non-empty value for `system_id` but received {system_id!r}")
        if not system_config_id:
            raise ValueError(f"Expected a non-empty value for `system_config_id` but received {system_config_id!r}")
        return await self._get(
            f"/systems/{system_id}/configs/{system_config_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SystemConfig,
        )


class SystemConfigsResourceWithRawResponse:
    def __init__(self, system_configs: SystemConfigsResource) -> None:
        self._system_configs = system_configs

        self.create = to_raw_response_wrapper(
            system_configs.create,
        )
        self.list = to_raw_response_wrapper(
            system_configs.list,
        )
        self.get = to_raw_response_wrapper(
            system_configs.get,
        )


class AsyncSystemConfigsResourceWithRawResponse:
    def __init__(self, system_configs: AsyncSystemConfigsResource) -> None:
        self._system_configs = system_configs

        self.create = async_to_raw_response_wrapper(
            system_configs.create,
        )
        self.list = async_to_raw_response_wrapper(
            system_configs.list,
        )
        self.get = async_to_raw_response_wrapper(
            system_configs.get,
        )


class SystemConfigsResourceWithStreamingResponse:
    def __init__(self, system_configs: SystemConfigsResource) -> None:
        self._system_configs = system_configs

        self.create = to_streamed_response_wrapper(
            system_configs.create,
        )
        self.list = to_streamed_response_wrapper(
            system_configs.list,
        )
        self.get = to_streamed_response_wrapper(
            system_configs.get,
        )


class AsyncSystemConfigsResourceWithStreamingResponse:
    def __init__(self, system_configs: AsyncSystemConfigsResource) -> None:
        self._system_configs = system_configs

        self.create = async_to_streamed_response_wrapper(
            system_configs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            system_configs.list,
        )
        self.get = async_to_streamed_response_wrapper(
            system_configs.get,
        )
