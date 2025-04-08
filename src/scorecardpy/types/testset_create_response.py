# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TestsetCreateResponse", "FieldMapping"]


class FieldMapping(BaseModel):
    inputs: List[str]
    """Fields that represent inputs to the AI system"""

    labels: List[str]
    """Fields that represent expected outputs/labels"""

    metadata: List[str]
    """Fields that are not inputs or labels"""


class TestsetCreateResponse(BaseModel):
    __test__ = False
    id: int
    """The ID of the testset"""

    description: str
    """The description of the testset"""

    field_mapping: FieldMapping = FieldInfo(alias="fieldMapping")
    """Maps top-level keys of the testcase schema to their roles (input/label).

    Unmapped fields are treated as metadata.
    """

    name: str
    """The name of the testset"""

    schema_: object = FieldInfo(alias="schema")
