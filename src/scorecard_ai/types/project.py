# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    id: str
    """The ID of the Project."""

    description: Optional[str] = None
    """The description of the Project."""

    name: Optional[str] = None
    """The name of the Project."""
