# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    metrics: Optional[Iterable[int]]

    model_params: Optional[object]
    """Optional. The model parameters to use for this run."""

    notes: Optional[str]

    prompt_id: Optional[str]

    prompt_template: Optional[str]

    scoring_config_id: Optional[int]

    source: str

    status: str

    testset_id: Optional[int]
