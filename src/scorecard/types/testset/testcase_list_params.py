# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TestcaseListParams"]


class TestcaseListParams(TypedDict, total=False):
    limit: int
    """The number of testcases to return."""

    offset: int
    """The offset to start from."""
