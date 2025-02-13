# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ScoreCreateParams"]


class ScoreCreateParams(TypedDict, total=False):
    run_id: Required[int]
    """The ID of the run that created the testrecord to be scored."""

    binary_score: Required[Optional[bool]]
    """Specify boolean scores."""

    int_score: Required[Optional[int]]
    """Specify integer scores."""

    metric_id: Required[int]
    """The ID of the metric"""

    reasoning: Required[Optional[str]]
    """The reasoning for the assigned score."""
