# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MetricGroup"]


class MetricGroup(BaseModel):
    """
    A Metric Group is a named collection of Metrics within a Project, used to score or compare records with a consistent set of Metrics.
    """

    id: str
    """The ID of the Metric Group."""

    created_at: str = FieldInfo(alias="createdAt")
    """The ISO 8601 timestamp when the Metric Group was created."""

    description: str
    """The description of the Metric Group."""

    metric_ids: List[str] = FieldInfo(alias="metricIds")
    """The IDs of the Metrics in the group."""

    name: str
    """The name of the Metric Group."""

    project_id: str = FieldInfo(alias="projectId")
    """The ID of the Project the Metric Group belongs to."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """The ISO 8601 timestamp when the Metric Group was last updated."""
