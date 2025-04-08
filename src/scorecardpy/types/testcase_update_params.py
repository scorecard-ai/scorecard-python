# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["TestcaseUpdateParams"]


class TestcaseUpdateParams(TypedDict, total=False):
    data: Required[Dict[str, Dict[str, object]]]
    """The JSON data of the testcase, which is validated against the testset's schema."""
