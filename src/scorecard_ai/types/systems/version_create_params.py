# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["VersionCreateParams"]


class VersionCreateParams(TypedDict, total=False):
    config: Required[Dict[str, object]]
    """The configuration of the system version."""

    name: Required[str]
    """The name of the system version."""
