# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ..core.unchecked_base_model import UncheckedBaseModel
from .score_status import ScoreStatus


class Grade(UncheckedBaseModel):
    user_id: typing.Optional[str] = None
    id: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The ID of the grade.
    """

    run_id: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The ID of the run that created the grade.
    """

    testcase_id: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The ID of the testcase associated with the grade.
    """

    testrecord_id: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The ID of the testrecord for which the grade was created.
    """

    metric_id: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The ID of the metric used to compute the grade.
    """

    binary_score: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    The binary score assigned to the grade.
    """

    int_score: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The integer score assigned to the grade.
    """

    reasoning: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The reasoning for the assigned score.
    """

    human_eval: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Indicates if a human should assign a grade.
    """

    status: typing.Optional[ScoreStatus] = pydantic_v1.Field(default=None)
    """
    The status of the grade.
    """

    error_message: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The error message if the grade was not created successfully.
    """

    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    when the grade was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    when the grade was last updated.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
