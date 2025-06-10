# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["MetricCreateParams", "Variant0", "Variant1", "Variant2", "Variant3", "Variant4", "Variant5"]


class Variant0(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["ai"], PropertyInfo(alias="evalType")]]
    """AI-based evaluation type."""

    name: Required[str]
    """The name of the Metric."""

    output_type: Required[Annotated[Literal["int"], PropertyInfo(alias="outputType")]]

    prompt_template: Required[Annotated[str, PropertyInfo(alias="promptTemplate")]]
    """The complete prompt template for AI evaluation.

    Should include placeholders for dynamic content.
    """

    description: Optional[str]
    """The description of the Metric."""

    guidelines: Optional[str]
    """Guidelines for AI evaluation on how to score the metric."""

    model_name: Annotated[str, PropertyInfo(alias="modelName")]
    """The AI model to use for evaluation."""

    passing_threshold: Annotated[int, PropertyInfo(alias="passingThreshold")]
    """The threshold for determining pass/fail from integer scores (1-5)."""

    temperature: float
    """The temperature for AI evaluation (0-2)."""


class Variant1(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["human"], PropertyInfo(alias="evalType")]]
    """Human-based evaluation type."""

    name: Required[str]
    """The name of the Metric."""

    output_type: Required[Annotated[Literal["int"], PropertyInfo(alias="outputType")]]

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Guidelines for human evaluators."""

    passing_threshold: Annotated[int, PropertyInfo(alias="passingThreshold")]
    """The threshold for determining pass/fail from integer scores (1-5)."""


class Variant2(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["heuristic"], PropertyInfo(alias="evalType")]]
    """Heuristic-based evaluation type."""

    name: Required[str]
    """The name of the Metric."""

    output_type: Required[Annotated[Literal["int"], PropertyInfo(alias="outputType")]]

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Optional guidelines for heuristic evaluation logic."""

    passing_threshold: Annotated[int, PropertyInfo(alias="passingThreshold")]
    """The threshold for determining pass/fail from integer scores (1-5)."""


class Variant3(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["ai"], PropertyInfo(alias="evalType")]]
    """AI-based evaluation type."""

    name: Required[str]
    """The name of the Metric."""

    output_type: Required[Annotated[Literal["boolean"], PropertyInfo(alias="outputType")]]

    prompt_template: Required[Annotated[str, PropertyInfo(alias="promptTemplate")]]
    """The complete prompt template for AI evaluation.

    Should include placeholders for dynamic content.
    """

    description: Optional[str]
    """The description of the Metric."""

    guidelines: Optional[str]
    """Guidelines for AI evaluation on how to score the metric."""

    model_name: Annotated[str, PropertyInfo(alias="modelName")]
    """The AI model to use for evaluation."""

    temperature: float
    """The temperature for AI evaluation (0-2)."""


class Variant4(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["human"], PropertyInfo(alias="evalType")]]
    """Human-based evaluation type."""

    name: Required[str]
    """The name of the Metric."""

    output_type: Required[Annotated[Literal["boolean"], PropertyInfo(alias="outputType")]]

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Guidelines for human evaluators."""


class Variant5(TypedDict, total=False):
    eval_type: Required[Annotated[Literal["heuristic"], PropertyInfo(alias="evalType")]]
    """Heuristic-based evaluation type."""

    name: Required[str]
    """The name of the Metric."""

    output_type: Required[Annotated[Literal["boolean"], PropertyInfo(alias="outputType")]]

    description: Optional[str]
    """The description of the Metric."""

    guidelines: str
    """Optional guidelines for heuristic evaluation logic."""


MetricCreateParams: TypeAlias = Union[Variant0, Variant1, Variant2, Variant3, Variant4, Variant5]
