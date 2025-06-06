# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Testcase", "ValidationError"]


class ValidationError(BaseModel):
    message: str
    """Human-readable error description."""

    path: str
    """JSON Pointer to the field with the validation error."""


class Testcase(BaseModel):
    __test__ = False
    id: str
    """The ID of the Testcase."""

    expected: Dict[str, object]
    """Derived from data based on the Testset's fieldMapping.

    Contains all fields marked as expected outputs, including those with validation
    errors.
    """

    inputs: Dict[str, object]
    """Derived from data based on the Testset's fieldMapping.

    Contains all fields marked as inputs, including those with validation errors.
    """

    json_data: Dict[str, object] = FieldInfo(alias="jsonData")
    """The JSON data of the Testcase, which is validated against the Testset's schema."""

    testset_id: str = FieldInfo(alias="testsetId")
    """The ID of the Testset this Testcase belongs to."""

    validation_errors: Optional[List[ValidationError]] = FieldInfo(alias="validationErrors", default=None)
    """Validation errors found in the Testcase data.

    If present, the Testcase doesn't fully conform to its Testset's schema.
    """
