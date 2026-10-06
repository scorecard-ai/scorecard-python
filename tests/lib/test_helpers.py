from __future__ import annotations

import asyncio
from typing import Any, cast
from collections import Counter
from unittest.mock import Mock, AsyncMock
from collections.abc import Awaitable, Generator, AsyncGenerator

import pytest

from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai._types import NOT_GIVEN, omit
from scorecard_ai.lib._helpers import (
    SystemInput,
    SystemOutput,
    SystemOptions,
    SimpleTestcase,
    run_and_evaluate,
    async_run_and_evaluate,
)
from scorecard_ai.types.testcase import Testcase
from scorecard_ai.types.systems.system_version import SystemVersion


class OutputAwaitable:
    def __init__(self, output: SystemOutput) -> None:
        self.output = output

    def __await__(self) -> Generator[Any, None, SystemOutput]:
        async def resolve() -> SystemOutput:
            return self.output

        return resolve().__await__()


@pytest.mark.parametrize("system_kind", ["sync", "async", "coroutine", "awaitable"])
@pytest.mark.parametrize("with_options", [False, True])
@pytest.mark.parametrize("from_testset", [False, True])
async def test_async_run_and_evaluate(system_kind: str, with_options: bool, from_testset: bool) -> None:
    client = Mock()
    client.base_app_url = "https://app.example.com"
    client.runs.create = AsyncMock(return_value=Mock(id="run-id"))
    client.records.create = AsyncMock()
    version = Mock(spec=SystemVersion)
    client.systems.versions.get = AsyncMock(return_value=version)
    testcases: list[SimpleTestcase] = [
        {"inputs": {"value": value}, "expected": {"answer": value}} for value in range(2)
    ]

    async def list_testcases() -> AsyncGenerator[Testcase, None]:
        for index, testcase in enumerate(testcases):
            yield Testcase(
                id=str(index),
                inputs=testcase["inputs"],
                expected=testcase["expected"],
                jsonData={},
                testsetId="testset-id",
            )

    client.testcases.list.return_value = list_testcases() if from_testset else None
    calls: list[tuple[SystemInput, SystemVersion | None, SystemOptions | None]] = []
    active = 0
    max_active = 0

    async def resolve(inputs: SystemInput) -> SystemOutput:
        nonlocal active, max_active
        active += 1
        max_active = max(max_active, active)
        await asyncio.sleep(0)
        active -= 1
        return {"answer": inputs["value"]}

    def sync_system(
        inputs: SystemInput, system_version: SystemVersion | None, options: SystemOptions | None = None
    ) -> SystemOutput | Awaitable[SystemOutput]:
        calls.append((inputs, system_version, options))
        if system_kind == "coroutine":
            return resolve(inputs)
        output = {"answer": inputs["value"]}
        return OutputAwaitable(output) if system_kind == "awaitable" else output

    async def async_system(
        inputs: SystemInput, system_version: SystemVersion | None, options: SystemOptions | None = None
    ) -> SystemOutput:
        calls.append((inputs, system_version, options))
        return await resolve(inputs)

    selected_system = async_system if system_kind == "async" else sync_system

    def two_argument_system(
        inputs: SystemInput, system_version: SystemVersion | None
    ) -> SystemOutput | Awaitable[SystemOutput]:
        return selected_system(inputs, system_version)

    result = await async_run_and_evaluate(
        cast(AsyncScorecard, client),
        project_id="project-id",
        metric_ids=["metric-id"],
        testset_id="testset-id" if from_testset else NOT_GIVEN,
        testcases=NOT_GIVEN if from_testset else testcases,
        system_version_id="version-id",
        system=selected_system if with_options else two_argument_system,
        trials=3,
    )

    assert result == {"id": "run-id", "url": "https://app.example.com/projects/project-id/runs/run-id"}
    assert len(calls) == 6
    assert all(system_version is version for _, system_version, _ in calls)
    assert client.records.create.await_count == 6
    records = [call.kwargs for call in client.records.create.await_args_list]
    assert Counter(record["inputs"]["value"] for record in records) == {0: 3, 1: 3}
    assert len({record["extra_body"]["otelLinkId"] for record in records}) == 6
    for record in records:
        value = record["inputs"]["value"]
        assert record["outputs"] == record["expected"] == {"answer": value}
        assert record["run_id"] == "run-id"
        assert record["testcase_id"] == (str(value) if from_testset else omit)
    if with_options:
        assert {options["otel_link_id"] for _, _, options in calls if options is not None} == {
            record["extra_body"]["otelLinkId"] for record in records
        }
    else:
        assert all(options is None for _, _, options in calls)
    if system_kind in ("async", "coroutine"):
        assert max_active == 6


@pytest.mark.parametrize("with_options", [False, True])
def test_run_and_evaluate_sync_system(with_options: bool) -> None:
    client = Mock()
    client.base_app_url = "https://app.example.com"
    client.runs.create.return_value.id = "run-id"

    def system(inputs: SystemInput, version: SystemVersion | None, options: SystemOptions) -> SystemOutput:
        assert version is None
        assert options["otel_link_id"]
        return {"answer": inputs["value"]}

    def two_argument_system(inputs: SystemInput, version: SystemVersion | None) -> SystemOutput:
        assert version is None
        return {"answer": inputs["value"]}

    result = run_and_evaluate(
        cast(Scorecard, client),
        project_id="project-id",
        metric_ids=["metric-id"],
        testcases=[{"inputs": {"value": 42}, "expected": {"answer": 42}}],
        system=system if with_options else two_argument_system,
        trials=3,
    )

    assert result["id"] == "run-id"
    assert client.records.create.call_count == 3
    assert all(call.kwargs["outputs"] == {"answer": 42} for call in client.records.create.call_args_list)


@pytest.mark.parametrize("system_kind", ["async", "coroutine", "awaitable"])
@pytest.mark.parametrize("with_options", [False, True])
def test_run_and_evaluate_rejects_awaitable(system_kind: str, with_options: bool) -> None:
    client = Mock()

    async def async_system(
        inputs: SystemInput, version: SystemVersion | None, options: SystemOptions | None = None
    ) -> SystemOutput:
        assert version is None
        assert (options is not None) == with_options
        return {"answer": inputs["value"]}

    def system(inputs: SystemInput, version: SystemVersion | None, options: SystemOptions) -> Any:
        if system_kind == "awaitable":
            return OutputAwaitable({"answer": inputs["value"]})
        return async_system(inputs, version, options)

    def two_argument_system(inputs: SystemInput, version: SystemVersion | None) -> Any:
        if system_kind == "awaitable":
            return OutputAwaitable({"answer": inputs["value"]})
        return async_system(inputs, version)

    selected_system = (async_system if system_kind == "async" else system) if with_options else two_argument_system
    with pytest.raises(TypeError, match="async_run_and_evaluate"):
        run_and_evaluate(
            cast(Scorecard, client),
            project_id="project-id",
            metric_ids=["metric-id"],
            testcases=[{"inputs": {"value": 42}, "expected": {}}],
            system=cast(Any, selected_system),
        )
    client.records.create.assert_not_called()
