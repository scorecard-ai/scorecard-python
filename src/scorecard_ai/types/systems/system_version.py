# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SystemVersion", "ValidationError"]


class ValidationError(BaseModel):
    message: str
    """Human-readable error description."""

    path: str
    """JSON Pointer to the field with the validation error."""


class SystemVersion(BaseModel):
    id: str
    """The ID of the system version."""

    config: Dict[str, object]
    """The configuration of the system version."""

    name: str
    """The name of the system version."""

    system_id: str = FieldInfo(alias="systemId")
    """The ID of the system the system version belongs to."""

    validation_errors: Optional[List[ValidationError]] = FieldInfo(alias="validationErrors", default=None)
    """Validation errors found in the system version.

    If present, the system version doesn't fully conform to its system's
    configSchema.
    """
