from __future__ import annotations

from types import SimpleNamespace
from contextlib import ExitStack
from unittest.mock import patch

import httpx
import pytest
from respx import MockRouter

from scorecard_ai import Scorecard, AsyncScorecard
from scorecard_ai.lib._helpers import SystemInput, _get_run_url, run_and_evaluate, async_run_and_evaluate
from scorecard_ai.lib._multi_turn_simulation import ChatMessage, multi_turn_simulation


@pytest.fixture(autouse=True)
def clear_url_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SCORECARD_BASE_URL", raising=False)
    monkeypatch.delenv("SCORECARD_APP_URL", raising=False)


@pytest.mark.parametrize(
    "base_url, app_url",
    [
        ("https://api2.scorecard.io/api/v2", "https://app.scorecard.io"),
        ("https://api2.scorecard.io/api/v2/", "https://app.scorecard.io"),
        ("https://staging.api2.scorecard.io/api/v2", "https://staging.app.getscorecard.ai"),
        ("HTTPS://API2.SCORECARD.IO/api/v2///", "https://app.scorecard.io"),
        ("HTTPS://STAGING.API2.SCORECARD.IO/api/v2///", "https://staging.app.getscorecard.ai"),
        ("HTTP://LOCALHOST:3000/api/v2///", "http://localhost:3002"),
        ("https://staging.api2.scorecard.io/API/v2", "https://app.scorecard.io"),
        ("http://localhost:3000/api/v2", "http://localhost:3002"),
        ("http://localhost:8000/api/v2", "https://app.scorecard.io"),
        ("http://127.0.0.1:8000/api/v2/", "https://app.scorecard.io"),
        ("https://custom.example/api/v2", "https://app.scorecard.io"),
    ],
)
@pytest.mark.parametrize("from_env", [False, True])
@pytest.mark.parametrize("client_class", [Scorecard, AsyncScorecard])
def test_run_url(
    monkeypatch: pytest.MonkeyPatch,
    base_url: str,
    app_url: str,
    from_env: bool,
    client_class: type[Scorecard] | type[AsyncScorecard],
) -> None:
    if from_env:
        monkeypatch.setenv("SCORECARD_BASE_URL", base_url)
        client = client_class(api_key="test")
    else:
        client = client_class(api_key="test", base_url=base_url)
    assert _get_run_url(client, "project", "run") == f"{app_url}/projects/project/runs/run"


@pytest.mark.parametrize("client_class", [Scorecard, AsyncScorecard])
@pytest.mark.parametrize("base_url", ["https://api2.scorecard.io/api/v2", "http://localhost:8000/api/v2"])
@pytest.mark.parametrize("app_url", ["https://custom-app.example/ui/", "HTTPS://Custom-App.Example/UI///"])
def test_run_url_app_override(
    monkeypatch: pytest.MonkeyPatch,
    client_class: type[Scorecard] | type[AsyncScorecard],
    base_url: str,
    app_url: str,
) -> None:
    monkeypatch.setenv("SCORECARD_APP_URL", app_url)
    client = client_class(api_key="test", base_url=base_url)
    assert _get_run_url(client, "project", "run") == f"{app_url.rstrip('/')}/projects/project/runs/run"


def test_run_and_evaluate_url(respx_mock: MockRouter) -> None:
    respx_mock.post("http://localhost:8000/api/v2/projects/project/runs").mock(
        return_value=httpx.Response(200, json={"id": "run"})
    )
    with Scorecard(api_key="test", base_url="http://localhost:8000/api/v2") as client:
        result = run_and_evaluate(client, project_id="project", metric_ids=[], testcases=[], system=lambda *_: {})
    assert result == {"id": "run", "url": "https://app.scorecard.io/projects/project/runs/run"}


async def test_async_run_and_evaluate_url(respx_mock: MockRouter) -> None:
    respx_mock.post("http://localhost:8000/api/v2/projects/project/runs").mock(
        return_value=httpx.Response(200, json={"id": "run"})
    )
    async with AsyncScorecard(api_key="test", base_url="http://localhost:8000/api/v2") as client:
        result = await async_run_and_evaluate(
            client, project_id="project", metric_ids=[], testcases=[], system=lambda *_: {}
        )
    assert result == {"id": "run", "url": "https://app.scorecard.io/projects/project/runs/run"}


def test_multi_turn_simulation_url() -> None:
    def system(_messages: list[ChatMessage], _inputs: SystemInput) -> list[ChatMessage]:
        return []

    with Scorecard(api_key="test", base_url="http://localhost:8000/api/v2") as client:
        with ExitStack() as mocks:
            mocks.enter_context(
                patch.object(
                    client.systems, "get", return_value=SimpleNamespace(production_version=SimpleNamespace(id="v"))
                )
            )
            mocks.enter_context(patch.object(client.runs, "create", return_value=SimpleNamespace(id="run")))
            mocks.enter_context(patch.object(client.testcases, "list", return_value=[]))
            result = multi_turn_simulation(
                client,
                project_id="project",
                metric_ids=[],
                testset_id="testset",
                sim_agent_id="agent",
                system=system,
            )
    assert result == {"id": "run", "url": "https://app.scorecard.io/projects/project/runs/run"}
