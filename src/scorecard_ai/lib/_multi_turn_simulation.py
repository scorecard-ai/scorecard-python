"""
Multi-turn simulation.
"""

from __future__ import annotations

import time
from typing import List, Literal, Callable, TypedDict
from collections.abc import Iterable

import httpx

from scorecard_ai import Scorecard
from scorecard_ai._types import NOT_GIVEN, NotGiven
from scorecard_ai.lib._helpers import RunResponse, SystemInput, _get_run_url
from scorecard_ai.types.testcase import Testcase


class ChatMessage(TypedDict):
    """
    A message in a chat. Follows the ChatML format.
    """

    role: Literal["user", "assistant", "system", "tool"]
    """
    The role of the message.

    The simulated user's messages are `"user"`.
    The assistant's (system under test) messages are `"assistant"`.

    The simulated user ignores any messages with roles `"system"` or `"tool"`.
    """
    content: str
    """
    The content of the message.
    """


class ConversationInfo(TypedDict):
    """
    Information about the simulated conversation so far.
    """

    messages: List[ChatMessage]
    """
    The messages exchanged so far.
    """
    turn_count: int
    """
    Number of turns in the conversation.
    One turn is a system call plus simulated agent call.
    Does not count the initial messages as turns.
    """
    is_system_turn: bool
    """
    Whether the current turn is the system's turn.
    """
    time_elapsed: float
    """
    The number of seconds since the simulation began.
    """


StopCheck = Callable[[ConversationInfo], bool]
"""
A function that, given the conversation info so far, returns `True` if the simulation should end.

```python
# Example: Stop after 5 turns
stop_check = lambda info: info["turn_count"] >= 5
```
"""


class StopChecks:
    """
    A collection of common stop checks.

    For example, set `stop_check=StopChecks.max_turns(5)` to end the simulation after 5 turns.
    """

    @staticmethod
    def max_turns(max_turns: int) -> StopCheck:
        """
        End the simulation after a given number of turns, not including any initial messages.

        ```python
        # Stop after 5 turns
        stop_check = StopChecks.max_turns(5)
        ```
        """
        if max_turns <= 0:
            raise ValueError("max_turns must be positive")
        return lambda info: info["turn_count"] >= max_turns

    @staticmethod
    def content(stop_phrases: List[str]) -> StopCheck:
        """
        End the simulation when a given substring appears in the conversation, case-insensitive.

        ```python
        # End the simulation when any stop words appear in the conversation
        stop_check = StopChecks.content(["stop", "bye"])
        ```
        """
        phrases = set(phrase.lower() for phrase in stop_phrases)
        return lambda info: any(
            any(phrase in message["content"].lower() for phrase in phrases) for message in info["messages"]
        )

    @staticmethod
    def max_time(max_seconds: float) -> StopCheck:
        """
        End the simulation when the conversation has lasted for more than a given number of seconds.

        ```python
        # Stop after 20 seconds
        stop_check = StopChecks.max_time(20)
        ```
        """
        return lambda info: info["time_elapsed"] >= max_seconds

    @staticmethod
    def all(criteria: Iterable[StopCheck]) -> StopCheck:
        """
        End the simulation when all of the given stop checks are met.

        ```python
        # Stop after at least 5 turns and 20 seconds (whichever comes later)
        stop_check = StopChecks.all(
            [
                StopChecks.max_turns(5),
                StopChecks.max_time(20),
            ]
        )
        ```
        """
        return lambda info: all(criterion(info) for criterion in criteria)

    @staticmethod
    def any(criteria: Iterable[StopCheck]) -> StopCheck:
        """
        End the simulation when any of the given stop checks are met.

        ```python
        # Stop after 5 turns or 20 seconds (whichever comes first)
        stop_check = StopChecks.any(
            [
                StopChecks.max_turns(5),
                StopChecks.max_time(10),
            ]
        )
        ```
        """
        return lambda info: any(criterion(info) for criterion in criteria)


MAX_TURNS = 100


def _run_simulation(
    client: Scorecard,
    *,
    initial_messages: List[ChatMessage],
    system: Callable[[List[ChatMessage], SystemInput], Iterable[str | ChatMessage]],
    start_with_system: bool | NotGiven,
    sim_agent_version_id: str,
    testcase: Testcase,
    stop_check: StopCheck,
) -> List[ChatMessage]:
    """
    Runs a single simulation for a Scorecard Testcase.
    """
    messages = list(initial_messages)
    is_system_turn: bool
    if isinstance(start_with_system, NotGiven):
        is_system_turn = len(messages) > 0 and messages[-1]["role"] == "user"
    else:
        is_system_turn = bool(start_with_system)

    start_time = time.time()

    # A full turn consists of one system response and one agent response.
    # The loop iterates up to MAX_TURNS half-turns to prevent infinite conversation loops.
    for turn_index in range(MAX_TURNS):
        stop_check_start_time = time.time()
        if stop_check(
            ConversationInfo(
                messages=list(messages),
                turn_count=turn_index // 2,
                is_system_turn=is_system_turn,
                time_elapsed=stop_check_start_time - start_time,
            )
        ):
            # End the simulation
            break
        # Do not count the time spent in the stop check towards the simulation's time
        start_time += time.time() - stop_check_start_time

        if is_system_turn:
            # Call the system function
            for system_response in system(messages, testcase.inputs):
                if isinstance(system_response, str):
                    messages.append(ChatMessage(role="assistant", content=system_response))
                else:
                    messages.append(system_response)
        else:
            # Call the simulated agent
            response = client.post(
                f"/agents/{sim_agent_version_id}/simulate",
                cast_to=httpx.Response,
                body={
                    "testcaseId": testcase.id,
                    "messages": messages,
                },
            )
            response.raise_for_status()
            messages.extend(response.json()["messages"])
        is_system_turn = not is_system_turn

    return messages


DEFAULT_STOP_CHECK = StopChecks.max_turns(5)


def multi_turn_simulation(
    client: Scorecard,
    *,
    project_id: str,
    metric_ids: List[str],
    testset_id: str,
    sim_agent_id: str,
    system: Callable[[List[ChatMessage], SystemInput], Iterable[str | ChatMessage]],
    initial_messages: (List[ChatMessage] | Callable[[SystemInput], List[ChatMessage]] | NotGiven) = NOT_GIVEN,
    start_with_system: bool | NotGiven = NOT_GIVEN,
    stop_check: StopCheck = DEFAULT_STOP_CHECK,
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
            The second argument is the Testcase's inputs.

        initial_messages: ChatMessages that seed a conversation
            before simulation begins. If a callable, it will be called with the
            Testcase's inputs to get the initial messages.

        start_with_system: If provided, forces each conversation to start with
            the system's turn (`True`) or with the simulated agent (`False`).
            When omitted, the function infers the starting turn from
            `initial_messages` if provided and defaults to the user's turn.

        stop_check: A callable that ends the simulation when it returns `True`.
            See `StopChecks` for common stop checks. Defaults to stopping after 5 turns.

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
        starting_messages: list[ChatMessage]
        if isinstance(initial_messages, NotGiven):
            starting_messages = []
        elif callable(initial_messages):
            starting_messages = initial_messages(testcase.inputs)
        else:
            starting_messages = initial_messages

        messages = _run_simulation(
            client,
            initial_messages=starting_messages,
            system=system,
            start_with_system=start_with_system,
            sim_agent_version_id=system_version_id,
            testcase=testcase,
            stop_check=stop_check,
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
