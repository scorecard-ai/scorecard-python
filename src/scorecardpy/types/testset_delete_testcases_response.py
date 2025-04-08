# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TestsetDeleteTestcasesResponse", "Error"]


class Error(BaseModel):
    id: int
    """ID of the testcase that failed to be deleted"""

    message: str
    """Error message explaining why the deletion failed"""


class TestsetDeleteTestcasesResponse(BaseModel):
    __test__ = False
    deleted_count: int = FieldInfo(alias="deletedCount")
    """Number of testcases successfully deleted"""

    errors: List[Error]
    """List of errors encountered during deletion, if any"""
