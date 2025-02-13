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
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import prompt, traces, welcome, run_metric, scoring_config
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ScorecardError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.run import run
from .resources.testset import testset

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
    "production": "https://api.getscorecard.ai",
    "environment_1": "http://localhost:8000",
    "environment_2": "https://api.scorecard.io",
}


class Scorecard(SyncAPIClient):
    welcome: welcome.WelcomeResource
    run_metric: run_metric.RunMetricResource
    testset: testset.TestsetResource
    run: run.RunResource
    traces: traces.TracesResource
    prompt: prompt.PromptResource
    scoring_config: scoring_config.ScoringConfigResource
    with_raw_response: ScorecardWithRawResponse
    with_streaming_response: ScorecardWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "environment_1", "environment_2"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | NotGiven = NOT_GIVEN,
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
        """Construct a new synchronous scorecard client instance.

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

        self.welcome = welcome.WelcomeResource(self)
        self.run_metric = run_metric.RunMetricResource(self)
        self.testset = testset.TestsetResource(self)
        self.run = run.RunResource(self)
        self.traces = traces.TracesResource(self)
        self.prompt = prompt.PromptResource(self)
        self.scoring_config = scoring_config.ScoringConfigResource(self)
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
        return {"X-API-Key": api_key}

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
        environment: Literal["production", "environment_1", "environment_2"] | None = None,
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


class AsyncScorecard(AsyncAPIClient):
    welcome: welcome.AsyncWelcomeResource
    run_metric: run_metric.AsyncRunMetricResource
    testset: testset.AsyncTestsetResource
    run: run.AsyncRunResource
    traces: traces.AsyncTracesResource
    prompt: prompt.AsyncPromptResource
    scoring_config: scoring_config.AsyncScoringConfigResource
    with_raw_response: AsyncScorecardWithRawResponse
    with_streaming_response: AsyncScorecardWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "environment_1", "environment_2"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | NotGiven = NOT_GIVEN,
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
        """Construct a new async scorecard client instance.

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

        self.welcome = welcome.AsyncWelcomeResource(self)
        self.run_metric = run_metric.AsyncRunMetricResource(self)
        self.testset = testset.AsyncTestsetResource(self)
        self.run = run.AsyncRunResource(self)
        self.traces = traces.AsyncTracesResource(self)
        self.prompt = prompt.AsyncPromptResource(self)
        self.scoring_config = scoring_config.AsyncScoringConfigResource(self)
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
        return {"X-API-Key": api_key}

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
        environment: Literal["production", "environment_1", "environment_2"] | None = None,
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
        self.welcome = welcome.WelcomeResourceWithRawResponse(client.welcome)
        self.run_metric = run_metric.RunMetricResourceWithRawResponse(client.run_metric)
        self.testset = testset.TestsetResourceWithRawResponse(client.testset)
        self.run = run.RunResourceWithRawResponse(client.run)
        self.traces = traces.TracesResourceWithRawResponse(client.traces)
        self.prompt = prompt.PromptResourceWithRawResponse(client.prompt)
        self.scoring_config = scoring_config.ScoringConfigResourceWithRawResponse(client.scoring_config)


class AsyncScorecardWithRawResponse:
    def __init__(self, client: AsyncScorecard) -> None:
        self.welcome = welcome.AsyncWelcomeResourceWithRawResponse(client.welcome)
        self.run_metric = run_metric.AsyncRunMetricResourceWithRawResponse(client.run_metric)
        self.testset = testset.AsyncTestsetResourceWithRawResponse(client.testset)
        self.run = run.AsyncRunResourceWithRawResponse(client.run)
        self.traces = traces.AsyncTracesResourceWithRawResponse(client.traces)
        self.prompt = prompt.AsyncPromptResourceWithRawResponse(client.prompt)
        self.scoring_config = scoring_config.AsyncScoringConfigResourceWithRawResponse(client.scoring_config)


class ScorecardWithStreamedResponse:
    def __init__(self, client: Scorecard) -> None:
        self.welcome = welcome.WelcomeResourceWithStreamingResponse(client.welcome)
        self.run_metric = run_metric.RunMetricResourceWithStreamingResponse(client.run_metric)
        self.testset = testset.TestsetResourceWithStreamingResponse(client.testset)
        self.run = run.RunResourceWithStreamingResponse(client.run)
        self.traces = traces.TracesResourceWithStreamingResponse(client.traces)
        self.prompt = prompt.PromptResourceWithStreamingResponse(client.prompt)
        self.scoring_config = scoring_config.ScoringConfigResourceWithStreamingResponse(client.scoring_config)


class AsyncScorecardWithStreamedResponse:
    def __init__(self, client: AsyncScorecard) -> None:
        self.welcome = welcome.AsyncWelcomeResourceWithStreamingResponse(client.welcome)
        self.run_metric = run_metric.AsyncRunMetricResourceWithStreamingResponse(client.run_metric)
        self.testset = testset.AsyncTestsetResourceWithStreamingResponse(client.testset)
        self.run = run.AsyncRunResourceWithStreamingResponse(client.run)
        self.traces = traces.AsyncTracesResourceWithStreamingResponse(client.traces)
        self.prompt = prompt.AsyncPromptResourceWithStreamingResponse(client.prompt)
        self.scoring_config = scoring_config.AsyncScoringConfigResourceWithStreamingResponse(client.scoring_config)


Client = Scorecard

AsyncClient = AsyncScorecard
