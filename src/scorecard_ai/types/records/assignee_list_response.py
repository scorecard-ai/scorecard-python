# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .record_assignment import RecordAssignment

__all__ = ["AssigneeListResponse"]


class AssigneeListResponse(BaseModel):
    data: List[RecordAssignment]
