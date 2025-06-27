# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SystemUpdateParams"]


class SystemUpdateParams(TypedDict, total=False):
    description: str
    """The description of the system."""

    name: str
    """The name of the system. Unique within the project."""

    production_version_id: Annotated[str, PropertyInfo(alias="productionVersionId")]
    """The ID of the production version of the system."""
