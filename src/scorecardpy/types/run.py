# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Run"]


class Run(BaseModel):
    id: str
    """The ID of the Run"""

    metric_ids: List[str] = FieldInfo(alias="metricIds")
    """The IDs of the metrics this Run is using"""

    testset_id: str = FieldInfo(alias="testsetId")
    """The ID of the Testset this Run is testing"""

    system_config_id: Optional[str] = FieldInfo(alias="systemConfigId", default=None)
    """The ID of the system configuration this Run is using"""
