# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .systems.system_version import SystemVersion

__all__ = ["System", "Version"]


class Version(BaseModel):
    """A SystemVersion defines the specific settings for a System Under Test.

    System versions contain parameter values that determine system behavior during evaluation.
    They are immutable snapshots - once created, they never change.

    When running evaluations, you reference a specific systemVersionId to establish which system version to test.
    """

    id: str
    """The ID of the system version."""

    name: str
    """The name of the system version."""


class System(BaseModel):
    """A System Under Test (SUT).

    Systems are templates - to run evaluations, pair them with a SystemVersion that provides specific
    parameter values.
    """

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
