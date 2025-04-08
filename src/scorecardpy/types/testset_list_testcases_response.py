# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.testcase import Testcase

__all__ = ["TestsetListTestcasesResponse"]


class TestsetListTestcasesResponse(BaseModel):
    __test__ = False
    data: List[Testcase]

    has_more: bool = FieldInfo(alias="hasMore")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)

    total: Optional[int] = None
