# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Annotation"]


class Annotation(BaseModel):
    """
    An annotation on a Record, containing a rating (thumbs up/down) and/or a text comment.
    """

    id: str
    """The ID of the Annotation."""

    comment: Optional[str] = None
    """An optional text comment for the annotation."""

    created_at: str = FieldInfo(alias="createdAt")
    """The ISO 8601 timestamp when the annotation was created."""

    rating: Optional[bool] = None
    """
    The rating of the annotation: true (positive), false (negative), or null (no
    rating).
    """

    record_id: str = FieldInfo(alias="recordId")
    """The ID of the Record this Annotation belongs to."""

    span_id: Optional[str] = FieldInfo(alias="spanId", default=None)
    """Optional span ID linking this annotation to a specific span."""

    user_id: str = FieldInfo(alias="userId")
    """The ID of the user who created the annotation."""
