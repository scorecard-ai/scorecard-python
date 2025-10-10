# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .score import Score
from .record import Record

__all__ = ["RecordListResponse"]


class RecordListResponse(Record):
    scores: List[Score]
    """All scores associated with this record."""
