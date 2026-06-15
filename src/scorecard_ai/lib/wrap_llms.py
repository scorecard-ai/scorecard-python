"""Lazy entry points for tracing OpenAI and Anthropic SDK calls.

The tracing implementation relies on OpenTelemetry, which is an *optional*
dependency of this package. Importing ``scorecard_ai`` (and therefore this
module) must not require OpenTelemetry to be installed, so the heavy
implementation lives in :mod:`scorecard_ai.lib._wrap_llms_otel` and is imported
lazily the first time one of the public wrappers is called.

To use LLM tracing, install the optional ``otel`` extra::

    pip install 'scorecard-ai[otel]'
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar, Optional, cast

if TYPE_CHECKING:
    # Type-only re-export; importing the implementation at runtime would pull in
    # the optional OpenTelemetry dependency, which we deliberately defer.
    from ._wrap_llms_otel import WrapConfig as WrapConfig

__all__ = ["wrap", "wrap_openai", "wrap_anthropic"]

_ClientT = TypeVar("_ClientT")

_OTEL_MISSING_MESSAGE = (
    "Tracing LLM calls requires OpenTelemetry, which is an optional dependency "
    "of scorecard-ai. Install it with:\n\n"
    "    pip install 'scorecard-ai[otel]'\n"
)


def _load_impl() -> Any:
    """Import the OpenTelemetry-backed implementation, with a helpful error."""
    try:
        from . import _wrap_llms_otel
    except ImportError as exc:
        raise ImportError(_OTEL_MISSING_MESSAGE) from exc

    return _wrap_llms_otel


def wrap(client: _ClientT, config: Optional[WrapConfig] = None) -> _ClientT:
    """
    Wrap any LLM SDK (OpenAI or Anthropic) to automatically trace all API calls.

    Requires the optional ``otel`` extra (``pip install 'scorecard-ai[otel]'``).

    Args:
        client: An instance of OpenAI or Anthropic SDK client
        config: Optional configuration for tracing

    Returns:
        The wrapped client with automatic tracing enabled

    Example:
        >>> from scorecard_ai import wrap
        >>> from openai import OpenAI
        >>> from anthropic import Anthropic
        >>>
        >>> # Works with OpenAI
        >>> openai = wrap(OpenAI(api_key="..."), {
        ...     "api_key": os.getenv("SCORECARD_API_KEY"),
        ...     "project_id": "123"
        >>> })
        >>>
        >>> # Works with Anthropic
        >>> claude = wrap(Anthropic(api_key="..."), {
        ...     "api_key": os.getenv("SCORECARD_API_KEY"),
        ...     "project_id": "123"
        >>> })
        >>>
        >>> # Use normally - traces are automatically sent to Scorecard
        >>> response = openai.chat.completions.create(...)
        >>> response2 = claude.messages.create(...)
    """
    return cast(_ClientT, _load_impl().wrap(client, config))


# Backwards compatibility aliases
wrap_openai = wrap
wrap_anthropic = wrap
