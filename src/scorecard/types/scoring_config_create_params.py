# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["ScoringConfigCreateParams"]


class ScoringConfigCreateParams(TypedDict, total=False):
    description: Optional[str]

    metrics: Optional[Iterable[int]]

    name: Optional[str]

    project_id: int
