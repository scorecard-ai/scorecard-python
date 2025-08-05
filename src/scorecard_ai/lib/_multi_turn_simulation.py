"""
Multi-turn simulation.
"""

from __future__ import annotations

from typing import List, Literal, Callable, TypedDict
from collections.abc import Iterable

import httpx

from scorecard_ai import Scorecard
from scorecard_ai._types import NOT_GIVEN, NotGiven
from scorecard_ai.lib._helpers import RunResponse, _get_run_url


class ChatMessage(TypedDict):
    """
    A message in a chat. Follows the ChatML format.
    """

    role: Literal["user", "assistant", "system", "tool"]
    content: str


def run_simulation(
    client: Scorecard,
    *,
    initial_messages: List[ChatMessage],
    system: Callable[[List[ChatMessage]], Iterable[str | ChatMessage]],
    start_with_system: bool | NotGiven = NOT_GIVEN,
    max_turns: int,
    sim_agent_version_id: str,
    testcase_id: str,
) -> List[ChatMessage]:
    """
    Runs a single simulation for a Scorecard Testcase.

    Args:
        client: The Scorecard client.

        initial_messages: A list of ChatML messages that seed the conversation
            before the simulation begins.

        system: A callable that, given the conversation so far, yields one or
            more assistant/tool messages to append when it is the system's turn.

        start_with_system: If provided, forces the conversation to start with
            the system's turn (`True`) or with the simulated agent (`False`).
            When omitted, the function infers the starting turn based on the
            role of the last message in `initial_messages`.

        max_turns: The number of turns (system plus agent) to simulate.

        sim_agent_version_id: The ID of the SystemVersion to invoke for the
            simulated agent.

        testcase_id: The ID of the Testcase being simulated.

    Returns:
        All ChatML messages exchanged during the simulation, in order.
    """
    messages = list(initial_messages)
    is_system_turn: bool
    if start_with_system is not NOT_GIVEN:
        is_system_turn = bool(start_with_system)
    else:
        is_system_turn = len(messages) > 0 and messages[-1]["role"] == "user"

    for _ in range(max_turns):
        if is_system_turn:
            # Call the system function
            system_responses = list(system(messages))
            for system_response in system_responses:
                if isinstance(system_response, str):
                    messages.append(
                        ChatMessage(role="assistant", content=system_response)
                    )
                else:
                    messages.append(system_response)
        else:
            # Call the simulated agent
            response = client.post(
                f"/agents/{sim_agent_version_id}/simulate",
                cast_to=httpx.Response,
                body={
                    "testcaseId": testcase_id,
                    "messages": messages,
                },
            )
            response.raise_for_status()
            messages.extend(response.json()["messages"])
        is_system_turn = not is_system_turn
    return messages


def multi_turn_simulation(
    client: Scorecard,
    *,
    project_id: str,
    metric_ids: List[str],
    testset_id: str,
    sim_agent_id: str,
    system: Callable[[List[ChatMessage]], Iterable[str | ChatMessage]],
    initial_messages: List[ChatMessage] | NotGiven = NOT_GIVEN,
    start_with_system: bool | NotGiven = NOT_GIVEN,
    max_turns: int = 5,
) -> RunResponse:
    """
    Simulates a multi-turn conversation for each Testcase in a Testset and
    records the results in a Scorecard Run.

    Args:
        client: The Scorecard client.

        project_id: The ID of the Project that the Run will belong to.

        metric_ids: The IDs of the Metrics that should be used to evaluate the Run.

        testset_id: The ID of the Testset whose Testcases will be executed.

        sim_agent_id: The ID of the System that represents the simulated agent.
            Its production SystemVersion will be invoked for each simulation.

        system: A callable that, given the conversation so far, yields one or
            more assistant/tool messages to append when it is the system's turn.

        initial_messages: Optional ChatML messages that seed every conversation
            before simulation begins.

        start_with_system: If provided, forces each conversation to start with
            the system's turn (`True`) or with the simulated agent (`False`).
            When omitted, the function infers the starting turn from
            `initial_messages`.

        max_turns: The maximum number of turns (system plus agent) to simulate
            for each Testcase.

    Returns:
        A `RunResponse` containing the ID and UI URL of the created Run.
    """

    system_version_id = client.systems.get(system_id=sim_agent_id).production_version.id

    run = client.runs.create(
        project_id=project_id,
        testset_id=testset_id,
        metric_ids=metric_ids,
        system_version_id=system_version_id,
    )

    # Run each Testcase sequentially
    for testcase in client.testcases.list(testset_id):
        messages = run_simulation(
            client,
            initial_messages=initial_messages or [],
            system=system,
            start_with_system=start_with_system,
            max_turns=max_turns,
            sim_agent_version_id=system_version_id,
            testcase_id=testcase.id,
        )
        client.records.create(
            run_id=run.id,
            testcase_id=testcase.id,
            inputs=testcase.inputs,
            expected=testcase.expected,
            outputs={"messages": messages},
        )

    return RunResponse(
        id=run.id,
        url=_get_run_url(client, project_id, run.id),
    )
