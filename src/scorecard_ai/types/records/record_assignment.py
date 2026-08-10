# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RecordAssignment"]


class RecordAssignment(BaseModel):
    """An assignment of an organization member to a Record."""

    id: str
    """The ID of the record assignment."""

    assigned_by_user_id: str = FieldInfo(alias="assignedByUserId")
    """The ID of the user who created the assignment."""

    assignee_user_id: str = FieldInfo(alias="assigneeUserId")
    """The ID of the organization member assigned to the Record."""

    created_at: str = FieldInfo(alias="createdAt")
    """The ISO 8601 timestamp when the assignment was created."""

    record_id: str = FieldInfo(alias="recordId")
    """The ID of the Record this assignment belongs to."""
