# This file was auto-generated by Fern from our API Definition.

import typing

import httpx
import os

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.api_error import ApiError
from .environment import ScorecardEnvironment
from .resources.run.client import AsyncRunClient, RunClient
from .resources.testcase.client import AsyncTestcaseClient, TestcaseClient
from .resources.testrecord.client import AsyncTestrecordClient, TestrecordClient
from .resources.testset.client import AsyncTestsetClient, TestsetClient


class Scorecard:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: ScorecardEnvironment = ScorecardEnvironment.DEFAULT,
        api_key: typing.Optional[str] = os.getenv("SCORECARD_API_KEY"),
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        if api_key is None: 
            raise ApiError(
                body="Please provide an api_key or set SCORECARD_API_KEY")
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.testset = TestsetClient(client_wrapper=self._client_wrapper)
        self.testcase = TestcaseClient(client_wrapper=self._client_wrapper)
        self.run = RunClient(client_wrapper=self._client_wrapper)
        self.testrecord = TestrecordClient(client_wrapper=self._client_wrapper)

    def run_tests(
        self,
        *,
        input_testset_id: int,
        scoring_config_id: int,
        model_invocation: typing.Callable[[str], typing.Any],
    ) -> None: 
        """
        Runs all tests within a testset.

        Parameters:
            - input_testset_id: int. The ID of the Test Set you want to run.

            - scoring_config_id: int. 

            - model_invocation: typing.Callable[[typing.str], typing.Any].
            A function that will call your AI model with a prompt.
        """
        run_id = self.run.create(
            testset_id=input_testset_id, 
            scoring_config_id=scoring_config_id
        )
        testcases = self.testset.get(input_testset_id)

        for testcase in testcases:
            testcase_id = testcase['id']
            query = testcase['user_query']

            print(f"Running testcase {testcase_id}...")
            print(f"User query: {query}")

            response = model_invocation(query)

            self.testrecord.create(
                run_id=run_id,
                testcase_id=testcase_id,
                model_response=response,
            )

        print("Finished running testcases...")


class AsyncScorecard:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: ScorecardEnvironment = ScorecardEnvironment.DEFAULT,
        api_key: str,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        if api_key is None: 
            raise ApiError(
                body="Please provide an api_key or set SCORECARD_API_KEY")
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.testset = AsyncTestsetClient(client_wrapper=self._client_wrapper)
        self.testcase = AsyncTestcaseClient(client_wrapper=self._client_wrapper)
        self.run = AsyncRunClient(client_wrapper=self._client_wrapper)
        self.testrecord = AsyncTestrecordClient(client_wrapper=self._client_wrapper)
    
    async def run_tests(
        self,
        *,
        input_testset_id: int,
        scoring_config_id: int,
        model_invocation: typing.Callable[[str], typing.Any],
    ) -> None: 
        """
        Runs all tests within a testset.

        Parameters:
            - input_testset_id: int. The ID of the Test Set you want to run.

            - scoring_config_id: int. 

            - model_invocation: typing.Callable[[typing.str], typing.Any].
            A function that will call your AI model with a prompt.
        """
        run_id = await self.run.create(
            testset_id=input_testset_id, 
            scoring_config_id=scoring_config_id
        )
        testcases = await self.testset.get(input_testset_id)

        for testcase in testcases:
            testcase_id = testcase['id']
            query = testcase['user_query']

            print(f"Running testcase {testcase_id}...")
            print(f"User query: {query}")

            response = model_invocation(query)

            await self.testrecord.create(
                run_id=run_id,
                testcase_id=testcase_id,
                model_response=response,
            )

        print("Finished running testcases...")


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: ScorecardEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
