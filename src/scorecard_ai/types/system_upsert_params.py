# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["SystemUpsertParams"]


class SystemUpsertParams(TypedDict, total=False):
    config: Required[Dict[str, object]]
    """The configuration of the system."""

    description: str
    """The description of the system."""

    name: str
    """The name of the system.

    Should be unique within the project. Default is "Default system"
    """
