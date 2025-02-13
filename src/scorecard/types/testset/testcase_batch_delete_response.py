# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["TestcaseBatchDeleteResponse"]


class TestcaseBatchDeleteResponse(BaseModel):
    __test__ = False
    detail: str
    """The message indicating the testcases were deleted."""

    ids: List[int]
    """The IDs of the testcases that were deleted."""
