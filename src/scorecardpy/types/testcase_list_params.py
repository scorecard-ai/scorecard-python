# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TestcaseListParams"]


class TestcaseListParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination.

    Pass the `nextCursor` from the previous response to get the next page of
    results.
    """

    limit: int
    """Maximum number of items to return (1-100).

    Use with `cursor` for pagination through large sets.
    """
