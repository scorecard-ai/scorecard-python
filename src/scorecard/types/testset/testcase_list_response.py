# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .test_case import TestCase

__all__ = ["TestcaseListResponse"]


class TestcaseListResponse(BaseModel):
    __test__ = False
    count: int

    next: Optional[str] = None
    """The URL to fetch the next page of testcases."""

    previous: Optional[str] = None
    """The URL to fetch the previous page of testcases."""

    results: List[TestCase]
    """The list of Testcases retrieved in this page."""
