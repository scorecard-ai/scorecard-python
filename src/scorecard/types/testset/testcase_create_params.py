# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "TestcaseCreateParams",
    "CustomInputs",
    "CustomInputsFileURL",
    "CustomInputsJsonObjectInput",
    "CustomLabels",
    "CustomLabelsFileURL",
    "CustomLabelsJsonObjectInput",
]


class TestcaseCreateParams(TypedDict, total=False):
    context: Optional[str]
    """The context to be used while generating the testcase."""

    custom_inputs: Optional[Dict[str, Optional[CustomInputs]]]

    custom_labels: Optional[Dict[str, Optional[CustomLabels]]]

    ideal: Optional[str]
    """The ideal response to the user query."""

    user_query: str
    """The user query to be executed."""


class CustomInputsFileURL(TypedDict, total=False):
    url: Required[str]

    name: Optional[str]


class CustomInputsJsonObjectInput(TypedDict, total=False):
    value: Required[Union[Dict[str, object], Iterable[object], str, float, bool, None]]
    """
    The value of the JSON object, which can be a dictionary, list, string, integer,
    float, boolean, or None.
    """


CustomInputs: TypeAlias = Union[str, CustomInputsFileURL, CustomInputsJsonObjectInput, float, bool]


class CustomLabelsFileURL(TypedDict, total=False):
    url: Required[str]

    name: Optional[str]


class CustomLabelsJsonObjectInput(TypedDict, total=False):
    value: Required[Union[Dict[str, object], Iterable[object], str, float, bool, None]]
    """
    The value of the JSON object, which can be a dictionary, list, string, integer,
    float, boolean, or None.
    """


CustomLabels: TypeAlias = Union[str, CustomLabelsFileURL, CustomLabelsJsonObjectInput, float, bool]
