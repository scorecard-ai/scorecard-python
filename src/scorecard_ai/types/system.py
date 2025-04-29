# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["System"]


class System(BaseModel):
    id: str
    """The ID of the system."""

    config_schema: Dict[str, object] = FieldInfo(alias="configSchema")
    """The schema of the system's configuration."""

    description: str
    """The description of the system."""

    input_schema: Dict[str, object] = FieldInfo(alias="inputSchema")
    """The schema of the system's inputs."""

    name: str
    """The name of the system."""

    output_schema: Dict[str, object] = FieldInfo(alias="outputSchema")
    """The schema of the system's outputs."""
