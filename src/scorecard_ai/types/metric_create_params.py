# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MetricCreateParams",
    "AIIntMetric",
    "HumanIntMetric",
    "HeuristicIntMetric",
    "AIBooleanMetric",
    "HumanBooleanMetric",
    "HeuristicBooleanMetric",
]


class AIIntMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["ai"], PropertyInfo(alias="evalType")]]
    """AI-based evaluation type."""

    name: Required[str]
    """The name of the Metric."""

    output_type: Required[Annotated[Literal["int"], PropertyInfo(alias="outputType")]]
    """Integer output type."""

    prompt_template: Required[Annotated[str, PropertyInfo(alias="promptTemplate")]]
    """The complete prompt template for AI evaluation.

    Should include placeholders for dynamic content.
    """

    description: Optional[str]
    """The description of the Metric."""

    eval_model_name: Annotated[str, PropertyInfo(alias="evalModelName")]
    """The AI model to use for evaluation."""

    guidelines: Optional[str]
    """Guidelines for AI evaluation on how to score the metric."""

    passing_threshold: Annotated[int, PropertyInfo(alias="passingThreshold")]
    """The threshold for determining pass/fail from integer scores (1-5)."""

    temperature: float
    """The temperature for AI evaluation (0-2)."""


class HumanIntMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["human"], PropertyInfo(alias="evalType")]]
    """Human-based evaluation type."""

    name: Required[str]
    """The name of the Metric."""

    output_type: Required[Annotated[Literal["int"], PropertyInfo(alias="outputType")]]
    """Integer output type."""

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Guidelines for human evaluators."""

    passing_threshold: Annotated[int, PropertyInfo(alias="passingThreshold")]
    """The threshold for determining pass/fail from integer scores (1-5)."""


class HeuristicIntMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["heuristic"], PropertyInfo(alias="evalType")]]
    """Heuristic-based evaluation type."""

    name: Required[str]
    """The name of the Metric."""

    output_type: Required[Annotated[Literal["int"], PropertyInfo(alias="outputType")]]
    """Integer output type."""

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Optional guidelines for heuristic evaluation logic."""

    passing_threshold: Annotated[int, PropertyInfo(alias="passingThreshold")]
    """The threshold for determining pass/fail from integer scores (1-5)."""


class AIBooleanMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["ai"], PropertyInfo(alias="evalType")]]
    """AI-based evaluation type."""

    name: Required[str]
    """The name of the Metric."""

    output_type: Required[Annotated[Literal["boolean"], PropertyInfo(alias="outputType")]]
    """Boolean output type."""

    prompt_template: Required[Annotated[str, PropertyInfo(alias="promptTemplate")]]
    """The complete prompt template for AI evaluation.

    Should include placeholders for dynamic content.
    """

    description: Optional[str]
    """The description of the Metric."""

    eval_model_name: Annotated[str, PropertyInfo(alias="evalModelName")]
    """The AI model to use for evaluation."""

    guidelines: Optional[str]
    """Guidelines for AI evaluation on how to score the metric."""

    temperature: float
    """The temperature for AI evaluation (0-2)."""


class HumanBooleanMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["human"], PropertyInfo(alias="evalType")]]
    """Human-based evaluation type."""

    name: Required[str]
    """The name of the Metric."""

    output_type: Required[Annotated[Literal["boolean"], PropertyInfo(alias="outputType")]]
    """Boolean output type."""

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Guidelines for human evaluators."""


class HeuristicBooleanMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["heuristic"], PropertyInfo(alias="evalType")]]
    """Heuristic-based evaluation type."""

    name: Required[str]
    """The name of the Metric."""

    output_type: Required[Annotated[Literal["boolean"], PropertyInfo(alias="outputType")]]
    """Boolean output type."""

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Optional guidelines for heuristic evaluation logic."""


MetricCreateParams: TypeAlias = Union[
    AIIntMetric, HumanIntMetric, HeuristicIntMetric, AIBooleanMetric, HumanBooleanMetric, HeuristicBooleanMetric
]
