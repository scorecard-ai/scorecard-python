"""
Helper functions for the Scorecard AI library.
"""

import asyncio
from typing import Any, List, Callable, Coroutine
from typing_extensions import TypedDict

from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.types.record import Record
from scorecard_ai.types.testcase import Testcase


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
    project_id: str,
    testset_id: str,
    metric_ids: List[str],
    system: Callable[[Any], Any],
) -> RunResponse:
    """
    Runs a system on a Testset and records the results in Scorecard.

    Args:
        scorecard: The Scorecard client.

        project_id: The ID of the Project to run the system on.

        testset_id: The ID of the Testset to run the system on.

        metric_ids: The IDs of the Metrics to use for evaluation.

        system: The system to run on the Testset.
    """
    run = client.runs.create(project_id=project_id, testset_id=testset_id, metric_ids=metric_ids)

    # Run each Testcase sequentially
    for testcase in client.testcases.list(run.testset_id):
        model_response = system(testcase.inputs)
        client.records.create(
            run_id=run.id,
            testcase_id=testcase.id,
            inputs=testcase.inputs,
            labels=testcase.labels,
            outputs=model_response,
        )

    # Mark the Run as done with execution and ready for scoring.
    client.runs.update(run.id, status="awaiting_scoring")

    run_url = f"https://app.getscorecard.ai/projects/{project_id}/runs/grades/{run.id}"

    return RunResponse(id=run.id, url=run_url)


async def async_run_and_evaluate(
    client: AsyncScorecard,
    project_id: str,
    testset_id: str,
    metric_ids: List[str],
    system: Callable[[Any], Any],
) -> RunResponse:
    """
    Runs a system on a Testset and records the results in Scorecard.

    Async equivalent of `run_and_evaluate`.

    Args:
        scorecard: The AsyncScorecard client.

        project_id: The ID of the Project to run the system on.

        testset_id: The ID of the Testset to run the system on.

        metric_ids: The IDs of the Metrics to use for evaluation.

        system: The system to run on the Testset.
    """
    run = await client.runs.create(project_id=project_id, testset_id=testset_id, metric_ids=metric_ids)

    def run_testcase(testcase: Testcase) -> Coroutine[Any, Any, Record]:
        model_response = system(testcase.inputs)
        return client.records.create(
            run_id=run.id,
            testcase_id=testcase.id,
            inputs=testcase.inputs,
            labels=testcase.labels,
            outputs=model_response,
        )

    # Create a Record for each Testcase
    await asyncio.gather(*[run_testcase(testcase) async for testcase in client.testcases.list(run.testset_id)])

    # Mark the Run as done with execution and ready for scoring.
    await client.runs.update(run.id, status="awaiting_scoring")

    run_url = f"https://app.getscorecard.ai/projects/{project_id}/runs/grades/{run.id}"
    return RunResponse(id=run.id, url=run_url)
