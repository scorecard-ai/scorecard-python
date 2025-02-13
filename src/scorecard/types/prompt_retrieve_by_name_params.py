# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PromptRetrieveByNameParams"]


class PromptRetrieveByNameParams(TypedDict, total=False):
    name: Required[str]
    """Name of the prompt."""

    tag: str
    """Tag to select by. Defaults to selecting the production version"""
