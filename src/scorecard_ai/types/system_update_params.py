# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SystemUpdateParams"]


class SystemUpdateParams(TypedDict, total=False):
    config_schema: Annotated[Dict[str, object], PropertyInfo(alias="configSchema")]
    """The schema of the system's configuration."""

    description: str
    """The description of the system."""

    input_schema: Annotated[Dict[str, object], PropertyInfo(alias="inputSchema")]
    """The schema of the system's inputs."""

    name: str
    """The name of the system."""

    output_schema: Annotated[Dict[str, object], PropertyInfo(alias="outputSchema")]
    """The schema of the system's outputs."""
