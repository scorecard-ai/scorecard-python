# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PromptCreateParams"]


class PromptCreateParams(TypedDict, total=False):
    prompt_template: Required[str]

    description: Optional[str]

    is_prod: Optional[bool]

    model_params: Optional[Dict[str, Union[float, str, bool]]]

    name: Optional[str]

    parent_id: Optional[str]

    project_id: Optional[int]

    tag: Optional[str]
