# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .testcase import Testcase

__all__ = ["TestsetCreateTestcasesResponse"]


class TestsetCreateTestcasesResponse(BaseModel):
    __test__ = False
    items: List[Testcase]
