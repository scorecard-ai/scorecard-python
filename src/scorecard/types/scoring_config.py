# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ScoringConfig"]


class ScoringConfig(BaseModel):
    id: Optional[int] = None

    config: Optional[object] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    is_archived: Optional[bool] = None

    metrics: Optional[List[int]] = None

    name: Optional[str] = None

    org_id: Optional[str] = None
    """The organization this resource belongs to."""

    project_id: Optional[int] = None
    """The ID of the project the scoring config belongs to."""

    user_id: Optional[str] = None
    """The user this record belongs to."""
