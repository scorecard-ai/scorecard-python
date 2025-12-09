# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["APIError"]


class APIError(BaseModel):
    """An API error."""

    code: str

    details: Dict[str, object]

    message: str
