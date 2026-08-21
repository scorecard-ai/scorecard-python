# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MetricGroupUpdateParams"]


class MetricGroupUpdateParams(TypedDict, total=False):
    description: str
    """The new description of the Metric Group."""

    metric_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="metricIds")]
    """The new set of Metric IDs for the group, replacing the current set.

    Every Metric must belong to the same Project as the group.
    """

    name: str
    """The new name of the Metric Group."""
