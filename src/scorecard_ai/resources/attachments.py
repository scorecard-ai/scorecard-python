# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import attachment_list_params, attachment_initiate_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.attachment import Attachment
from ..types.attachment_get_response import AttachmentGetResponse
from ..types.attachment_delete_response import AttachmentDeleteResponse
from ..types.attachment_initiate_response import AttachmentInitiateResponse

__all__ = ["AttachmentsResource", "AsyncAttachmentsResource"]


class AttachmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttachmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AttachmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttachmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AttachmentsResourceWithStreamingResponse(self)

    def list(
        self,
        session_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedResponse[Attachment]:
        """Lists the uploaded attachments for a session.

        Only committed attachments are
        returned.

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get_api_list(
            path_template("/sessions/{session_id}/attachments", session_id=session_id),
            page=SyncPaginatedResponse[Attachment],
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
                    attachment_list_params.AttachmentListParams,
                ),
            ),
            model=Attachment,
        )

    def delete(
        self,
        attachment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentDeleteResponse:
        """
        Deletes an attachment: both the stored file and its metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attachment_id:
            raise ValueError(f"Expected a non-empty value for `attachment_id` but received {attachment_id!r}")
        return self._delete(
            path_template("/attachments/{attachment_id}", attachment_id=attachment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentDeleteResponse,
        )

    def commit(
        self,
        attachment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Attachment:
        """
        Finalizes an upload after the file bytes have been PUT to the signed upload URL.
        Verifies the object landed in storage before the attachment starts describing
        the new content. Committing an already-committed attachment is a no-op.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attachment_id:
            raise ValueError(f"Expected a non-empty value for `attachment_id` but received {attachment_id!r}")
        return self._post(
            path_template("/attachments/{attachment_id}/commit", attachment_id=attachment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Attachment,
        )

    def get(
        self,
        attachment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentGetResponse:
        """
        Retrieves an attachment's metadata and a short-lived signed download URL for its
        content.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attachment_id:
            raise ValueError(f"Expected a non-empty value for `attachment_id` but received {attachment_id!r}")
        return self._get(
            path_template("/attachments/{attachment_id}", attachment_id=attachment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentGetResponse,
        )

    def initiate(
        self,
        *,
        content_type: str,
        file_path: str,
        session_id: str,
        sha256: str,
        size_bytes: int,
        filename: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentInitiateResponse:
        """Initiates (or deduplicates) an upload of a file attached to a session.

        If the
        exact content is already stored for this (session ID, file path), the response
        has `alreadyExists: true` and no upload is needed. Otherwise, PUT the file bytes
        to the returned `uploadUrl`, then call the commit endpoint. Re-initiating an
        existing (session ID, file path) with new content updates the attachment in
        place on commit.

        Args:
          content_type: MIME type of the file.

          file_path: The logical file path of the attachment (e.g. the path the agent wrote on disk).
              Together with the session ID it identifies the attachment: re-uploading the same
              path in the same session updates the existing attachment in place.

          session_id: The session ID the attachment belongs to. Matches the `session.id` emitted on
              OTel spans, which is how attachments are joined to traces and records.

          sha256: Lowercase hex SHA-256 of the file content.

          size_bytes: Size of the file in bytes.

          filename: Display filename. Defaults to none.

          metadata: Arbitrary metadata to store with the attachment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/attachments",
            body=maybe_transform(
                {
                    "content_type": content_type,
                    "file_path": file_path,
                    "session_id": session_id,
                    "sha256": sha256,
                    "size_bytes": size_bytes,
                    "filename": filename,
                    "metadata": metadata,
                },
                attachment_initiate_params.AttachmentInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentInitiateResponse,
        )


class AsyncAttachmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttachmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAttachmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttachmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scorecard-ai/scorecard-python#with_streaming_response
        """
        return AsyncAttachmentsResourceWithStreamingResponse(self)

    def list(
        self,
        session_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Attachment, AsyncPaginatedResponse[Attachment]]:
        """Lists the uploaded attachments for a session.

        Only committed attachments are
        returned.

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get_api_list(
            path_template("/sessions/{session_id}/attachments", session_id=session_id),
            page=AsyncPaginatedResponse[Attachment],
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
                    attachment_list_params.AttachmentListParams,
                ),
            ),
            model=Attachment,
        )

    async def delete(
        self,
        attachment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentDeleteResponse:
        """
        Deletes an attachment: both the stored file and its metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attachment_id:
            raise ValueError(f"Expected a non-empty value for `attachment_id` but received {attachment_id!r}")
        return await self._delete(
            path_template("/attachments/{attachment_id}", attachment_id=attachment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentDeleteResponse,
        )

    async def commit(
        self,
        attachment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Attachment:
        """
        Finalizes an upload after the file bytes have been PUT to the signed upload URL.
        Verifies the object landed in storage before the attachment starts describing
        the new content. Committing an already-committed attachment is a no-op.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attachment_id:
            raise ValueError(f"Expected a non-empty value for `attachment_id` but received {attachment_id!r}")
        return await self._post(
            path_template("/attachments/{attachment_id}/commit", attachment_id=attachment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Attachment,
        )

    async def get(
        self,
        attachment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentGetResponse:
        """
        Retrieves an attachment's metadata and a short-lived signed download URL for its
        content.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attachment_id:
            raise ValueError(f"Expected a non-empty value for `attachment_id` but received {attachment_id!r}")
        return await self._get(
            path_template("/attachments/{attachment_id}", attachment_id=attachment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentGetResponse,
        )

    async def initiate(
        self,
        *,
        content_type: str,
        file_path: str,
        session_id: str,
        sha256: str,
        size_bytes: int,
        filename: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentInitiateResponse:
        """Initiates (or deduplicates) an upload of a file attached to a session.

        If the
        exact content is already stored for this (session ID, file path), the response
        has `alreadyExists: true` and no upload is needed. Otherwise, PUT the file bytes
        to the returned `uploadUrl`, then call the commit endpoint. Re-initiating an
        existing (session ID, file path) with new content updates the attachment in
        place on commit.

        Args:
          content_type: MIME type of the file.

          file_path: The logical file path of the attachment (e.g. the path the agent wrote on disk).
              Together with the session ID it identifies the attachment: re-uploading the same
              path in the same session updates the existing attachment in place.

          session_id: The session ID the attachment belongs to. Matches the `session.id` emitted on
              OTel spans, which is how attachments are joined to traces and records.

          sha256: Lowercase hex SHA-256 of the file content.

          size_bytes: Size of the file in bytes.

          filename: Display filename. Defaults to none.

          metadata: Arbitrary metadata to store with the attachment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/attachments",
            body=await async_maybe_transform(
                {
                    "content_type": content_type,
                    "file_path": file_path,
                    "session_id": session_id,
                    "sha256": sha256,
                    "size_bytes": size_bytes,
                    "filename": filename,
                    "metadata": metadata,
                },
                attachment_initiate_params.AttachmentInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentInitiateResponse,
        )


class AttachmentsResourceWithRawResponse:
    def __init__(self, attachments: AttachmentsResource) -> None:
        self._attachments = attachments

        self.list = to_raw_response_wrapper(
            attachments.list,
        )
        self.delete = to_raw_response_wrapper(
            attachments.delete,
        )
        self.commit = to_raw_response_wrapper(
            attachments.commit,
        )
        self.get = to_raw_response_wrapper(
            attachments.get,
        )
        self.initiate = to_raw_response_wrapper(
            attachments.initiate,
        )


class AsyncAttachmentsResourceWithRawResponse:
    def __init__(self, attachments: AsyncAttachmentsResource) -> None:
        self._attachments = attachments

        self.list = async_to_raw_response_wrapper(
            attachments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            attachments.delete,
        )
        self.commit = async_to_raw_response_wrapper(
            attachments.commit,
        )
        self.get = async_to_raw_response_wrapper(
            attachments.get,
        )
        self.initiate = async_to_raw_response_wrapper(
            attachments.initiate,
        )


class AttachmentsResourceWithStreamingResponse:
    def __init__(self, attachments: AttachmentsResource) -> None:
        self._attachments = attachments

        self.list = to_streamed_response_wrapper(
            attachments.list,
        )
        self.delete = to_streamed_response_wrapper(
            attachments.delete,
        )
        self.commit = to_streamed_response_wrapper(
            attachments.commit,
        )
        self.get = to_streamed_response_wrapper(
            attachments.get,
        )
        self.initiate = to_streamed_response_wrapper(
            attachments.initiate,
        )


class AsyncAttachmentsResourceWithStreamingResponse:
    def __init__(self, attachments: AsyncAttachmentsResource) -> None:
        self._attachments = attachments

        self.list = async_to_streamed_response_wrapper(
            attachments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            attachments.delete,
        )
        self.commit = async_to_streamed_response_wrapper(
            attachments.commit,
        )
        self.get = async_to_streamed_response_wrapper(
            attachments.get,
        )
        self.initiate = async_to_streamed_response_wrapper(
            attachments.initiate,
        )
