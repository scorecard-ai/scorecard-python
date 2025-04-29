# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TestcaseDeleteResponse"]


class TestcaseDeleteResponse(BaseModel):
    __test__ = False
    success: bool
    """Whether the deletion was successful."""
