# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RecordTag"]


class RecordTag(BaseModel):
    """An arbitrary tag applied to a Record (e.g.

    `urgent`, `regression`, `env:prod`), either by a user or lifted from OTel span attributes at ingest.
    """

    id: str
    """The ID of the tag."""

    created_at: str = FieldInfo(alias="createdAt")
    """The ISO 8601 timestamp when the tag was created."""

    record_id: str = FieldInfo(alias="recordId")
    """The ID of the Record this tag belongs to."""

    source: Literal["user", "otel"]
    """
    How the tag was applied: `user` (UI, SDK, or REST) or `otel` (lifted from a span
    attribute at ingest).
    """

    text: str
    """The tag text. May encode key:value semantics with a colon (e.g. `env:prod`)."""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """The ID of the user who applied the tag; null for OTel-sourced tags."""
