# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    """A Project in the Scorecard system."""

    id: str
    """The ID of the Project."""

    description: Optional[str] = None
    """The description of the Project."""

    name: Optional[str] = None
    """The name of the Project."""

    status: Optional[Literal["in_progress", "in_review", "completed"]] = None
    """The review status of the Project, set by an organization admin.

    `null` if the Project doesn't track a status.
    """

    status_updated_at: Optional[str] = FieldInfo(alias="statusUpdatedAt", default=None)
    """The ISO 8601 timestamp when `status` last changed.

    `null` if a status has never been set.
    """
