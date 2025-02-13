# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ScoreUpdateParams"]


class ScoreUpdateParams(TypedDict, total=False):
    run_id: Required[int]
    """The run ID that created the test record to be scored."""

    testrecord_id: Required[int]
    """The ID of the testrecord whose score will be updated."""

    binary_score: Required[Optional[bool]]
    """The new boolean score to assign."""

    int_score: Required[Optional[int]]
    """The new integer score to assign."""

    reasoning: Required[Optional[str]]
    """The reasoning for the score update."""
