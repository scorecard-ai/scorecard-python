"""
Helper functions for the Scorecard AI library.
"""

from __future__ import annotations

import asyncio
from typing import Any, Dict, List, Callable, Coroutine
from collections.abc import Generator, AsyncGenerator
from typing_extensions import TypedDict

from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai._types import NOT_GIVEN, NotGiven
from scorecard_ai.types.record import Record
from scorecard_ai.types.testcase import Testcase
from scorecard_ai.types.systems.system_version import SystemVersion

SystemInput = Dict[str, Any]
SystemOutput = Dict[str, Any]


class SimpleTestcase(TypedDict):
    """
    A simple test case not tracked in a Scorecard Testset.
    """

    inputs: SystemInput
    expected: Dict[str, Any]


class _SimpleTestcaseWithId(SimpleTestcase):
    id: str | NotGiven


def _transform_testcase(testcase: Testcase | SimpleTestcase) -> _SimpleTestcaseWithId:
    """
    Transforms a Testcase or SimpleTestcase into a _SimpleTestcaseWithId.
    """
    if isinstance(testcase, Testcase):
        return _SimpleTestcaseWithId(
            id=testcase.id,
            inputs=testcase.inputs,
            expected=testcase.expected,
        )
    else:
        return _SimpleTestcaseWithId(
            id=NOT_GIVEN,
            inputs=testcase["inputs"],
            expected=testcase["expected"],
        )


def _get_run_url(
    scorecard: Scorecard | AsyncScorecard, project_id: str, run_id: str
) -> str:
    return f"{scorecard.base_app_url}/projects/{project_id}/runs/{run_id}"


class RunResponse(TypedDict):
    """
    The response from the run_and_evaluate function.
    """

    id: str
    """The ID of the run."""

    url: str
    """The URL of the run."""


def run_and_evaluate(
    client: Scorecard,
    *,
    project_id: str,
    metric_ids: List[str],
    testset_id: str | NotGiven = NOT_GIVEN,
    testcases: List[Testcase] | List[SimpleTestcase] | NotGiven = NOT_GIVEN,
    system_version_id: str | NotGiven = NOT_GIVEN,
    system: Callable[[SystemInput, SystemVersion | None], SystemOutput],
    trials: int = 1,
) -> RunResponse:
    """
    Runs the given `system` on the given test cases and records the results in a Scorecard Run.

    Exactly one of `testset_id` and `testcases` must be provided.

    Args:
        scorecard: The Scorecard client.

        project_id: The ID of the Project to run the system on.

        metric_ids: The IDs of the Metrics to use for evaluation.

        testset_id: The ID of the Testset to run the system on, if `testcases` is not provided.

        testcases: The Testcases to run the system on, if `testset_id` is not provided.

        system_version_id: The ID of the SystemVersion to use for the run.

        system: The system to run on the Testset.

        trials: The number of times to run the system on each Testcase.
    """
    if trials <= 0:
        raise ValueError("trials must be positive")

    testcase_iter: Generator[_SimpleTestcaseWithId, None, None]
    if not isinstance(testcases, NotGiven) and not isinstance(testset_id, NotGiven):
        raise ValueError("testcases and testset_id cannot both be provided")
    elif not isinstance(testcases, NotGiven):
        testcase_iter = (_transform_testcase(testcase) for testcase in testcases)
    elif not isinstance(testset_id, NotGiven):
        testcase_iter = (
            _transform_testcase(testcase)
            for testcase in client.testcases.list(testset_id)
        )
    else:
        raise ValueError("testcases or testset_id must be provided")

    run = client.runs.create(
        project_id=project_id,
        testset_id=testset_id,
        metric_ids=metric_ids,
        system_version_id=system_version_id,
    )

    system_version: SystemVersion | None = (
        client.systems.versions.get(system_version_id)
        if not isinstance(system_version_id, NotGiven)
        else None
    )

    # Run each Testcase sequentially
    for testcase in testcase_iter:
        for _ in range(trials):
            model_response = system(testcase["inputs"], system_version)
            client.records.create(
                run_id=run.id,
                testcase_id=testcase["id"],
                inputs=testcase["inputs"],
                expected=testcase["expected"],
                outputs=model_response,
            )

    return RunResponse(id=run.id, url=_get_run_url(client, project_id, run.id))


async def async_run_and_evaluate(
    client: AsyncScorecard,
    *,
    project_id: str,
    metric_ids: List[str],
    testset_id: str | NotGiven = NOT_GIVEN,
    testcases: List[Testcase] | List[SimpleTestcase] | NotGiven = NOT_GIVEN,
    system_version_id: str | NotGiven = NOT_GIVEN,
    system: Callable[[SystemInput, SystemVersion | None], SystemOutput],
    trials: int = 1,
) -> RunResponse:
    """
    Runs a system on a Testset and records the results in Scorecard.

    Exactly one of `testset_id` and `testcases` must be provided. Async equivalent of `run_and_evaluate`.

    Args:
        scorecard: The AsyncScorecard client.

        project_id: The ID of the Project to run the system on.

        metric_ids: The IDs of the Metrics to use for evaluation.

        testset_id: The ID of the Testset to run the system on, if `testcases` is not provided.

        testcases: The Testcases to run the system on, if `testset_id` is not provided.

        system_version_id: The ID of the SystemVersion to use for the run.

        system: The system to run on the Testset.

        trials: The number of times to run the system on each Testcase.
    """
    if trials <= 0:
        raise ValueError("trials must be positive")

    testcase_iter: (
        Generator[_SimpleTestcaseWithId, None, None]
        | AsyncGenerator[_SimpleTestcaseWithId, None]
    )
    if not isinstance(testcases, NotGiven) and not isinstance(testset_id, NotGiven):
        raise ValueError("testcases and testset_id cannot both be provided")
    elif not isinstance(testcases, NotGiven):
        testcase_iter = (_transform_testcase(testcase) for testcase in testcases)
    elif not isinstance(testset_id, NotGiven):
        testcase_iter = (
            _transform_testcase(testcase)
            async for testcase in client.testcases.list(testset_id)
        )
    else:
        raise ValueError("testcases or testset_id must be provided")

    run = await client.runs.create(
        project_id=project_id,
        testset_id=testset_id,
        metric_ids=metric_ids,
        system_version_id=system_version_id,
    )

    system_version: SystemVersion | None = (
        await client.systems.versions.get(system_version_id)
        if not isinstance(system_version_id, NotGiven)
        else None
    )

    def run_testcase(
        testcase: _SimpleTestcaseWithId,
    ) -> Coroutine[Any, Any, Record]:
        model_response = system(testcase["inputs"], system_version)
        return client.records.create(
            run_id=run.id,
            testcase_id=testcase["id"],
            inputs=testcase["inputs"],
            expected=testcase["expected"],
            outputs=model_response,
        )

    # Create a Record for each Testcase
    if isinstance(testcase_iter, AsyncGenerator):
        await asyncio.gather(
            *[
                run_testcase(testcase)
                async for testcase in testcase_iter
                for _ in range(trials)
            ]
        )
    else:
        await asyncio.gather(
            *[
                run_testcase(testcase)
                for testcase in testcase_iter
                for _ in range(trials)
            ]
        )

    return RunResponse(id=run.id, url=_get_run_url(client, project_id, run.id))
