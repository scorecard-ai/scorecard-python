# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RunUpdateResponse"]


class RunUpdateResponse(BaseModel):
    id: str
    """The ID of the Run."""

    status: Literal[
        "pending",
        "awaiting_execution",
        "running_execution",
        "awaiting_scoring",
        "running_scoring",
        "awaiting_human_scoring",
        "completed",
    ]
    """The status of the Run."""
