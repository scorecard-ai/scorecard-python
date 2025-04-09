# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .testcase import Testcase

__all__ = ["TestcaseCreateResponse"]


class TestcaseCreateResponse(BaseModel):
    __test__ = False
    items: List[Testcase]
