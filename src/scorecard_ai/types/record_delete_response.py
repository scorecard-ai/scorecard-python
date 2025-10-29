# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["RecordDeleteResponse"]


class RecordDeleteResponse(BaseModel):
    success: bool
    """Whether the deletion was successful."""
