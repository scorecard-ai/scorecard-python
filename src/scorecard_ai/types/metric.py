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
    "AIBooleanMetric",
    "HumanBooleanMetric",
    "HeuristicBooleanMetric",
]


class AIIntMetric(BaseModel):
    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_model_name: str = FieldInfo(alias="evalModelName")
    """The AI model to use for evaluation."""

    eval_type: Literal["ai"] = FieldInfo(alias="evalType")
    """AI-based evaluation type."""

    guidelines: Optional[str] = None
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
    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["human"] = FieldInfo(alias="evalType")
    """Human-based evaluation type."""

    name: str
    """The name of the Metric."""

    output_type: Literal["int"] = FieldInfo(alias="outputType")
    """Integer output type."""

    passing_threshold: int = FieldInfo(alias="passingThreshold")
    """The threshold for determining pass/fail from integer scores (1-5)."""

    guidelines: Optional[str] = None
    """Guidelines for human evaluators."""


class HeuristicIntMetric(BaseModel):
    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["heuristic"] = FieldInfo(alias="evalType")
    """Heuristic-based evaluation type."""

    name: str
    """The name of the Metric."""

    output_type: Literal["int"] = FieldInfo(alias="outputType")
    """Integer output type."""

    passing_threshold: int = FieldInfo(alias="passingThreshold")
    """The threshold for determining pass/fail from integer scores (1-5)."""

    guidelines: Optional[str] = None
    """Optional guidelines for heuristic evaluation logic."""


class AIBooleanMetric(BaseModel):
    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_model_name: str = FieldInfo(alias="evalModelName")
    """The AI model to use for evaluation."""

    eval_type: Literal["ai"] = FieldInfo(alias="evalType")
    """AI-based evaluation type."""

    guidelines: Optional[str] = None
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
    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["human"] = FieldInfo(alias="evalType")
    """Human-based evaluation type."""

    name: str
    """The name of the Metric."""

    output_type: Literal["boolean"] = FieldInfo(alias="outputType")
    """Boolean output type."""

    guidelines: Optional[str] = None
    """Guidelines for human evaluators."""


class HeuristicBooleanMetric(BaseModel):
    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["heuristic"] = FieldInfo(alias="evalType")
    """Heuristic-based evaluation type."""

    name: str
    """The name of the Metric."""

    output_type: Literal["boolean"] = FieldInfo(alias="outputType")
    """Boolean output type."""

    guidelines: Optional[str] = None
    """Optional guidelines for heuristic evaluation logic."""


Metric: TypeAlias = Union[
    AIIntMetric, HumanIntMetric, HeuristicIntMetric, AIBooleanMetric, HumanBooleanMetric, HeuristicBooleanMetric
]
