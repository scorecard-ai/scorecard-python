# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Testcase", "ValidationError"]


class ValidationError(BaseModel):
    message: str
    """Human-readable error description"""

    path: str
    """JSON Pointer to the field with the validation error"""


class Testcase(BaseModel):
    __test__ = False
    id: str
    """The ID of the testcase"""

    inputs: Dict[str, object]
    """Derived from data based on the testset's fieldMapping.

    Contains all fields marked as inputs, including those with validation errors.
    """

    json_data: Dict[str, object] = FieldInfo(alias="jsonData")
    """The JSON data of the testcase, which is validated against the testset's schema."""

    labels: Dict[str, object]
    """Derived from data based on the testset's fieldMapping.

    Contains all fields marked as labels, including those with validation errors.
    """

    testset_id: str = FieldInfo(alias="testsetId")
    """The ID of the testset this testcase belongs to"""

    validation_errors: Optional[List[ValidationError]] = FieldInfo(alias="validationErrors", default=None)
    """Validation errors found in the testcase data.

    If present, the testcase doesn't fully conform to its testset's schema.
    """
