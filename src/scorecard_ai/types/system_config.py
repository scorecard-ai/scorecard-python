# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SystemConfig", "ValidationError"]


class ValidationError(BaseModel):
    message: str
    """Human-readable error description."""

    path: str
    """JSON Pointer to the field with the validation error."""


class SystemConfig(BaseModel):
    id: str
    """The ID of the system configuration."""

    config: Dict[str, object]
    """The configuration of the system."""

    name: str
    """The name of the system configuration."""

    system_id: str = FieldInfo(alias="systemId")
    """The ID of the system the configuration belongs to."""

    validation_errors: Optional[List[ValidationError]] = FieldInfo(alias="validationErrors", default=None)
    """Validation errors found in the configuration.

    If present, the configuration doesn't fully conform to its system's
    configSchema.
    """
