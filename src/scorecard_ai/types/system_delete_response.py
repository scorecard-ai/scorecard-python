# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SystemDeleteResponse"]


class SystemDeleteResponse(BaseModel):
    success: bool
    """Whether the deletion was successful."""
