# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Attachment"]


class Attachment(BaseModel):
    """A file attached to a session.

    Bytes live in object storage; this describes the last committed content.
    """

    id: str
    """The ID of the Attachment."""

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)
    """MIME type of the last committed content. Null until the first commit."""

    filename: Optional[str] = None
    """Display filename, if provided."""

    file_path: str = FieldInfo(alias="filePath")
    """The logical file path of the attachment (e.g.

    the path the agent wrote on disk). Together with the session ID it identifies
    the attachment: re-uploading the same path in the same session updates the
    existing attachment in place.
    """

    metadata: Optional[Dict[str, object]] = None
    """Arbitrary caller-supplied metadata."""

    session_id: str = FieldInfo(alias="sessionId")
    """The session ID the attachment belongs to.

    Matches the `session.id` emitted on OTel spans, which is how attachments are
    joined to traces and records.
    """

    sha256: Optional[str] = None
    """SHA-256 of the last committed content. Null until the first commit."""

    size_bytes: Optional[int] = FieldInfo(alias="sizeBytes", default=None)
    """Size in bytes of the last committed content. Null until the first commit."""

    status: Literal["pending", "uploaded"]
    """
    `uploaded` once a commit has succeeded; `pending` while an initiated upload has
    not been committed yet.
    """

    uploaded_at: Optional[str] = FieldInfo(alias="uploadedAt", default=None)
    """ISO 8601 timestamp of the last successful commit. Null until the first commit."""
