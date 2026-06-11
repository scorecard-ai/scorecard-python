# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TagCreateParams"]


class TagCreateParams(TypedDict, total=False):
    text: Required[str]
    """The tag text to apply. Idempotent: re-applying an existing tag is a no-op."""
