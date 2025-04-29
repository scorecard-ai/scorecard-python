# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TestcaseUpdateParams"]


class TestcaseUpdateParams(TypedDict, total=False):
    json_data: Required[Annotated[Dict[str, object], PropertyInfo(alias="jsonData")]]
    """The JSON data of the Testcase, which is validated against the Testset's schema."""
