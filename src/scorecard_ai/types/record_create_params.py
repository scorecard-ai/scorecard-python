# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RecordCreateParams"]


class RecordCreateParams(TypedDict, total=False):
    expected: Required[Dict[str, object]]
    """The expected outputs for the Testcase."""

    inputs: Required[Dict[str, object]]
    """
    The actual inputs sent to the system, which should match the system's input
    schema.
    """

    outputs: Required[Dict[str, object]]
    """The actual outputs from the system."""

    testcase_id: Annotated[str, PropertyInfo(alias="testcaseId")]
    """The ID of the Testcase."""
