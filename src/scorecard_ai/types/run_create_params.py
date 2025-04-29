# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    metric_ids: Required[Annotated[List[str], PropertyInfo(alias="metricIds")]]
    """The IDs of the metrics this Run is using."""

    testset_id: Required[Annotated[str, PropertyInfo(alias="testsetId")]]
    """The ID of the Testset this Run is testing."""

    system_config_id: Annotated[str, PropertyInfo(alias="systemConfigId")]
    """The ID of the system configuration this Run is using."""
