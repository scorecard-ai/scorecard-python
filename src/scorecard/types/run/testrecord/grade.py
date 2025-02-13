# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Grade"]


class Grade(BaseModel):
    id: Optional[int] = None
    """The ID of the grade."""

    binary_score: Optional[bool] = None
    """The binary score assigned to the grade."""

    created_at: Optional[datetime] = None
    """when the grade was created."""

    error_message: Optional[str] = None
    """The error message if the grade was not created successfully."""

    human_eval: Optional[bool] = None
    """Indicates if a human should assign a grade."""

    int_score: Optional[int] = None
    """The integer score assigned to the grade."""

    metric_id: Optional[int] = None
    """The ID of the metric used to compute the grade."""

    reasoning: Optional[str] = None
    """The reasoning for the assigned score."""

    run_id: Optional[int] = None
    """The ID of the run that created the grade."""

    status: Optional[Literal["pending", "error", "completed"]] = None
    """The status of the grade."""

    testcase_id: Optional[int] = None
    """The ID of the testcase associated with the grade."""

    testrecord_id: Optional[int] = None
    """The ID of the testrecord for which the grade was created."""

    updated_at: Optional[datetime] = None
    """when the grade was last updated."""

    user_id: Optional[str] = None
