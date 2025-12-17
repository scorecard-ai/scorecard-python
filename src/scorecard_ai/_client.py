# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ScorecardError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import runs, scores, metrics, records, systems, projects, testsets, testcases
    from .resources.runs import RunsResource, AsyncRunsResource
    from .resources.scores import ScoresResource, AsyncScoresResource
    from .resources.metrics import MetricsResource, AsyncMetricsResource
    from .resources.records import RecordsResource, AsyncRecordsResource
    from .resources.projects import ProjectsResource, AsyncProjectsResource
    from .resources.testsets import TestsetsResource, AsyncTestsetsResource
    from .resources.testcases import TestcasesResource, AsyncTestcasesResource
    from .resources.systems.systems import SystemsResource, AsyncSystemsResource

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


class HasBaseAppURL:
    """
    This class is used to add the base app URL to the sync and async clients.
    """

    _base_url: httpx.URL

    @property
    def base_app_url(self) -> str:
        """Returns the base URL for the Scorecard app."""
        base_url = str(self._base_url).rstrip("/")
        if base_url == ENVIRONMENTS["production"]:
            return "https://app.scorecard.io"
        elif base_url == ENVIRONMENTS["staging"]:
            return "https://staging.app.getscorecard.ai"
        elif base_url == ENVIRONMENTS["local"]:
            return "http://localhost:3002"
        else:
            return "https://staging.app.getscorecard.ai"


class Scorecard(HasBaseAppURL, SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def projects(self) -> ProjectsResource:
        from .resources.projects import ProjectsResource

        return ProjectsResource(self)

    @cached_property
    def testsets(self) -> TestsetsResource:
        from .resources.testsets import TestsetsResource

        return TestsetsResource(self)

    @cached_property
    def testcases(self) -> TestcasesResource:
        from .resources.testcases import TestcasesResource

        return TestcasesResource(self)

    @cached_property
    def runs(self) -> RunsResource:
        from .resources.runs import RunsResource

        return RunsResource(self)

    @cached_property
    def metrics(self) -> MetricsResource:
        from .resources.metrics import MetricsResource

        return MetricsResource(self)

    @cached_property
    def records(self) -> RecordsResource:
        from .resources.records import RecordsResource

        return RecordsResource(self)

    @cached_property
    def scores(self) -> ScoresResource:
        from .resources.scores import ScoresResource

        return ScoresResource(self)

    @cached_property
    def systems(self) -> SystemsResource:
        from .resources.systems import SystemsResource

        return SystemsResource(self)

    @cached_property
    def with_raw_response(self) -> ScorecardWithRawResponse:
        return ScorecardWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScorecardWithStreamedResponse:
        return ScorecardWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
    # client options
    api_key: str

    _environment: Literal["production", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def projects(self) -> AsyncProjectsResource:
        from .resources.projects import AsyncProjectsResource

        return AsyncProjectsResource(self)

    @cached_property
    def testsets(self) -> AsyncTestsetsResource:
        from .resources.testsets import AsyncTestsetsResource

        return AsyncTestsetsResource(self)

    @cached_property
    def testcases(self) -> AsyncTestcasesResource:
        from .resources.testcases import AsyncTestcasesResource

        return AsyncTestcasesResource(self)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        from .resources.runs import AsyncRunsResource

        return AsyncRunsResource(self)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        from .resources.metrics import AsyncMetricsResource

        return AsyncMetricsResource(self)

    @cached_property
    def records(self) -> AsyncRecordsResource:
        from .resources.records import AsyncRecordsResource

        return AsyncRecordsResource(self)

    @cached_property
    def scores(self) -> AsyncScoresResource:
        from .resources.scores import AsyncScoresResource

        return AsyncScoresResource(self)

    @cached_property
    def systems(self) -> AsyncSystemsResource:
        from .resources.systems import AsyncSystemsResource

        return AsyncSystemsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncScorecardWithRawResponse:
        return AsyncScorecardWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScorecardWithStreamedResponse:
        return AsyncScorecardWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
    _client: Scorecard

    def __init__(self, client: Scorecard) -> None:
        self._client = client

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithRawResponse:
        from .resources.projects import ProjectsResourceWithRawResponse

        return ProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def testsets(self) -> testsets.TestsetsResourceWithRawResponse:
        from .resources.testsets import TestsetsResourceWithRawResponse

        return TestsetsResourceWithRawResponse(self._client.testsets)

    @cached_property
    def testcases(self) -> testcases.TestcasesResourceWithRawResponse:
        from .resources.testcases import TestcasesResourceWithRawResponse

        return TestcasesResourceWithRawResponse(self._client.testcases)

    @cached_property
    def runs(self) -> runs.RunsResourceWithRawResponse:
        from .resources.runs import RunsResourceWithRawResponse

        return RunsResourceWithRawResponse(self._client.runs)

    @cached_property
    def metrics(self) -> metrics.MetricsResourceWithRawResponse:
        from .resources.metrics import MetricsResourceWithRawResponse

        return MetricsResourceWithRawResponse(self._client.metrics)

    @cached_property
    def records(self) -> records.RecordsResourceWithRawResponse:
        from .resources.records import RecordsResourceWithRawResponse

        return RecordsResourceWithRawResponse(self._client.records)

    @cached_property
    def scores(self) -> scores.ScoresResourceWithRawResponse:
        from .resources.scores import ScoresResourceWithRawResponse

        return ScoresResourceWithRawResponse(self._client.scores)

    @cached_property
    def systems(self) -> systems.SystemsResourceWithRawResponse:
        from .resources.systems import SystemsResourceWithRawResponse

        return SystemsResourceWithRawResponse(self._client.systems)


class AsyncScorecardWithRawResponse:
    _client: AsyncScorecard

    def __init__(self, client: AsyncScorecard) -> None:
        self._client = client

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithRawResponse:
        from .resources.projects import AsyncProjectsResourceWithRawResponse

        return AsyncProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def testsets(self) -> testsets.AsyncTestsetsResourceWithRawResponse:
        from .resources.testsets import AsyncTestsetsResourceWithRawResponse

        return AsyncTestsetsResourceWithRawResponse(self._client.testsets)

    @cached_property
    def testcases(self) -> testcases.AsyncTestcasesResourceWithRawResponse:
        from .resources.testcases import AsyncTestcasesResourceWithRawResponse

        return AsyncTestcasesResourceWithRawResponse(self._client.testcases)

    @cached_property
    def runs(self) -> runs.AsyncRunsResourceWithRawResponse:
        from .resources.runs import AsyncRunsResourceWithRawResponse

        return AsyncRunsResourceWithRawResponse(self._client.runs)

    @cached_property
    def metrics(self) -> metrics.AsyncMetricsResourceWithRawResponse:
        from .resources.metrics import AsyncMetricsResourceWithRawResponse

        return AsyncMetricsResourceWithRawResponse(self._client.metrics)

    @cached_property
    def records(self) -> records.AsyncRecordsResourceWithRawResponse:
        from .resources.records import AsyncRecordsResourceWithRawResponse

        return AsyncRecordsResourceWithRawResponse(self._client.records)

    @cached_property
    def scores(self) -> scores.AsyncScoresResourceWithRawResponse:
        from .resources.scores import AsyncScoresResourceWithRawResponse

        return AsyncScoresResourceWithRawResponse(self._client.scores)

    @cached_property
    def systems(self) -> systems.AsyncSystemsResourceWithRawResponse:
        from .resources.systems import AsyncSystemsResourceWithRawResponse

        return AsyncSystemsResourceWithRawResponse(self._client.systems)


class ScorecardWithStreamedResponse:
    _client: Scorecard

    def __init__(self, client: Scorecard) -> None:
        self._client = client

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithStreamingResponse:
        from .resources.projects import ProjectsResourceWithStreamingResponse

        return ProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def testsets(self) -> testsets.TestsetsResourceWithStreamingResponse:
        from .resources.testsets import TestsetsResourceWithStreamingResponse

        return TestsetsResourceWithStreamingResponse(self._client.testsets)

    @cached_property
    def testcases(self) -> testcases.TestcasesResourceWithStreamingResponse:
        from .resources.testcases import TestcasesResourceWithStreamingResponse

        return TestcasesResourceWithStreamingResponse(self._client.testcases)

    @cached_property
    def runs(self) -> runs.RunsResourceWithStreamingResponse:
        from .resources.runs import RunsResourceWithStreamingResponse

        return RunsResourceWithStreamingResponse(self._client.runs)

    @cached_property
    def metrics(self) -> metrics.MetricsResourceWithStreamingResponse:
        from .resources.metrics import MetricsResourceWithStreamingResponse

        return MetricsResourceWithStreamingResponse(self._client.metrics)

    @cached_property
    def records(self) -> records.RecordsResourceWithStreamingResponse:
        from .resources.records import RecordsResourceWithStreamingResponse

        return RecordsResourceWithStreamingResponse(self._client.records)

    @cached_property
    def scores(self) -> scores.ScoresResourceWithStreamingResponse:
        from .resources.scores import ScoresResourceWithStreamingResponse

        return ScoresResourceWithStreamingResponse(self._client.scores)

    @cached_property
    def systems(self) -> systems.SystemsResourceWithStreamingResponse:
        from .resources.systems import SystemsResourceWithStreamingResponse

        return SystemsResourceWithStreamingResponse(self._client.systems)


class AsyncScorecardWithStreamedResponse:
    _client: AsyncScorecard

    def __init__(self, client: AsyncScorecard) -> None:
        self._client = client

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithStreamingResponse:
        from .resources.projects import AsyncProjectsResourceWithStreamingResponse

        return AsyncProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def testsets(self) -> testsets.AsyncTestsetsResourceWithStreamingResponse:
        from .resources.testsets import AsyncTestsetsResourceWithStreamingResponse

        return AsyncTestsetsResourceWithStreamingResponse(self._client.testsets)

    @cached_property
    def testcases(self) -> testcases.AsyncTestcasesResourceWithStreamingResponse:
        from .resources.testcases import AsyncTestcasesResourceWithStreamingResponse

        return AsyncTestcasesResourceWithStreamingResponse(self._client.testcases)

    @cached_property
    def runs(self) -> runs.AsyncRunsResourceWithStreamingResponse:
        from .resources.runs import AsyncRunsResourceWithStreamingResponse

        return AsyncRunsResourceWithStreamingResponse(self._client.runs)

    @cached_property
    def metrics(self) -> metrics.AsyncMetricsResourceWithStreamingResponse:
        from .resources.metrics import AsyncMetricsResourceWithStreamingResponse

        return AsyncMetricsResourceWithStreamingResponse(self._client.metrics)

    @cached_property
    def records(self) -> records.AsyncRecordsResourceWithStreamingResponse:
        from .resources.records import AsyncRecordsResourceWithStreamingResponse

        return AsyncRecordsResourceWithStreamingResponse(self._client.records)

    @cached_property
    def scores(self) -> scores.AsyncScoresResourceWithStreamingResponse:
        from .resources.scores import AsyncScoresResourceWithStreamingResponse

        return AsyncScoresResourceWithStreamingResponse(self._client.scores)

    @cached_property
    def systems(self) -> systems.AsyncSystemsResourceWithStreamingResponse:
        from .resources.systems import AsyncSystemsResourceWithStreamingResponse

        return AsyncSystemsResourceWithStreamingResponse(self._client.systems)


Client = Scorecard

AsyncClient = AsyncScorecard
