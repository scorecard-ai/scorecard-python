# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["TestcaseDeleteParams"]


class TestcaseDeleteParams(TypedDict, total=False):
    ids: Required[Iterable[int]]
    """IDs of testcases to delete (max 100)"""
