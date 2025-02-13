# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "Testrecord",
    "CustomInputs",
    "CustomInputsFileURL",
    "CustomInputsJsonObjectOutput",
    "CustomLabels",
    "CustomLabelsFileURL",
    "CustomLabelsJsonObjectOutput",
    "CustomOutputs",
    "CustomOutputsFileURL",
    "CustomOutputsJsonObjectOutput",
]


class CustomInputsFileURL(BaseModel):
    url: str

    name: Optional[str] = None


class CustomInputsJsonObjectOutput(BaseModel):
    value: Union[Dict[str, object], List[object], str, float, bool, None] = None
    """
    The value of the JSON object, which can be a dictionary, list, string, integer,
    float, boolean, or None.
    """


CustomInputs: TypeAlias = Union[str, CustomInputsFileURL, CustomInputsJsonObjectOutput]


class CustomLabelsFileURL(BaseModel):
    url: str

    name: Optional[str] = None


class CustomLabelsJsonObjectOutput(BaseModel):
    value: Union[Dict[str, object], List[object], str, float, bool, None] = None
    """
    The value of the JSON object, which can be a dictionary, list, string, integer,
    float, boolean, or None.
    """


CustomLabels: TypeAlias = Union[str, CustomLabelsFileURL, CustomLabelsJsonObjectOutput]


class CustomOutputsFileURL(BaseModel):
    url: str

    name: Optional[str] = None


class CustomOutputsJsonObjectOutput(BaseModel):
    value: Union[Dict[str, object], List[object], str, float, bool, None] = None
    """
    The value of the JSON object, which can be a dictionary, list, string, integer,
    float, boolean, or None.
    """


CustomOutputs: TypeAlias = Union[str, CustomOutputsFileURL, CustomOutputsJsonObjectOutput]


class Testrecord(BaseModel):
    __test__ = False
    id: Optional[int] = None

    context: Optional[str] = None
    """The context for the testrecord."""

    created_at: Optional[datetime] = None
    """The creation date and time of the testrecord."""

    custom_inputs: Optional[Dict[str, CustomInputs]] = None

    custom_labels: Optional[Dict[str, CustomLabels]] = None

    custom_outputs: Optional[Dict[str, CustomOutputs]] = None

    error_message: Optional[str] = None
    """The error message for the testrecord."""

    ideal: Optional[str] = None
    """The ideal response for the testrecord."""

    api_model_debug_info: Optional[Dict[str, Union[float, str]]] = FieldInfo(alias="model_debug_info", default=None)
    """Debug information produced during the testrecord's generation."""

    api_model_params: Optional[Dict[str, Union[float, str]]] = FieldInfo(alias="model_params", default=None)
    """The model parameters used when generating the testrecord."""

    api_model_response: Optional[str] = FieldInfo(alias="model_response", default=None)
    """The actual response of the model for the testrecord."""

    prompt: Optional[str] = None
    """The prompt used to generate the testrecord."""

    run_id: Optional[int] = None
    """The ID of the run the testrecord belongs to."""

    status: Optional[str] = None
    """The current status of the testrecord."""

    testcase_id: Optional[int] = None
    """The ID of the testcase the testrecord belongs to."""

    testset_id: Optional[int] = None
    """The ID of the testset the testrecord belongs to."""

    user_query: Optional[str] = None
    """The user query for the testrecord."""
