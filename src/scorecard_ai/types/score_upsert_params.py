# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScoreUpsertParams"]


class ScoreUpsertParams(TypedDict, total=False):
    record_id: Required[Annotated[str, PropertyInfo(alias="recordId")]]

    score: Required[Dict[str, object]]
    """The score of the Record, as arbitrary JSON.

    This data should ideally conform to the output schema defined by the associated
    MetricConfig. If it doesn't, validation errors will be captured in the
    `validationErrors` field.
    """
