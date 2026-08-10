# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AttachmentInitiateParams"]


class AttachmentInitiateParams(TypedDict, total=False):
    content_type: Required[Annotated[str, PropertyInfo(alias="contentType")]]
    """MIME type of the file."""

    file_path: Required[Annotated[str, PropertyInfo(alias="filePath")]]
    """The logical file path of the attachment (e.g.

    the path the agent wrote on disk). Together with the session ID it identifies
    the attachment: re-uploading the same path in the same session updates the
    existing attachment in place.
    """

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]
    """The session ID the attachment belongs to.

    Matches the `session.id` emitted on OTel spans, which is how attachments are
    joined to traces and records.
    """

    sha256: Required[str]
    """Lowercase hex SHA-256 of the file content."""

    size_bytes: Required[Annotated[int, PropertyInfo(alias="sizeBytes")]]
    """Size of the file in bytes."""

    filename: str
    """Display filename. Defaults to none."""

    metadata: Dict[str, object]
    """Arbitrary metadata to store with the attachment."""
