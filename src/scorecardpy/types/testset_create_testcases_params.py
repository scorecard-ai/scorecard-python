# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["TestsetCreateTestcasesParams", "Item"]


class TestsetCreateTestcasesParams(TypedDict, total=False):
    items: Required[Iterable[Item]]
    """Testcases to create (max 100)"""


class Item(TypedDict, total=False):
    data: Required[Dict[str, object]]
    """The JSON data of the testcase, which is validated against the testset's schema."""
