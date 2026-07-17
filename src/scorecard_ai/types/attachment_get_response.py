# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .attachment import Attachment

__all__ = ["AttachmentGetResponse"]


class AttachmentGetResponse(Attachment):
    """A file attached to a session.

    Bytes live in object storage; this describes the last committed content.
    """

    download_expires_at: Optional[str] = FieldInfo(alias="downloadExpiresAt", default=None)
    """ISO 8601 expiry of `downloadUrl`."""

    download_url: Optional[str] = FieldInfo(alias="downloadUrl", default=None)
    """Short-lived signed URL to download the file.

    Null while the attachment has no committed content.
    """
