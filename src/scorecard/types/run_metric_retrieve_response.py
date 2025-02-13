# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["RunMetricRetrieveResponse", "RunMetricRetrieveResponseItem"]


class RunMetricRetrieveResponseItem(BaseModel):
    id: Optional[int] = None

    created_at: Optional[datetime] = None

    metric_id: Optional[int] = None

    run_id: Optional[int] = None


RunMetricRetrieveResponse: TypeAlias = List[RunMetricRetrieveResponseItem]
