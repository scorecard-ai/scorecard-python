# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .prompt import Prompt
from .._models import BaseModel

__all__ = ["PromptListResponse"]


class PromptListResponse(BaseModel):
    items: List[Prompt]

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
