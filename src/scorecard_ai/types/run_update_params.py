# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RunUpdateParams"]


class RunUpdateParams(TypedDict, total=False):
    status: Required[
        Literal[
            "pending",
            "awaiting_execution",
            "running_execution",
            "awaiting_scoring",
            "running_scoring",
            "awaiting_human_scoring",
            "completed",
        ]
    ]
    """The status of the Run."""
