# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TestsetGetSchemaResponse", "Variable"]


class Variable(BaseModel):
    data_type: Literal["text", "file_url", "json_object"]
    """Enum for data types."""

    name: str

    role: Literal["input", "output", "label", "metadata"]
    """Enum for role types."""

    description: Optional[str] = None


class TestsetGetSchemaResponse(BaseModel):
    __test__ = False
    variables: Optional[List[Variable]] = None
    """Ordered list of custom variables"""
