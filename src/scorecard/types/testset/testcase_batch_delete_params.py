# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["TestcaseBatchDeleteParams"]


class TestcaseBatchDeleteParams(TypedDict, total=False):
    ids: Iterable[int]
    """List of Testcase IDs to delete."""
