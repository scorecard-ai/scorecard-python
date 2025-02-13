# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "TestCase",
    "CustomInputs",
    "CustomInputsFileURL",
    "CustomInputsJsonObjectOutput",
    "CustomLabels",
    "CustomLabelsFileURL",
    "CustomLabelsJsonObjectOutput",
]


class CustomInputsFileURL(BaseModel):
    url: str

    name: Optional[str] = None


class CustomInputsJsonObjectOutput(BaseModel):
    value: Union[Dict[str, object], List[object], str, float, bool, None] = None
    """
    The value of the JSON object, which can be a dictionary, list, string, integer,
    float, boolean, or None.
    """


CustomInputs: TypeAlias = Union[str, CustomInputsFileURL, CustomInputsJsonObjectOutput, float, bool, None]


class CustomLabelsFileURL(BaseModel):
    url: str

    name: Optional[str] = None


class CustomLabelsJsonObjectOutput(BaseModel):
    value: Union[Dict[str, object], List[object], str, float, bool, None] = None
    """
    The value of the JSON object, which can be a dictionary, list, string, integer,
    float, boolean, or None.
    """


CustomLabels: TypeAlias = Union[str, CustomLabelsFileURL, CustomLabelsJsonObjectOutput, float, bool, None]


class TestCase(BaseModel):
    __test__ = False
    testset_id: int
    """The ID of the testset the testcase belongs to."""

    user_query: str
    """The user query for the testcase."""

    id: Optional[int] = None
    """The ID of the testcase."""

    context: Optional[str] = None
    """The context for the testcase."""

    created_at: Optional[datetime] = None
    """The creation date and time of the testcase."""

    custom_inputs: Optional[Dict[str, Optional[CustomInputs]]] = None

    custom_labels: Optional[Dict[str, Optional[CustomLabels]]] = None

    ideal: Optional[str] = None
    """The ideal response for the testcase."""
