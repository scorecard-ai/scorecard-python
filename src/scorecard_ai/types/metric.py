# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Metric",
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


class AIIntMetric(BaseModel):
    """A Metric with AI evaluation and integer output."""

    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_model_name: str = FieldInfo(alias="evalModelName")
    """The AI model to use for evaluation."""

    eval_type: Literal["ai"] = FieldInfo(alias="evalType")
    """AI-based evaluation type."""

    guidelines: str
    """Guidelines for AI evaluation on how to score the metric."""

    name: str
    """The name of the Metric."""

    output_type: Literal["int"] = FieldInfo(alias="outputType")
    """Integer output type."""

    passing_threshold: int = FieldInfo(alias="passingThreshold")
    """The threshold for determining pass/fail from integer scores (1-5)."""

    prompt_template: str = FieldInfo(alias="promptTemplate")
    """The complete prompt template for AI evaluation.

    Should include placeholders for dynamic content.
    """

    temperature: float
    """The temperature for AI evaluation (0-2)."""


class HumanIntMetric(BaseModel):
    """A Metric with human evaluation and integer output."""

    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["human"] = FieldInfo(alias="evalType")
    """Human-based evaluation type."""

    guidelines: str
    """Guidelines for human evaluators."""

    name: str
    """The name of the Metric."""

    output_type: Literal["int"] = FieldInfo(alias="outputType")
    """Integer output type."""

    passing_threshold: int = FieldInfo(alias="passingThreshold")
    """The threshold for determining pass/fail from integer scores (1-5)."""


class HeuristicIntMetric(BaseModel):
    """A Metric with heuristic evaluation and integer output."""

    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["heuristic"] = FieldInfo(alias="evalType")
    """Heuristic-based evaluation type."""

    guidelines: str
    """Guidelines for heuristic evaluation logic."""

    name: str
    """The name of the Metric."""

    output_type: Literal["int"] = FieldInfo(alias="outputType")
    """Integer output type."""

    passing_threshold: int = FieldInfo(alias="passingThreshold")
    """The threshold for determining pass/fail from integer scores (1-5)."""


class AIFloatMetric(BaseModel):
    """A Metric with AI evaluation and float output."""

    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_model_name: str = FieldInfo(alias="evalModelName")
    """The AI model to use for evaluation."""

    eval_type: Literal["ai"] = FieldInfo(alias="evalType")
    """AI-based evaluation type."""

    guidelines: str
    """Guidelines for AI evaluation on how to score the metric."""

    name: str
    """The name of the Metric."""

    output_type: Literal["float"] = FieldInfo(alias="outputType")
    """Float output type (0-1)."""

    passing_threshold: float = FieldInfo(alias="passingThreshold")
    """Threshold for determining pass/fail from float scores (0.0-1.0)."""

    prompt_template: str = FieldInfo(alias="promptTemplate")
    """The complete prompt template for AI evaluation.

    Should include placeholders for dynamic content.
    """

    temperature: float
    """The temperature for AI evaluation (0-2)."""


class HumanFloatMetric(BaseModel):
    """A Metric with human evaluation and float output."""

    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["human"] = FieldInfo(alias="evalType")
    """Human-based evaluation type."""

    guidelines: str
    """Guidelines for human evaluators."""

    name: str
    """The name of the Metric."""

    output_type: Literal["float"] = FieldInfo(alias="outputType")
    """Float output type (0-1)."""

    passing_threshold: float = FieldInfo(alias="passingThreshold")
    """Threshold for determining pass/fail from float scores (0.0-1.0)."""


class HeuristicFloatMetric(BaseModel):
    """A Metric with heuristic evaluation and float output."""

    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["heuristic"] = FieldInfo(alias="evalType")
    """Heuristic-based evaluation type."""

    guidelines: str
    """Guidelines for heuristic evaluation logic."""

    name: str
    """The name of the Metric."""

    output_type: Literal["float"] = FieldInfo(alias="outputType")
    """Float output type (0-1)."""

    passing_threshold: float = FieldInfo(alias="passingThreshold")
    """Threshold for determining pass/fail from float scores (0.0-1.0)."""


class AIBooleanMetric(BaseModel):
    """A Metric with AI evaluation and boolean output."""

    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_model_name: str = FieldInfo(alias="evalModelName")
    """The AI model to use for evaluation."""

    eval_type: Literal["ai"] = FieldInfo(alias="evalType")
    """AI-based evaluation type."""

    guidelines: str
    """Guidelines for AI evaluation on how to score the metric."""

    name: str
    """The name of the Metric."""

    output_type: Literal["boolean"] = FieldInfo(alias="outputType")
    """Boolean output type."""

    prompt_template: str = FieldInfo(alias="promptTemplate")
    """The complete prompt template for AI evaluation.

    Should include placeholders for dynamic content.
    """

    temperature: float
    """The temperature for AI evaluation (0-2)."""


class HumanBooleanMetric(BaseModel):
    """A Metric with human evaluation and boolean output."""

    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["human"] = FieldInfo(alias="evalType")
    """Human-based evaluation type."""

    guidelines: str
    """Guidelines for human evaluators."""

    name: str
    """The name of the Metric."""

    output_type: Literal["boolean"] = FieldInfo(alias="outputType")
    """Boolean output type."""


class HeuristicBooleanMetric(BaseModel):
    """A Metric with heuristic evaluation and boolean output."""

    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["heuristic"] = FieldInfo(alias="evalType")
    """Heuristic-based evaluation type."""

    guidelines: str
    """Guidelines for heuristic evaluation logic."""

    name: str
    """The name of the Metric."""

    output_type: Literal["boolean"] = FieldInfo(alias="outputType")
    """Boolean output type."""


Metric: TypeAlias = Union[
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
