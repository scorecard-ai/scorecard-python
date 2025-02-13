# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TestsetCreateParams", "CustomSchema", "CustomSchemaVariable"]


class TestsetCreateParams(TypedDict, total=False):
    name: Required[str]

    created_by_playground: Optional[bool]
    """Whether or not the testset was created by the playground."""

    custom_schema: Optional[CustomSchema]
    """Custom schema model with an ordered list of custom variables."""

    description: Optional[str]
    """A description for the testset."""

    ingestion_method: Optional[Literal["csv", "logging"]]
    """The method of ingestion for the testset."""

    project_id: Optional[int]
    """The ID of the project to create the testset in.

    Omitting this optional argument will create the testset inside your
    Organization's default project.
    """

    published: Optional[bool]
    """Whether or not the testset is published."""

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
