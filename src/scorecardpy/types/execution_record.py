# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExecutionRecord"]


class ExecutionRecord(BaseModel):
    id: str
    """The ID of the execution record"""

    inputs: Dict[str, object]
    """
    The actual inputs sent to the system, which should match the system's input
    schema
    """

    labels: Dict[str, object]
    """The expected outputs for the testcase"""

    outputs: Dict[str, object]
    """The actual outputs from the system"""

    run_id: str = FieldInfo(alias="runId")
    """The ID of the run containing this execution record"""

    testcase_id: Optional[str] = FieldInfo(alias="testcaseId", default=None)
    """The ID of the testcase"""
