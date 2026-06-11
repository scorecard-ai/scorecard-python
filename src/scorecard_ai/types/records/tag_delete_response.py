# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["TagDeleteResponse"]


class TagDeleteResponse(BaseModel):
    deleted: float
    """The number of tag rows removed (0 if the tag was not present)."""
