# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AssigneeCreateParams"]


class AssigneeCreateParams(TypedDict, total=False):
    assignee_user_id: Required[Annotated[str, PropertyInfo(alias="assigneeUserId")]]
    """The ID of the organization member to assign.

    Idempotent: re-assigning an existing member returns the existing assignment.
    """
