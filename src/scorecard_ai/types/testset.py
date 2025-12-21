# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Testset", "FieldMapping"]


class FieldMapping(BaseModel):
    """
    Maps top-level keys of the Testcase schema to their roles (input/expected output). Unmapped fields are treated as metadata.
    """

    expected: List[str]
    """Fields that represent expected outputs."""

    inputs: List[str]
    """Fields that represent inputs to the AI system."""

    metadata: List[str]
    """Fields that are not inputs or expected outputs."""


class Testset(BaseModel):
    __test__ = False
    """
    A collection of Testcases that share the same schema.
    Each Testset defines the structure of its Testcases through a JSON schema.
    The `fieldMapping` object maps top-level keys of the Testcase schema to their roles (input/expected output).
    Fields not mentioned in the `fieldMapping` during creation or update are treated as metadata.

    ## JSON Schema validation constraints supported:

    - **Required fields** - Fields listed in the schema's `required` array must be present in Testcases.
    - **Type validation** - Values must match the specified type (string, number, boolean, null, integer, object, array).
    - **Enum validation** - Values must be one of the options specified in the `enum` array.
    - **Object property validation** - Properties of objects must conform to their defined schemas.
    - **Array item validation** - Items in arrays must conform to the `items` schema.
    - **Logical composition** - Values must conform to at least one schema in the `anyOf` array.

    Testcases that fail validation will still be stored, but will include `validationErrors` detailing the issues.
    Extra fields in the Testcase data that are not in the schema will be stored but are ignored during validation.
    """
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
