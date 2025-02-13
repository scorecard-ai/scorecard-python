# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TestsetUpdateParams", "CustomSchema", "CustomSchemaVariable"]


class TestsetUpdateParams(TypedDict, total=False):
    custom_schema: Optional[CustomSchema]
    """Custom schema model with an ordered list of custom variables."""

    description: Optional[str]
    """A description for the testset."""

    name: Optional[str]

    using_retrieval: Optional[bool]
    """Whether or not the testset uses retrieval."""


class CustomSchemaVariable(TypedDict, total=False):
    data_type: Required[Literal["text", "file_url", "json_object"]]
    """Enum for data types."""

    name: Required[str]

    role: Required[Literal["input", "output", "label", "metadata"]]
    """Enum for role types."""

    description: Optional[str]


class CustomSchema(TypedDict, total=False):
    variables: Iterable[CustomSchemaVariable]
    """Ordered list of custom variables"""
