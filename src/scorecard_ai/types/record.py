# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Record"]


class Record(BaseModel):
    id: str
    """The ID of the Record."""

    expected: Dict[str, object]
    """The expected outputs for the Testcase."""

    inputs: Dict[str, object]
    """
    The actual inputs sent to the system, which should match the system's input
    schema.
    """

    outputs: Dict[str, object]
    """The actual outputs from the system."""

    run_id: str = FieldInfo(alias="runId")
    """The ID of the Run containing this Record."""

    testcase_id: Optional[str] = FieldInfo(alias="testcaseId", default=None)
    """The ID of the Testcase."""
