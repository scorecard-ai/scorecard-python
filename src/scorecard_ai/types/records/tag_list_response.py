# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .record_tag import RecordTag

__all__ = ["TagListResponse"]


class TagListResponse(BaseModel):
    data: List[RecordTag]
