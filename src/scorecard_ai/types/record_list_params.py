# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["RecordListParams"]


class RecordListParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination.

    Pass the `nextCursor` from the previous response to get the next page of
    results.
    """

    limit: int
    """Maximum number of items to return (1-100).

    Use with `cursor` for pagination through large sets.
    """

    tags: SequenceNotStr[str]
    """Filter to records carrying every listed tag (repeatable, AND semantics).

    E.g. `?tags=urgent&tags=regression`.
    """
