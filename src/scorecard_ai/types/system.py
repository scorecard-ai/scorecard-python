# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .systems.system_version import SystemVersion

__all__ = ["System", "Version"]


class Version(BaseModel):
    id: str
    """The ID of the system version."""

    name: str
    """The name of the system version."""


class System(BaseModel):
    id: str
    """The ID of the system."""

    description: str
    """The description of the system."""

    name: str
    """The name of the system. Unique within the project."""

    production_version: SystemVersion = FieldInfo(alias="productionVersion")
    """The production version of the system."""

    versions: List[Version]
    """The versions of the system."""
