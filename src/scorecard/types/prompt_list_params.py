# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PromptListParams"]


class PromptListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Cursor for the next page"""

    project_id: Optional[int]
    """ID of Project to filter by."""

    size: int
    """Page size"""
