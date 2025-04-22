# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SystemConfigCreateParams", "ValidationError"]


class SystemConfigCreateParams(TypedDict, total=False):
    id: Required[str]
    """The ID of the system configuration"""

    config: Required[Dict[str, object]]
    """The configuration of the system"""

    label: Required[str]
    """The label for the system configuration"""

    body_system_id: Required[Annotated[str, PropertyInfo(alias="systemId")]]
    """The ID of the system the configuration belongs to"""

    validation_errors: Annotated[Iterable[ValidationError], PropertyInfo(alias="validationErrors")]
    """Validation errors found in the configuration.

    If present, the configuration doesn't fully conform to its system's
    configSchema.
    """


class ValidationError(TypedDict, total=False):
    message: Required[str]
    """Human-readable error description"""

    path: Required[str]
    """JSON Pointer to the field with the validation error"""
