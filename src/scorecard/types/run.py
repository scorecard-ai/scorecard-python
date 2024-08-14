# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import datetime as dt
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Run(UncheckedBaseModel):
    id: typing.Optional[int] = None
    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The creation date and time of the run.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time the run was updated.
    """

    execution_start_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The start time of the run.
    """

    execution_end_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The end time of the run.
    """

    testset_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The testset that was executed in this run.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current status of the run.
    """

    limit_testcases: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of testcases to run.
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    How the run was created.
    """

    model_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    The model parameters used when generating the run.
    """

    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Notes about the run.
    """

    scoring_config_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the Scoring Config the run uses.
    """

    prompt_template: typing.Optional[str] = pydantic.Field(default=None)
    """
    The prompt template to be used while executing the run.
    """

    scoring_start_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The start time of scoring the run's results.
    """

    scoring_end_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The end time of scoring the run's results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
