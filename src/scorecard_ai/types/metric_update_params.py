# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MetricUpdateParams",
    "AIIntMetric",
    "HumanIntMetric",
    "HeuristicIntMetric",
    "AIFloatMetric",
    "HumanFloatMetric",
    "HeuristicFloatMetric",
    "AIBooleanMetric",
    "HumanBooleanMetric",
    "HeuristicBooleanMetric",
]


class AIIntMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["ai"], PropertyInfo(alias="evalType")]]
    """AI-based evaluation type."""

    output_type: Required[Annotated[Literal["int"], PropertyInfo(alias="outputType")]]
    """Integer output type."""

    description: Optional[str]
    """The description of the Metric."""

    eval_model_name: Annotated[str, PropertyInfo(alias="evalModelName")]
    """The AI model to use for evaluation."""

    guidelines: str
    """Guidelines for AI evaluation on how to score the metric."""

    name: str
    """The name of the Metric."""

    passing_threshold: Annotated[int, PropertyInfo(alias="passingThreshold")]
    """The threshold for determining pass/fail from integer scores (1-5)."""

    prompt_template: Annotated[str, PropertyInfo(alias="promptTemplate")]
    """The complete prompt template for AI evaluation.

    Should include placeholders for dynamic content.
    """

    temperature: float
    """The temperature for AI evaluation (0-2)."""


class HumanIntMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["human"], PropertyInfo(alias="evalType")]]
    """Human-based evaluation type."""

    output_type: Required[Annotated[Literal["int"], PropertyInfo(alias="outputType")]]
    """Integer output type."""

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Guidelines for human evaluators."""

    name: str
    """The name of the Metric."""

    passing_threshold: Annotated[int, PropertyInfo(alias="passingThreshold")]
    """The threshold for determining pass/fail from integer scores (1-5)."""


class HeuristicIntMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["heuristic"], PropertyInfo(alias="evalType")]]
    """Heuristic-based evaluation type."""

    output_type: Required[Annotated[Literal["int"], PropertyInfo(alias="outputType")]]
    """Integer output type."""

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Guidelines for heuristic evaluation logic."""

    name: str
    """The name of the Metric."""

    passing_threshold: Annotated[int, PropertyInfo(alias="passingThreshold")]
    """The threshold for determining pass/fail from integer scores (1-5)."""


class AIFloatMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["ai"], PropertyInfo(alias="evalType")]]
    """AI-based evaluation type."""

    output_type: Required[Annotated[Literal["float"], PropertyInfo(alias="outputType")]]
    """Float output type (0-1)."""

    description: Optional[str]
    """The description of the Metric."""

    eval_model_name: Annotated[str, PropertyInfo(alias="evalModelName")]
    """The AI model to use for evaluation."""

    guidelines: str
    """Guidelines for AI evaluation on how to score the metric."""

    name: str
    """The name of the Metric."""

    passing_threshold: Annotated[float, PropertyInfo(alias="passingThreshold")]
    """Threshold for determining pass/fail from float scores (0.0-1.0)."""

    prompt_template: Annotated[str, PropertyInfo(alias="promptTemplate")]
    """The complete prompt template for AI evaluation.

    Should include placeholders for dynamic content.
    """

    temperature: float
    """The temperature for AI evaluation (0-2)."""


class HumanFloatMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["human"], PropertyInfo(alias="evalType")]]
    """Human-based evaluation type."""

    output_type: Required[Annotated[Literal["float"], PropertyInfo(alias="outputType")]]
    """Float output type (0-1)."""

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Guidelines for human evaluators."""

    name: str
    """The name of the Metric."""

    passing_threshold: Annotated[float, PropertyInfo(alias="passingThreshold")]
    """Threshold for determining pass/fail from float scores (0.0-1.0)."""


class HeuristicFloatMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["heuristic"], PropertyInfo(alias="evalType")]]
    """Heuristic-based evaluation type."""

    output_type: Required[Annotated[Literal["float"], PropertyInfo(alias="outputType")]]
    """Float output type (0-1)."""

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Guidelines for heuristic evaluation logic."""

    name: str
    """The name of the Metric."""

    passing_threshold: Annotated[float, PropertyInfo(alias="passingThreshold")]
    """Threshold for determining pass/fail from float scores (0.0-1.0)."""


class AIBooleanMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["ai"], PropertyInfo(alias="evalType")]]
    """AI-based evaluation type."""

    output_type: Required[Annotated[Literal["boolean"], PropertyInfo(alias="outputType")]]
    """Boolean output type."""

    description: Optional[str]
    """The description of the Metric."""

    eval_model_name: Annotated[str, PropertyInfo(alias="evalModelName")]
    """The AI model to use for evaluation."""

    guidelines: str
    """Guidelines for AI evaluation on how to score the metric."""

    name: str
    """The name of the Metric."""

    prompt_template: Annotated[str, PropertyInfo(alias="promptTemplate")]
    """The complete prompt template for AI evaluation.

    Should include placeholders for dynamic content.
    """

    temperature: float
    """The temperature for AI evaluation (0-2)."""


class HumanBooleanMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["human"], PropertyInfo(alias="evalType")]]
    """Human-based evaluation type."""

    output_type: Required[Annotated[Literal["boolean"], PropertyInfo(alias="outputType")]]
    """Boolean output type."""

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Guidelines for human evaluators."""

    name: str
    """The name of the Metric."""


class HeuristicBooleanMetric(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["heuristic"], PropertyInfo(alias="evalType")]]
    """Heuristic-based evaluation type."""

    output_type: Required[Annotated[Literal["boolean"], PropertyInfo(alias="outputType")]]
    """Boolean output type."""

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Guidelines for heuristic evaluation logic."""

    name: str
    """The name of the Metric."""


MetricUpdateParams: TypeAlias = Union[
    AIIntMetric,
    HumanIntMetric,
    HeuristicIntMetric,
    AIFloatMetric,
    HumanFloatMetric,
    HeuristicFloatMetric,
    AIBooleanMetric,
    HumanBooleanMetric,
    HeuristicBooleanMetric,
]
