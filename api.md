# Shared Types

```python
from scorecard_ai.types import APIError
```

# Projects

Types:

```python
from scorecard_ai.types import Project
```

Methods:

- <code title="post /projects">client.projects.<a href="./src/scorecard_ai/resources/projects.py">create</a>(\*\*<a href="src/scorecard_ai/types/project_create_params.py">params</a>) -> <a href="./src/scorecard_ai/types/project.py">Project</a></code>
- <code title="get /projects">client.projects.<a href="./src/scorecard_ai/resources/projects.py">list</a>(\*\*<a href="src/scorecard_ai/types/project_list_params.py">params</a>) -> <a href="./src/scorecard_ai/types/project.py">SyncPaginatedResponse[Project]</a></code>

# Testsets

Types:

```python
from scorecard_ai.types import Testset, TestsetDeleteResponse
```

Methods:

- <code title="post /projects/{projectId}/testsets">client.testsets.<a href="./src/scorecard_ai/resources/testsets.py">create</a>(project_id, \*\*<a href="src/scorecard_ai/types/testset_create_params.py">params</a>) -> <a href="./src/scorecard_ai/types/testset.py">Testset</a></code>
- <code title="patch /testsets/{testsetId}">client.testsets.<a href="./src/scorecard_ai/resources/testsets.py">update</a>(testset_id, \*\*<a href="src/scorecard_ai/types/testset_update_params.py">params</a>) -> <a href="./src/scorecard_ai/types/testset.py">Testset</a></code>
- <code title="get /projects/{projectId}/testsets">client.testsets.<a href="./src/scorecard_ai/resources/testsets.py">list</a>(project_id, \*\*<a href="src/scorecard_ai/types/testset_list_params.py">params</a>) -> <a href="./src/scorecard_ai/types/testset.py">SyncPaginatedResponse[Testset]</a></code>
- <code title="delete /testsets/{testsetId}">client.testsets.<a href="./src/scorecard_ai/resources/testsets.py">delete</a>(testset_id) -> <a href="./src/scorecard_ai/types/testset_delete_response.py">TestsetDeleteResponse</a></code>
- <code title="get /testsets/{testsetId}">client.testsets.<a href="./src/scorecard_ai/resources/testsets.py">get</a>(testset_id) -> <a href="./src/scorecard_ai/types/testset.py">Testset</a></code>

# Testcases

Types:

```python
from scorecard_ai.types import Testcase, TestcaseCreateResponse, TestcaseDeleteResponse
```

Methods:

- <code title="post /testsets/{testsetId}/testcases">client.testcases.<a href="./src/scorecard_ai/resources/testcases.py">create</a>(testset_id, \*\*<a href="src/scorecard_ai/types/testcase_create_params.py">params</a>) -> <a href="./src/scorecard_ai/types/testcase_create_response.py">TestcaseCreateResponse</a></code>
- <code title="put /testcases/{testcaseId}">client.testcases.<a href="./src/scorecard_ai/resources/testcases.py">update</a>(testcase_id, \*\*<a href="src/scorecard_ai/types/testcase_update_params.py">params</a>) -> <a href="./src/scorecard_ai/types/testcase.py">Testcase</a></code>
- <code title="get /testsets/{testsetId}/testcases">client.testcases.<a href="./src/scorecard_ai/resources/testcases.py">list</a>(testset_id, \*\*<a href="src/scorecard_ai/types/testcase_list_params.py">params</a>) -> <a href="./src/scorecard_ai/types/testcase.py">SyncPaginatedResponse[Testcase]</a></code>
- <code title="post /testcases/bulk-delete">client.testcases.<a href="./src/scorecard_ai/resources/testcases.py">delete</a>(\*\*<a href="src/scorecard_ai/types/testcase_delete_params.py">params</a>) -> <a href="./src/scorecard_ai/types/testcase_delete_response.py">TestcaseDeleteResponse</a></code>
- <code title="get /testcases/{testcaseId}">client.testcases.<a href="./src/scorecard_ai/resources/testcases.py">get</a>(testcase_id) -> <a href="./src/scorecard_ai/types/testcase.py">Testcase</a></code>

# Runs

Types:

```python
from scorecard_ai.types import Run
```

Methods:

- <code title="post /projects/{projectId}/runs">client.runs.<a href="./src/scorecard_ai/resources/runs.py">create</a>(project_id, \*\*<a href="src/scorecard_ai/types/run_create_params.py">params</a>) -> <a href="./src/scorecard_ai/types/run.py">Run</a></code>

# Metrics

Types:

```python
from scorecard_ai.types import Metric
```

Methods:

- <code title="post /projects/{projectId}/metrics">client.metrics.<a href="./src/scorecard_ai/resources/metrics.py">create</a>(project_id, \*\*<a href="src/scorecard_ai/types/metric_create_params.py">params</a>) -> <a href="./src/scorecard_ai/types/metric.py">Metric</a></code>

# Records

Types:

```python
from scorecard_ai.types import Record
```

Methods:

- <code title="post /runs/{runId}/records">client.records.<a href="./src/scorecard_ai/resources/records.py">create</a>(run_id, \*\*<a href="src/scorecard_ai/types/record_create_params.py">params</a>) -> <a href="./src/scorecard_ai/types/record.py">Record</a></code>

# Scores

Types:

```python
from scorecard_ai.types import Score
```

Methods:

- <code title="put /records/{recordId}/scores/{metricConfigId}">client.scores.<a href="./src/scorecard_ai/resources/scores.py">upsert</a>(metric_config_id, \*, record_id, \*\*<a href="src/scorecard_ai/types/score_upsert_params.py">params</a>) -> <a href="./src/scorecard_ai/types/score.py">Score</a></code>

# Systems

Types:

```python
from scorecard_ai.types import System, SystemDeleteResponse
```

Methods:

- <code title="post /projects/{projectId}/systems">client.systems.<a href="./src/scorecard_ai/resources/systems/systems.py">create</a>(project_id, \*\*<a href="src/scorecard_ai/types/system_create_params.py">params</a>) -> <a href="./src/scorecard_ai/types/system.py">System</a></code>
- <code title="patch /systems/{systemId}">client.systems.<a href="./src/scorecard_ai/resources/systems/systems.py">update</a>(system_id, \*\*<a href="src/scorecard_ai/types/system_update_params.py">params</a>) -> <a href="./src/scorecard_ai/types/system.py">System</a></code>
- <code title="get /projects/{projectId}/systems">client.systems.<a href="./src/scorecard_ai/resources/systems/systems.py">list</a>(project_id, \*\*<a href="src/scorecard_ai/types/system_list_params.py">params</a>) -> <a href="./src/scorecard_ai/types/system.py">SyncPaginatedResponse[System]</a></code>
- <code title="delete /systems/{systemId}">client.systems.<a href="./src/scorecard_ai/resources/systems/systems.py">delete</a>(system_id) -> <a href="./src/scorecard_ai/types/system_delete_response.py">SystemDeleteResponse</a></code>
- <code title="get /systems/{systemId}">client.systems.<a href="./src/scorecard_ai/resources/systems/systems.py">get</a>(system_id) -> <a href="./src/scorecard_ai/types/system.py">System</a></code>

## Versions

Types:

```python
from scorecard_ai.types.systems import SystemVersion
```

Methods:

- <code title="post /systems/{systemId}/configs">client.systems.versions.<a href="./src/scorecard_ai/resources/systems/versions.py">create</a>(system_id, \*\*<a href="src/scorecard_ai/types/systems/version_create_params.py">params</a>) -> <a href="./src/scorecard_ai/types/systems/system_version.py">SystemVersion</a></code>
- <code title="get /systems/{systemId}/configs">client.systems.versions.<a href="./src/scorecard_ai/resources/systems/versions.py">list</a>(system_id, \*\*<a href="src/scorecard_ai/types/systems/version_list_params.py">params</a>) -> <a href="./src/scorecard_ai/types/systems/system_version.py">SyncPaginatedResponse[SystemVersion]</a></code>
- <code title="get /systems/configs/{systemVersionId}">client.systems.versions.<a href="./src/scorecard_ai/resources/systems/versions.py">get</a>(system_version_id) -> <a href="./src/scorecard_ai/types/systems/system_version.py">SystemVersion</a></code>
