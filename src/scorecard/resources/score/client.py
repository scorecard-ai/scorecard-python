# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.forbidden_error import ForbiddenError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.grade import Grade
from ...types.http_validation_error import HttpValidationError
from ...types.not_found_error_body import NotFoundErrorBody
from ...types.unauthenticated_error import UnauthenticatedError
from ...types.unauthorized_error_body import UnauthorizedErrorBody

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ScoreClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        run_id: int,
        testrecord_id: int,
        *,
        metric_id: int,
        int_score: typing.Optional[int] = OMIT,
        binary_score: typing.Optional[bool] = OMIT,
        reasoning: typing.Optional[str] = OMIT,
    ) -> Grade:
        """
        Create a score

        Parameters:
            - run_id: int.

            - testrecord_id: int.

            - metric_id: int.

            - int_score: typing.Optional[int].

            - binary_score: typing.Optional[bool].

            - reasoning: typing.Optional[str].
        ---
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.score.create(
            run_id=1,
            testrecord_id=1,
            metric_id=1,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"metric_id": metric_id}
        if int_score is not OMIT:
            _request["int_score"] = int_score
        if binary_score is not OMIT:
            _request["binary_score"] = binary_score
        if reasoning is not OMIT:
            _request["reasoning"] = reasoning
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/run/{run_id}/testrecord/{testrecord_id}/score"
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Grade, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthenticatedError, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        run_id: int,
        testrecord_id: int,
        score_id: int,
        *,
        int_score: typing.Optional[int] = OMIT,
        binary_score: typing.Optional[bool] = OMIT,
        reasoning: typing.Optional[str] = OMIT,
    ) -> Grade:
        """
        Update a score

        Parameters:
            - run_id: int.

            - testrecord_id: int.

            - score_id: int.

            - int_score: typing.Optional[int].

            - binary_score: typing.Optional[bool].

            - reasoning: typing.Optional[str].
        ---
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.score.update(
            run_id=1,
            testrecord_id=1,
            score_id=1,
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if int_score is not OMIT:
            _request["int_score"] = int_score
        if binary_score is not OMIT:
            _request["binary_score"] = binary_score
        if reasoning is not OMIT:
            _request["reasoning"] = reasoning
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"v1/run/{run_id}/testrecord/{testrecord_id}/score/{score_id}",
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Grade, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthenticatedError, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncScoreClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        run_id: int,
        testrecord_id: int,
        *,
        metric_id: int,
        int_score: typing.Optional[int] = OMIT,
        binary_score: typing.Optional[bool] = OMIT,
        reasoning: typing.Optional[str] = OMIT,
    ) -> Grade:
        """
        Create a score

        Parameters:
            - run_id: int.

            - testrecord_id: int.

            - metric_id: int.

            - int_score: typing.Optional[int].

            - binary_score: typing.Optional[bool].

            - reasoning: typing.Optional[str].
        ---
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.score.create(
            run_id=1,
            testrecord_id=1,
            metric_id=1,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"metric_id": metric_id}
        if int_score is not OMIT:
            _request["int_score"] = int_score
        if binary_score is not OMIT:
            _request["binary_score"] = binary_score
        if reasoning is not OMIT:
            _request["reasoning"] = reasoning
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/run/{run_id}/testrecord/{testrecord_id}/score"
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Grade, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthenticatedError, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        run_id: int,
        testrecord_id: int,
        score_id: int,
        *,
        int_score: typing.Optional[int] = OMIT,
        binary_score: typing.Optional[bool] = OMIT,
        reasoning: typing.Optional[str] = OMIT,
    ) -> Grade:
        """
        Update a score

        Parameters:
            - run_id: int.

            - testrecord_id: int.

            - score_id: int.

            - int_score: typing.Optional[int].

            - binary_score: typing.Optional[bool].

            - reasoning: typing.Optional[str].
        ---
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.score.update(
            run_id=1,
            testrecord_id=1,
            score_id=1,
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if int_score is not OMIT:
            _request["int_score"] = int_score
        if binary_score is not OMIT:
            _request["binary_score"] = binary_score
        if reasoning is not OMIT:
            _request["reasoning"] = reasoning
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"v1/run/{run_id}/testrecord/{testrecord_id}/score/{score_id}",
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Grade, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthenticatedError, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)