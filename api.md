# Welcome

Types:

```python
from scorecard.types import WelcomeRetrieveResponse
```

Methods:

- <code title="get /v1/">client.welcome.<a href="./src/scorecard/resources/welcome.py">retrieve</a>() -> <a href="./src/scorecard/types/welcome_retrieve_response.py">object</a></code>

# RunMetric

Types:

```python
from scorecard.types import RunMetricRetrieveResponse
```

Methods:

- <code title="get /v1/run_metric/{run_id}">client.run_metric.<a href="./src/scorecard/resources/run_metric.py">retrieve</a>(run_id) -> <a href="./src/scorecard/types/run_metric_retrieve_response.py">RunMetricRetrieveResponse</a></code>

# Testset

Types:

```python
from scorecard.types import Testset, TestsetListResponse, TestsetGetSchemaResponse
```

Methods:

- <code title="post /v1/testset">client.testset.<a href="./src/scorecard/resources/testset/testset.py">create</a>(\*\*<a href="src/scorecard/types/testset_create_params.py">params</a>) -> <a href="./src/scorecard/types/testset/testset.py">Testset</a></code>
- <code title="get /v1/testset/{testset_id}">client.testset.<a href="./src/scorecard/resources/testset/testset.py">retrieve</a>(testset_id) -> <a href="./src/scorecard/types/testset/testset.py">Testset</a></code>
- <code title="patch /v1/testset/{testset_id}">client.testset.<a href="./src/scorecard/resources/testset/testset.py">update</a>(testset_id, \*\*<a href="src/scorecard/types/testset_update_params.py">params</a>) -> <a href="./src/scorecard/types/testset/testset.py">Testset</a></code>
- <code title="get /v1/testset">client.testset.<a href="./src/scorecard/resources/testset/testset.py">list</a>(\*\*<a href="src/scorecard/types/testset_list_params.py">params</a>) -> <a href="./src/scorecard/types/testset_list_response.py">TestsetListResponse</a></code>
- <code title="delete /v1/testset/{testset_id}">client.testset.<a href="./src/scorecard/resources/testset/testset.py">delete</a>(testset_id) -> <a href="./src/scorecard/types/testset/testset.py">Testset</a></code>
- <code title="get /v1/testset/{testset_id}/schema">client.testset.<a href="./src/scorecard/resources/testset/testset.py">get_schema</a>(testset_id) -> <a href="./src/scorecard/types/testset_get_schema_response.py">TestsetGetSchemaResponse</a></code>

## Testcase

Types:

```python
from scorecard.types.testset import (
    TestCase,
    TestcaseListResponse,
    TestcaseDeleteResponse,
    TestcaseBatchCopyResponse,
    TestcaseBatchDeleteResponse,
)
```

Methods:

- <code title="post /v1/testset/{testset_id}/testcase">client.testset.testcase.<a href="./src/scorecard/resources/testset/testcase.py">create</a>(testset_id, \*\*<a href="src/scorecard/types/testset/testcase_create_params.py">params</a>) -> <a href="./src/scorecard/types/testset/test_case.py">TestCase</a></code>
- <code title="get /v1/testset/{testset_id}/testcase/{testcase_id}">client.testset.testcase.<a href="./src/scorecard/resources/testset/testcase.py">retrieve</a>(testcase_id, \*, testset_id) -> <a href="./src/scorecard/types/testset/test_case.py">TestCase</a></code>
- <code title="patch /v1/testset/{testset_id}/testcase/{testcase_id}">client.testset.testcase.<a href="./src/scorecard/resources/testset/testcase.py">update</a>(testcase_id, \*, testset_id, \*\*<a href="src/scorecard/types/testset/testcase_update_params.py">params</a>) -> <a href="./src/scorecard/types/testset/test_case.py">TestCase</a></code>
- <code title="get /v1/testset/{testset_id}/testcase">client.testset.testcase.<a href="./src/scorecard/resources/testset/testcase.py">list</a>(testset_id, \*\*<a href="src/scorecard/types/testset/testcase_list_params.py">params</a>) -> <a href="./src/scorecard/types/testset/testcase_list_response.py">TestcaseListResponse</a></code>
- <code title="delete /v1/testset/{testset_id}/testcase/{testcase_id}">client.testset.testcase.<a href="./src/scorecard/resources/testset/testcase.py">delete</a>(testcase_id, \*, testset_id) -> <a href="./src/scorecard/types/testset/testcase_delete_response.py">TestcaseDeleteResponse</a></code>
- <code title="post /v1/testset/{testset_id}/testcase/batch_copy">client.testset.testcase.<a href="./src/scorecard/resources/testset/testcase.py">batch_copy</a>(testset_id, \*\*<a href="src/scorecard/types/testset/testcase_batch_copy_params.py">params</a>) -> <a href="./src/scorecard/types/testset/testcase_batch_copy_response.py">TestcaseBatchCopyResponse</a></code>
- <code title="patch /v1/testset/{testset_id}/testcase/batch_delete">client.testset.testcase.<a href="./src/scorecard/resources/testset/testcase.py">batch_delete</a>(testset_id, \*\*<a href="src/scorecard/types/testset/testcase_batch_delete_params.py">params</a>) -> <a href="./src/scorecard/types/testset/testcase_batch_delete_response.py">TestcaseBatchDeleteResponse</a></code>

# Run

Types:

```python
from scorecard.types import Run
```

Methods:

- <code title="post /v1/run">client.run.<a href="./src/scorecard/resources/run/run.py">create</a>(\*\*<a href="src/scorecard/types/run_create_params.py">params</a>) -> <a href="./src/scorecard/types/run/run.py">Run</a></code>
- <code title="get /v1/run/{run_id}">client.run.<a href="./src/scorecard/resources/run/run.py">retrieve</a>(run_id) -> <a href="./src/scorecard/types/run/run.py">Run</a></code>
- <code title="patch /v1/run/{run_id}/status">client.run.<a href="./src/scorecard/resources/run/run.py">update_status</a>(run_id, \*\*<a href="src/scorecard/types/run_update_status_params.py">params</a>) -> <a href="./src/scorecard/types/run/run.py">Run</a></code>

## Testrecord

Types:

```python
from scorecard.types.run import Testrecord
```

Methods:

- <code title="post /v1/run/{run_id}/testrecord">client.run.testrecord.<a href="./src/scorecard/resources/run/testrecord/testrecord.py">create</a>(run_id, \*\*<a href="src/scorecard/types/run/testrecord_create_params.py">params</a>) -> <a href="./src/scorecard/types/run/testrecord/testrecord.py">Testrecord</a></code>
- <code title="get /v1/run/{run_id}/testrecord/{testrecord_id}">client.run.testrecord.<a href="./src/scorecard/resources/run/testrecord/testrecord.py">retrieve</a>(testrecord_id, \*, run_id) -> <a href="./src/scorecard/types/run/testrecord/testrecord.py">Testrecord</a></code>

### Score

Types:

```python
from scorecard.types.run.testrecord import Grade
```

Methods:

- <code title="post /v1/run/{run_id}/testrecord/{testrecord_id}/score">client.run.testrecord.score.<a href="./src/scorecard/resources/run/testrecord/score.py">create</a>(testrecord_id, \*, run_id, \*\*<a href="src/scorecard/types/run/testrecord/score_create_params.py">params</a>) -> <a href="./src/scorecard/types/run/testrecord/grade.py">Grade</a></code>
- <code title="patch /v1/run/{run_id}/testrecord/{testrecord_id}/score/{score_id}">client.run.testrecord.score.<a href="./src/scorecard/resources/run/testrecord/score.py">update</a>(score_id, \*, run_id, testrecord_id, \*\*<a href="src/scorecard/types/run/testrecord/score_update_params.py">params</a>) -> <a href="./src/scorecard/types/run/testrecord/grade.py">Grade</a></code>

# Traces

Types:

```python
from scorecard.types import Trace, TraceListResponse, TraceRetrieveSpanResponse
```

Methods:

- <code title="get /v1/traces/{trace_id}">client.traces.<a href="./src/scorecard/resources/traces.py">retrieve</a>(trace_id) -> <a href="./src/scorecard/types/trace.py">Trace</a></code>
- <code title="get /v1/traces">client.traces.<a href="./src/scorecard/resources/traces.py">list</a>() -> <a href="./src/scorecard/types/trace_list_response.py">TraceListResponse</a></code>
- <code title="get /v1/traces/{trace_id}/spans/{span_id}">client.traces.<a href="./src/scorecard/resources/traces.py">retrieve_span</a>(span_id, \*, trace_id) -> <a href="./src/scorecard/types/trace_retrieve_span_response.py">TraceRetrieveSpanResponse</a></code>

# Prompt

Types:

```python
from scorecard.types import Prompt, PromptListResponse, PromptDeleteRootResponse
```

Methods:

- <code title="post /v1/prompt">client.prompt.<a href="./src/scorecard/resources/prompt.py">create</a>(\*\*<a href="src/scorecard/types/prompt_create_params.py">params</a>) -> <a href="./src/scorecard/types/prompt.py">Prompt</a></code>
- <code title="patch /v1/prompt/{id}">client.prompt.<a href="./src/scorecard/resources/prompt.py">update</a>(id, \*\*<a href="src/scorecard/types/prompt_update_params.py">params</a>) -> <a href="./src/scorecard/types/prompt.py">Prompt</a></code>
- <code title="get /v1/prompt/list">client.prompt.<a href="./src/scorecard/resources/prompt.py">list</a>(\*\*<a href="src/scorecard/types/prompt_list_params.py">params</a>) -> <a href="./src/scorecard/types/prompt_list_response.py">PromptListResponse</a></code>
- <code title="delete /v1/prompt/{id}">client.prompt.<a href="./src/scorecard/resources/prompt.py">delete_root</a>(id) -> <a href="./src/scorecard/types/prompt_delete_root_response.py">object</a></code>
- <code title="get /v1/prompt/{id}">client.prompt.<a href="./src/scorecard/resources/prompt.py">retrieve_by_id</a>(id) -> <a href="./src/scorecard/types/prompt.py">Prompt</a></code>
- <code title="get /v1/prompt">client.prompt.<a href="./src/scorecard/resources/prompt.py">retrieve_by_name</a>(\*\*<a href="src/scorecard/types/prompt_retrieve_by_name_params.py">params</a>) -> <a href="./src/scorecard/types/prompt.py">Prompt</a></code>

# ScoringConfig

Types:

```python
from scorecard.types import ScoringConfig, ScoringConfigDeleteResponse
```

Methods:

- <code title="post /v1/scoring_config">client.scoring_config.<a href="./src/scorecard/resources/scoring_config.py">create</a>(\*\*<a href="src/scorecard/types/scoring_config_create_params.py">params</a>) -> <a href="./src/scorecard/types/scoring_config.py">ScoringConfig</a></code>
- <code title="get /v1/scoring_config/{id}">client.scoring_config.<a href="./src/scorecard/resources/scoring_config.py">retrieve</a>(id) -> <a href="./src/scorecard/types/scoring_config.py">ScoringConfig</a></code>
- <code title="delete /v1/scoring_config/{id}">client.scoring_config.<a href="./src/scorecard/resources/scoring_config.py">delete</a>(id) -> <a href="./src/scorecard/types/scoring_config_delete_response.py">object</a></code>
