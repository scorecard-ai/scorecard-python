# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Prompt"]


class Prompt(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    is_archived: Optional[bool] = None

    merge_parent_id: Optional[str] = None

    api_model_params: Optional[Dict[str, Union[float, str]]] = FieldInfo(alias="model_params", default=None)

    name: Optional[str] = None

    org_id: Optional[str] = None
    """The organization this resource belongs to."""

    parent_id: Optional[str] = None

    project_id: Optional[int] = None
    """The ID of the project the prompt belongs to."""

    prompt_template: Optional[str] = None

    root_id: Optional[str] = None

    user_id: Optional[str] = None
    """The user this record belongs to."""
