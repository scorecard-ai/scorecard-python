# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import pydantic_v1
from ..core.unchecked_base_model import UncheckedBaseModel
from .prompt_model_params_value import PromptModelParamsValue


class Prompt(UncheckedBaseModel):
    org_id: typing.Optional[str] = None
    user_id: typing.Optional[str] = None
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    is_archived: typing.Optional[bool] = None
    prompt_template: typing.Optional[str] = None
    model_params: typing.Optional[typing.Dict[str, typing.Optional[PromptModelParamsValue]]] = None
    root_id: typing.Optional[str] = None
    parent_id: typing.Optional[str] = None
    merge_parent_id: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}