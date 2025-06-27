# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SystemVersion"]


class SystemVersion(BaseModel):
    id: str
    """The ID of the system version."""

    config: Dict[str, object]
    """The configuration of the system version."""

    name: str
    """The name of the system version."""

    system_id: str = FieldInfo(alias="systemId")
    """The ID of the system the system version belongs to."""
