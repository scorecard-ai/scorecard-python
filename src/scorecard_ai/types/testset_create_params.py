# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TestsetCreateParams", "FieldMapping"]


class TestsetCreateParams(TypedDict, total=False):
    description: Required[str]
    """The description of the Testset."""

    field_mapping: Required[Annotated[FieldMapping, PropertyInfo(alias="fieldMapping")]]
    """
    Maps top-level keys of the Testcase schema to their roles (input/expected
    output). Unmapped fields are treated as metadata.
    """

    json_schema: Required[Annotated[Dict[str, object], PropertyInfo(alias="jsonSchema")]]
    """The JSON schema for each Testcase in the Testset."""

    name: Required[str]
    """The name of the Testset."""


class FieldMapping(TypedDict, total=False):
    expected: Required[List[str]]
    """Fields that represent expected outputs."""

    inputs: Required[List[str]]
    """Fields that represent inputs to the AI system."""

    metadata: Required[List[str]]
    """Fields that are not inputs or expected outputs."""
