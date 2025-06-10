# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Metric", "UnionMember0", "UnionMember1", "UnionMember2", "UnionMember3", "UnionMember4", "UnionMember5"]


class UnionMember0(BaseModel):
    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["ai"] = FieldInfo(alias="evalType")
    """AI-based evaluation type."""

    guidelines: Optional[str] = None
    """Guidelines for AI evaluation on how to score the metric."""

    api_model_name: str = FieldInfo(alias="modelName")
    """The AI model to use for evaluation."""

    name: str
    """The name of the Metric."""

    output_type: Literal["int"] = FieldInfo(alias="outputType")

    passing_threshold: int = FieldInfo(alias="passingThreshold")
    """The threshold for determining pass/fail from integer scores (1-5)."""

    prompt_template: str = FieldInfo(alias="promptTemplate")
    """The complete prompt template for AI evaluation.

    Should include placeholders for dynamic content.
    """

    temperature: float
    """The temperature for AI evaluation (0-2)."""


class UnionMember1(BaseModel):
    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["human"] = FieldInfo(alias="evalType")
    """Human-based evaluation type."""

    name: str
    """The name of the Metric."""

    output_type: Literal["int"] = FieldInfo(alias="outputType")

    passing_threshold: int = FieldInfo(alias="passingThreshold")
    """The threshold for determining pass/fail from integer scores (1-5)."""

    guidelines: Optional[str] = None
    """Guidelines for human evaluators."""


class UnionMember2(BaseModel):
    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["heuristic"] = FieldInfo(alias="evalType")
    """Heuristic-based evaluation type."""

    name: str
    """The name of the Metric."""

    output_type: Literal["int"] = FieldInfo(alias="outputType")

    passing_threshold: int = FieldInfo(alias="passingThreshold")
    """The threshold for determining pass/fail from integer scores (1-5)."""

    guidelines: Optional[str] = None
    """Optional guidelines for heuristic evaluation logic."""


class UnionMember3(BaseModel):
    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["ai"] = FieldInfo(alias="evalType")
    """AI-based evaluation type."""

    guidelines: Optional[str] = None
    """Guidelines for AI evaluation on how to score the metric."""

    api_model_name: str = FieldInfo(alias="modelName")
    """The AI model to use for evaluation."""

    name: str
    """The name of the Metric."""

    output_type: Literal["boolean"] = FieldInfo(alias="outputType")

    prompt_template: str = FieldInfo(alias="promptTemplate")
    """The complete prompt template for AI evaluation.

    Should include placeholders for dynamic content.
    """

    temperature: float
    """The temperature for AI evaluation (0-2)."""


class UnionMember4(BaseModel):
    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["human"] = FieldInfo(alias="evalType")
    """Human-based evaluation type."""

    name: str
    """The name of the Metric."""

    output_type: Literal["boolean"] = FieldInfo(alias="outputType")

    guidelines: Optional[str] = None
    """Guidelines for human evaluators."""


class UnionMember5(BaseModel):
    id: str
    """The ID of the Metric."""

    description: Optional[str] = None
    """The description of the Metric."""

    eval_type: Literal["heuristic"] = FieldInfo(alias="evalType")
    """Heuristic-based evaluation type."""

    name: str
    """The name of the Metric."""

    output_type: Literal["boolean"] = FieldInfo(alias="outputType")

    guidelines: Optional[str] = None
    """Optional guidelines for heuristic evaluation logic."""


Metric: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5]
