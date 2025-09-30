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

    metric_version_ids: List[str] = FieldInfo(alias="metricVersionIds")
    """The IDs of the metric versions this Run is using."""

    num_expected_records: Optional[float] = FieldInfo(alias="numExpectedRecords", default=None)
    """The number of expected records in the Run.

    Determined by the number of testcases in the Run's Testset at the time of Run
    creation.
    """

    num_records: float = FieldInfo(alias="numRecords")
    """The number of records in the Run."""

    num_scores: float = FieldInfo(alias="numScores")
    """The number of completed scores in the Run so far."""

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

    system_id: Optional[str] = FieldInfo(alias="systemId", default=None)
    """The ID of the system this Run is using."""

    system_version_id: Optional[str] = FieldInfo(alias="systemVersionId", default=None)
    """The ID of the system version this Run is using."""

    testset_id: Optional[str] = FieldInfo(alias="testsetId", default=None)
    """The ID of the Testset this Run is testing."""
