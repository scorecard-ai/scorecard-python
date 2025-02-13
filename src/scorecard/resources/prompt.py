# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional

import httpx

from ..types import (
    prompt_list_params,
    prompt_create_params,
    prompt_update_params,
    prompt_retrieve_by_name_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.prompt import Prompt
from ..types.prompt_list_response import PromptListResponse

__all__ = ["PromptResource", "AsyncPromptResource"]


class PromptResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return PromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return PromptResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        prompt_template: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        is_prod: Optional[bool] | NotGiven = NOT_GIVEN,
        model_params: Optional[Dict[str, Union[float, str, bool]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        parent_id: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: Optional[int] | NotGiven = NOT_GIVEN,
        tag: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """
        Two types of prompts can be created - a root prompt or a child prompt (aka
        Prompt Version in the app).

                A root prompt can be created by providing the `name` param, and it will always be tagged as production.

                A child prompt can be created by providing the `parent_id` param. Note that the `name` param in this case will be ignored as all descendants from a root prompt would share the root's name. `is_prod` can also be provided to configure whether a child should be tagged as production.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/prompt",
            body=maybe_transform(
                {
                    "prompt_template": prompt_template,
                    "description": description,
                    "is_prod": is_prod,
                    "model_params": model_params,
                    "name": name,
                    "parent_id": parent_id,
                    "project_id": project_id,
                    "tag": tag,
                },
                prompt_create_params.PromptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )

    def update(
        self,
        id: str,
        *,
        is_prod: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """
        Update a prompt.

                `is_prod` tags the provided prompt as the production prompt within the prompt graph.

        Args:
          id: The id of the prompt to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v1/prompt/{id}",
            body=maybe_transform({"is_prod": is_prod}, prompt_update_params.PromptUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: Optional[int] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptListResponse:
        """
        List all prompts with cursor-based pagination

        Args:
          cursor: Cursor for the next page

          project_id: ID of Project to filter by.

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/prompt/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "project_id": project_id,
                        "size": size,
                    },
                    prompt_list_params.PromptListParams,
                ),
            ),
            cast_to=PromptListResponse,
        )

    def delete_root(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a root prompt and all of its children.

        Args:
          id: The id of the root prompt to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v1/prompt/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """
        Retrieve a prompt by id

        Args:
          id: The id of the prompt to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/prompt/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )

    def retrieve_by_name(
        self,
        *,
        name: str,
        tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """
        Retrieve a prompt by name, defaulting to the production prompt, unless a tag to
        select the prompt by is specified

        Args:
          name: Name of the prompt.

          tag: Tag to select by. Defaults to selecting the production version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/prompt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "tag": tag,
                    },
                    prompt_retrieve_by_name_params.PromptRetrieveByNameParams,
                ),
            ),
            cast_to=Prompt,
        )


class AsyncPromptResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scorecard-python#with_streaming_response
        """
        return AsyncPromptResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        prompt_template: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        is_prod: Optional[bool] | NotGiven = NOT_GIVEN,
        model_params: Optional[Dict[str, Union[float, str, bool]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        parent_id: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: Optional[int] | NotGiven = NOT_GIVEN,
        tag: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """
        Two types of prompts can be created - a root prompt or a child prompt (aka
        Prompt Version in the app).

                A root prompt can be created by providing the `name` param, and it will always be tagged as production.

                A child prompt can be created by providing the `parent_id` param. Note that the `name` param in this case will be ignored as all descendants from a root prompt would share the root's name. `is_prod` can also be provided to configure whether a child should be tagged as production.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/prompt",
            body=await async_maybe_transform(
                {
                    "prompt_template": prompt_template,
                    "description": description,
                    "is_prod": is_prod,
                    "model_params": model_params,
                    "name": name,
                    "parent_id": parent_id,
                    "project_id": project_id,
                    "tag": tag,
                },
                prompt_create_params.PromptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )

    async def update(
        self,
        id: str,
        *,
        is_prod: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """
        Update a prompt.

                `is_prod` tags the provided prompt as the production prompt within the prompt graph.

        Args:
          id: The id of the prompt to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v1/prompt/{id}",
            body=await async_maybe_transform({"is_prod": is_prod}, prompt_update_params.PromptUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: Optional[int] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptListResponse:
        """
        List all prompts with cursor-based pagination

        Args:
          cursor: Cursor for the next page

          project_id: ID of Project to filter by.

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/prompt/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "project_id": project_id,
                        "size": size,
                    },
                    prompt_list_params.PromptListParams,
                ),
            ),
            cast_to=PromptListResponse,
        )

    async def delete_root(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a root prompt and all of its children.

        Args:
          id: The id of the root prompt to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v1/prompt/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """
        Retrieve a prompt by id

        Args:
          id: The id of the prompt to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/prompt/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )

    async def retrieve_by_name(
        self,
        *,
        name: str,
        tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """
        Retrieve a prompt by name, defaulting to the production prompt, unless a tag to
        select the prompt by is specified

        Args:
          name: Name of the prompt.

          tag: Tag to select by. Defaults to selecting the production version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/prompt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "tag": tag,
                    },
                    prompt_retrieve_by_name_params.PromptRetrieveByNameParams,
                ),
            ),
            cast_to=Prompt,
        )


class PromptResourceWithRawResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

        self.create = to_raw_response_wrapper(
            prompt.create,
        )
        self.update = to_raw_response_wrapper(
            prompt.update,
        )
        self.list = to_raw_response_wrapper(
            prompt.list,
        )
        self.delete_root = to_raw_response_wrapper(
            prompt.delete_root,
        )
        self.retrieve_by_id = to_raw_response_wrapper(
            prompt.retrieve_by_id,
        )
        self.retrieve_by_name = to_raw_response_wrapper(
            prompt.retrieve_by_name,
        )


class AsyncPromptResourceWithRawResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

        self.create = async_to_raw_response_wrapper(
            prompt.create,
        )
        self.update = async_to_raw_response_wrapper(
            prompt.update,
        )
        self.list = async_to_raw_response_wrapper(
            prompt.list,
        )
        self.delete_root = async_to_raw_response_wrapper(
            prompt.delete_root,
        )
        self.retrieve_by_id = async_to_raw_response_wrapper(
            prompt.retrieve_by_id,
        )
        self.retrieve_by_name = async_to_raw_response_wrapper(
            prompt.retrieve_by_name,
        )


class PromptResourceWithStreamingResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

        self.create = to_streamed_response_wrapper(
            prompt.create,
        )
        self.update = to_streamed_response_wrapper(
            prompt.update,
        )
        self.list = to_streamed_response_wrapper(
            prompt.list,
        )
        self.delete_root = to_streamed_response_wrapper(
            prompt.delete_root,
        )
        self.retrieve_by_id = to_streamed_response_wrapper(
            prompt.retrieve_by_id,
        )
        self.retrieve_by_name = to_streamed_response_wrapper(
            prompt.retrieve_by_name,
        )


class AsyncPromptResourceWithStreamingResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

        self.create = async_to_streamed_response_wrapper(
            prompt.create,
        )
        self.update = async_to_streamed_response_wrapper(
            prompt.update,
        )
        self.list = async_to_streamed_response_wrapper(
            prompt.list,
        )
        self.delete_root = async_to_streamed_response_wrapper(
            prompt.delete_root,
        )
        self.retrieve_by_id = async_to_streamed_response_wrapper(
            prompt.retrieve_by_id,
        )
        self.retrieve_by_name = async_to_streamed_response_wrapper(
            prompt.retrieve_by_name,
        )
