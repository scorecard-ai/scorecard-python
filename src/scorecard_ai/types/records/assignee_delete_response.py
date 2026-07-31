# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AssigneeDeleteResponse"]


class AssigneeDeleteResponse(BaseModel):
    deleted: float
    """The number of assignment rows removed (0 if the member was not assigned)."""
