# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Testset", "CustomSchema", "CustomSchemaVariable"]


class CustomSchemaVariable(BaseModel):
    data_type: Literal["text", "file_url", "json_object"]
    """Enum for data types."""

    name: str

    role: Literal["input", "output", "label", "metadata"]
    """Enum for role types."""

    description: Optional[str] = None


class CustomSchema(BaseModel):
    variables: Optional[List[CustomSchemaVariable]] = None
    """Ordered list of custom variables"""


class Testset(BaseModel):
    __test__ = False
    id: Optional[int] = None
    """The ID of the testset."""

    created_at: Optional[datetime] = None
    """The creation date and time of the testset."""

    created_by_playground: Optional[bool] = None
    """Whether or not the testset was created by the playground."""

    custom_schema: Optional[CustomSchema] = None
    """Custom schema model with an ordered list of custom variables."""

    description: Optional[str] = None
    """A description for the testset."""

    ingestion_method: Optional[str] = None
    """The method used to ingest the testset."""

    is_archived: Optional[bool] = None
    """Whether or not the testset is archived."""

    name: Optional[str] = None
    """A human-readable name for the testset. This will be displayed in the UI."""

    num_testcases: Optional[int] = None
    """The number of testcases in the testset."""

    project_id: Optional[int] = None
    """The ID of the project the testset belongs to."""

    published: Optional[bool] = None
    """Whether or not the testset is published."""

    updated_at: Optional[datetime] = None
    """The last time the testset was updated."""

    using_retrieval: Optional[bool] = None
    """Whether or not the testset uses retrieval."""
