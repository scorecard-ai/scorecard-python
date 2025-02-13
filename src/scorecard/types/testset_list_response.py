# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .testset.testset import Testset

__all__ = ["TestsetListResponse"]


class TestsetListResponse(BaseModel):
    __test__ = False
    items: List[Testset]

    current_page: Optional[str] = None
    """Cursor to refetch the current page"""

    current_page_backwards: Optional[str] = None
    """Cursor to refetch the current page starting from the last item"""

    next_page: Optional[str] = None
    """Cursor for the next page"""

    previous_page: Optional[str] = None
    """Cursor for the previous page"""

    total: Optional[int] = None
    """Total items"""
