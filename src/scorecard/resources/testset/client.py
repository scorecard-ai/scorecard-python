# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.forbidden_error import ForbiddenError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.custom_schema import CustomSchema
from ...types.http_validation_error import HttpValidationError
from ...types.not_found_error_body import NotFoundErrorBody
from ...types.paginated_testcase_response import PaginatedTestcaseResponse
from ...types.testset import Testset
from ...types.unauthenticated_error import UnauthenticatedError
from ...types.unauthorized_error_body import UnauthorizedErrorBody

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TestsetClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, testset_id: int) -> Testset:
        """
        Retrieve Testset metadata without Testcase data

        Parameters:
            - testset_id: int.
        ---
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.testset.get(
            testset_id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/testset/{testset_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Testset, _response.json())  # type: ignore
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

    def delete(self, testset_id: int) -> Testset:
        """
        Delete a Testset

        Parameters:
            - testset_id: int.
        ---
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.testset.delete(
            testset_id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/testset/{testset_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Testset, _response.json())  # type: ignore
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

    def create(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        using_retrieval: typing.Optional[bool] = OMIT,
        custom_schema: typing.Optional[CustomSchema] = OMIT,
    ) -> Testset:
        """
        Create a new Testset

        Parameters:
            - name: str.

            - description: typing.Optional[str].

            - using_retrieval: typing.Optional[bool].

            - custom_schema: typing.Optional[CustomSchema].
        ---
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.testset.create(
            name="name",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"name": name}
        if description is not OMIT:
            _request["description"] = description
        if using_retrieval is not OMIT:
            _request["using_retrieval"] = using_retrieval
        if custom_schema is not OMIT:
            _request["custom_schema"] = custom_schema
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/testset"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Testset, _response.json())  # type: ignore
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

    def read_schema(self, testset_id: int) -> CustomSchema:
        """
        Read the schema of a Testset

        Parameters:
            - testset_id: int.
        ---
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.testset.read_schema(
            testset_id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/testset/{testset_id}/schema"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CustomSchema, _response.json())  # type: ignore
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

    def get_testcases(
        self, testset_id: int, *, offset: typing.Optional[int] = None, limit: typing.Optional[int] = None
    ) -> PaginatedTestcaseResponse:
        """
        Retrieve all Testcases from a Testset

        Parameters:
            - testset_id: int.

            - offset: typing.Optional[int].

            - limit: typing.Optional[int].
        ---
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.testset.get_testcases(
            testset_id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/testset/{testset_id}/testcase"),
            params=remove_none_from_dict({"offset": offset, "limit": limit}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedTestcaseResponse, _response.json())  # type: ignore
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


class AsyncTestsetClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, testset_id: int) -> Testset:
        """
        Retrieve Testset metadata without Testcase data

        Parameters:
            - testset_id: int.
        ---
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.testset.get(
            testset_id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/testset/{testset_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Testset, _response.json())  # type: ignore
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

    async def delete(self, testset_id: int) -> Testset:
        """
        Delete a Testset

        Parameters:
            - testset_id: int.
        ---
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.testset.delete(
            testset_id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/testset/{testset_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Testset, _response.json())  # type: ignore
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

    async def create(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        using_retrieval: typing.Optional[bool] = OMIT,
        custom_schema: typing.Optional[CustomSchema] = OMIT,
    ) -> Testset:
        """
        Create a new Testset

        Parameters:
            - name: str.

            - description: typing.Optional[str].

            - using_retrieval: typing.Optional[bool].

            - custom_schema: typing.Optional[CustomSchema].
        ---
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.testset.create(
            name="name",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"name": name}
        if description is not OMIT:
            _request["description"] = description
        if using_retrieval is not OMIT:
            _request["using_retrieval"] = using_retrieval
        if custom_schema is not OMIT:
            _request["custom_schema"] = custom_schema
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/testset"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Testset, _response.json())  # type: ignore
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

    async def read_schema(self, testset_id: int) -> CustomSchema:
        """
        Read the schema of a Testset

        Parameters:
            - testset_id: int.
        ---
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.testset.read_schema(
            testset_id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/testset/{testset_id}/schema"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CustomSchema, _response.json())  # type: ignore
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

    async def get_testcases(
        self, testset_id: int, *, offset: typing.Optional[int] = None, limit: typing.Optional[int] = None
    ) -> PaginatedTestcaseResponse:
        """
        Retrieve all Testcases from a Testset

        Parameters:
            - testset_id: int.

            - offset: typing.Optional[int].

            - limit: typing.Optional[int].
        ---
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.testset.get_testcases(
            testset_id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/testset/{testset_id}/testcase"),
            params=remove_none_from_dict({"offset": offset, "limit": limit}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedTestcaseResponse, _response.json())  # type: ignore
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
