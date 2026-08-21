# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MetricGroupCreateParams"]


class MetricGroupCreateParams(TypedDict, total=False):
    metric_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="metricIds")]]
    """The IDs of the Metrics to include in the group.

    Every Metric must belong to the same Project as the group.
    """

    name: Required[str]
    """The name of the Metric Group."""

    description: str
    """The description of the Metric Group."""
