# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import runs, scores, metrics, records, projects, testsets, testcases
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ScorecardError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.systems import systems

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Scorecard",
    "AsyncScorecard",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api2.scorecard.io/api/v2",
    "staging": "https://staging.api2.scorecard.io/api/v2",
    "local": "http://localhost:3000/api/v2",
}

class HasBaseAppURL():
    """
    This class is used to add the base app URL to the sync and async clients.
    """
    _base_url: httpx.URL

    @property
    def base_app_url(self) -> str:
        """Returns the base URL for the Scorecard app."""
        base_url = str(self._base_url).rstrip('/')
        if base_url == ENVIRONMENTS["production"]:
            return "https://app.scorecard.io"
        elif base_url == ENVIRONMENTS["staging"]:
            return "https://staging.app.getscorecard.ai"
        elif base_url == ENVIRONMENTS["local"]:
            return "http://localhost:3002"
        else:
            return "https://staging.app.getscorecard.ai"

class Scorecard(HasBaseAppURL, SyncAPIClient):
    projects: projects.ProjectsResource
    testsets: testsets.TestsetsResource
    testcases: testcases.TestcasesResource
    runs: runs.RunsResource
    metrics: metrics.MetricsResource
    records: records.RecordsResource
    scores: scores.ScoresResource
    systems: systems.SystemsResource
    with_raw_response: ScorecardWithRawResponse
    with_streaming_response: ScorecardWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Scorecard client instance.

        This automatically infers the `api_key` argument from the `SCORECARD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("SCORECARD_API_KEY")
        if api_key is None:
            raise ScorecardError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SCORECARD_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("SCORECARD_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `SCORECARD_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.projects = projects.ProjectsResource(self)
        self.testsets = testsets.TestsetsResource(self)
        self.testcases = testcases.TestcasesResource(self)
        self.runs = runs.RunsResource(self)
        self.metrics = metrics.MetricsResource(self)
        self.records = records.RecordsResource(self)
        self.scores = scores.ScoresResource(self)
        self.systems = systems.SystemsResource(self)
        self.with_raw_response = ScorecardWithRawResponse(self)
        self.with_streaming_response = ScorecardWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncScorecard(HasBaseAppURL, AsyncAPIClient):
    projects: projects.AsyncProjectsResource
    testsets: testsets.AsyncTestsetsResource
    testcases: testcases.AsyncTestcasesResource
    runs: runs.AsyncRunsResource
    metrics: metrics.AsyncMetricsResource
    records: records.AsyncRecordsResource
    scores: scores.AsyncScoresResource
    systems: systems.AsyncSystemsResource
    with_raw_response: AsyncScorecardWithRawResponse
    with_streaming_response: AsyncScorecardWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncScorecard client instance.

        This automatically infers the `api_key` argument from the `SCORECARD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("SCORECARD_API_KEY")
        if api_key is None:
            raise ScorecardError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SCORECARD_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("SCORECARD_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `SCORECARD_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.projects = projects.AsyncProjectsResource(self)
        self.testsets = testsets.AsyncTestsetsResource(self)
        self.testcases = testcases.AsyncTestcasesResource(self)
        self.runs = runs.AsyncRunsResource(self)
        self.metrics = metrics.AsyncMetricsResource(self)
        self.records = records.AsyncRecordsResource(self)
        self.scores = scores.AsyncScoresResource(self)
        self.systems = systems.AsyncSystemsResource(self)
        self.with_raw_response = AsyncScorecardWithRawResponse(self)
        self.with_streaming_response = AsyncScorecardWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ScorecardWithRawResponse:
    def __init__(self, client: Scorecard) -> None:
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.testsets = testsets.TestsetsResourceWithRawResponse(client.testsets)
        self.testcases = testcases.TestcasesResourceWithRawResponse(client.testcases)
        self.runs = runs.RunsResourceWithRawResponse(client.runs)
        self.metrics = metrics.MetricsResourceWithRawResponse(client.metrics)
        self.records = records.RecordsResourceWithRawResponse(client.records)
        self.scores = scores.ScoresResourceWithRawResponse(client.scores)
        self.systems = systems.SystemsResourceWithRawResponse(client.systems)


class AsyncScorecardWithRawResponse:
    def __init__(self, client: AsyncScorecard) -> None:
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.testsets = testsets.AsyncTestsetsResourceWithRawResponse(client.testsets)
        self.testcases = testcases.AsyncTestcasesResourceWithRawResponse(client.testcases)
        self.runs = runs.AsyncRunsResourceWithRawResponse(client.runs)
        self.metrics = metrics.AsyncMetricsResourceWithRawResponse(client.metrics)
        self.records = records.AsyncRecordsResourceWithRawResponse(client.records)
        self.scores = scores.AsyncScoresResourceWithRawResponse(client.scores)
        self.systems = systems.AsyncSystemsResourceWithRawResponse(client.systems)


class ScorecardWithStreamedResponse:
    def __init__(self, client: Scorecard) -> None:
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.testsets = testsets.TestsetsResourceWithStreamingResponse(client.testsets)
        self.testcases = testcases.TestcasesResourceWithStreamingResponse(client.testcases)
        self.runs = runs.RunsResourceWithStreamingResponse(client.runs)
        self.metrics = metrics.MetricsResourceWithStreamingResponse(client.metrics)
        self.records = records.RecordsResourceWithStreamingResponse(client.records)
        self.scores = scores.ScoresResourceWithStreamingResponse(client.scores)
        self.systems = systems.SystemsResourceWithStreamingResponse(client.systems)


class AsyncScorecardWithStreamedResponse:
    def __init__(self, client: AsyncScorecard) -> None:
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.testsets = testsets.AsyncTestsetsResourceWithStreamingResponse(client.testsets)
        self.testcases = testcases.AsyncTestcasesResourceWithStreamingResponse(client.testcases)
        self.runs = runs.AsyncRunsResourceWithStreamingResponse(client.runs)
        self.metrics = metrics.AsyncMetricsResourceWithStreamingResponse(client.metrics)
        self.records = records.AsyncRecordsResourceWithStreamingResponse(client.records)
        self.scores = scores.AsyncScoresResourceWithStreamingResponse(client.scores)
        self.systems = systems.AsyncSystemsResourceWithStreamingResponse(client.systems)


Client = Scorecard

AsyncClient = AsyncScorecard
