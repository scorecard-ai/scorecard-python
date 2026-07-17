# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AttachmentInitiateResponse"]


class AttachmentInitiateResponse(BaseModel):
    id: str
    """The ID of the Attachment."""

    already_exists: bool = FieldInfo(alias="alreadyExists")
    """
    True if this exact content is already stored for this (session, file path) — no
    upload is needed and no upload URL is returned.
    """

    expires_at: Optional[str] = FieldInfo(alias="expiresAt", default=None)
    """ISO 8601 expiry of `uploadUrl`."""

    upload_method: Optional[Literal["PUT"]] = FieldInfo(alias="uploadMethod", default=None)
    """HTTP method to use with `uploadUrl`."""

    upload_url: Optional[str] = FieldInfo(alias="uploadUrl", default=None)
    """Signed URL to PUT the file bytes to. Null when `alreadyExists` is true."""
