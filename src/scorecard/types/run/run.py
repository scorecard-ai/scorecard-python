# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Run"]


class Run(BaseModel):
    id: Optional[int] = None

    created_at: Optional[datetime] = None
    """The creation date and time of the run."""

    execution_end_time: Optional[datetime] = None
    """The end time of the run."""

    execution_start_time: Optional[datetime] = None
    """The start time of the run."""

    limit_testcases: Optional[int] = None
    """The maximum number of testcases to run."""

    api_model_params: Optional[object] = FieldInfo(alias="model_params", default=None)
    """The model parameters used when generating the run."""

    notes: Optional[str] = None
    """Notes about the run."""

    prompt_id: Optional[str] = None

    prompt_template: Optional[str] = None
    """The prompt template to be used while executing the run."""

    scoring_config_id: Optional[int] = None
    """The ID of the scoring configuration the run uses."""

    scoring_end_time: Optional[datetime] = None
    """The end time of scoring the run's results."""

    scoring_start_time: Optional[datetime] = None
    """The start time of scoring the run's results."""

    source: Optional[str] = None
    """How the run was created."""

    status: Optional[str] = None
    """The current status of the run."""

    testset_id: Optional[int] = None
    """The testset that was executed in this run."""

    updated_at: Optional[datetime] = None
    """The last time the run was updated."""
