# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AttachmentDeleteResponse"]


class AttachmentDeleteResponse(BaseModel):
    success: bool
    """Whether the deletion was successful."""
