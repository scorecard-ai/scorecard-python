# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ProjectUpdateParams"]


class ProjectUpdateParams(TypedDict, total=False):
    description: str
    """The new description of the Project."""

    name: str
    """The new name of the Project."""

    status: Optional[Literal["in_progress", "in_review", "completed"]]
    """The new review status of the Project.

    Only organization admins can change it. Pass `null` to stop tracking a status.
    """
