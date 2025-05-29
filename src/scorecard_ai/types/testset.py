# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Testset", "FieldMapping"]


class FieldMapping(BaseModel):
    expected: List[str]
    """Fields that represent expected outputs."""

    inputs: List[str]
    """Fields that represent inputs to the AI system."""

    metadata: List[str]
    """Fields that are not inputs or expected outputs."""


class Testset(BaseModel):
    __test__ = False
    id: str
    """The ID of the Testset."""

    description: str
    """The description of the Testset."""

    field_mapping: FieldMapping = FieldInfo(alias="fieldMapping")
    """
    Maps top-level keys of the Testcase schema to their roles (input/expected
    output). Unmapped fields are treated as metadata.
    """

    json_schema: Dict[str, object] = FieldInfo(alias="jsonSchema")
    """The JSON schema for each Testcase in the Testset."""

    name: str
    """The name of the Testset."""
