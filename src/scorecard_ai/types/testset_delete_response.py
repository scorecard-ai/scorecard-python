# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TestsetDeleteResponse"]


class TestsetDeleteResponse(BaseModel):
    __test__ = False
    success: bool
    """Whether the deletion was successful."""
