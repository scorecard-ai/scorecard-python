# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Run"]


class Run(BaseModel):
    id: str
    """The ID of the Run."""

    metric_ids: List[str] = FieldInfo(alias="metricIds")
    """The IDs of the metrics this Run is using."""

    status: Literal[
        "pending",
        "awaiting_execution",
        "running_execution",
        "awaiting_scoring",
        "running_scoring",
        "awaiting_human_scoring",
        "completed",
    ]
    """The status of the Run."""

    testset_id: Optional[str] = FieldInfo(alias="testsetId", default=None)
    """The ID of the Testset this Run is testing."""

    system_version_id: Optional[str] = FieldInfo(alias="systemVersionId", default=None)
    """The ID of the system version this Run is using."""
