# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Score", "ValidationError"]


class ValidationError(BaseModel):
    message: str
    """Human-readable error description."""

    path: str
    """JSON Pointer to the field with the validation error."""


class Score(BaseModel):
    metric_config_id: str = FieldInfo(alias="metricConfigId")
    """The ID of the MetricConfig this Score is for."""

    record_id: str = FieldInfo(alias="recordId")
    """The ID of the Record this Score is for."""

    score: Dict[str, object]
    """The score of the Record, as arbitrary JSON.

    This data should ideally conform to the output schema defined by the associated
    MetricConfig. If it doesn't, validation errors will be captured in the
    `validationErrors` field.
    """

    validation_errors: Optional[List[ValidationError]] = FieldInfo(alias="validationErrors", default=None)
    """Validation errors found in the Score data.

    If present, the Score doesn't fully conform to its MetricConfig's schema.
    """
