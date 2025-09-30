# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    metric_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="metricIds")]]
    """The IDs of the metrics this Run is using."""

    system_version_id: Annotated[Optional[str], PropertyInfo(alias="systemVersionId")]
    """The ID of the system version this Run is using."""

    testset_id: Annotated[Optional[str], PropertyInfo(alias="testsetId")]
    """The ID of the Testset this Run is testing."""
