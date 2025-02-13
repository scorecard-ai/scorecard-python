# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["TestcaseDeleteResponse"]


class TestcaseDeleteResponse(BaseModel):
    __test__ = False
    id: int
    """The ID of the testcase that was deleted."""

    detail: str
    """The message indicating the testcase was deleted."""
