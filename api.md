# Shared Types

```python
from scorecardpy.types import APIError
```

# Projects

Types:

```python
from scorecardpy.types import ProjectListResponse
```

Methods:

- <code title="get /projects">client.projects.<a href="./src/scorecardpy/resources/projects.py">list</a>(\*\*<a href="src/scorecardpy/types/project_list_params.py">params</a>) -> <a href="./src/scorecardpy/types/project_list_response.py">SyncPaginatedResponse[ProjectListResponse]</a></code>

# Testsets

Types:

```python
from scorecardpy.types import Testset, TestsetDeleteResponse
```

Methods:

- <code title="post /projects/{projectId}/testsets">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">create</a>(project_id, \*\*<a href="src/scorecardpy/types/testset_create_params.py">params</a>) -> <a href="./src/scorecardpy/types/testset.py">Testset</a></code>
- <code title="patch /testsets/{testsetId}">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">update</a>(testset_id, \*\*<a href="src/scorecardpy/types/testset_update_params.py">params</a>) -> <a href="./src/scorecardpy/types/testset.py">Testset</a></code>
- <code title="get /projects/{projectId}/testsets">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">list</a>(project_id, \*\*<a href="src/scorecardpy/types/testset_list_params.py">params</a>) -> <a href="./src/scorecardpy/types/testset.py">SyncPaginatedResponse[Testset]</a></code>
- <code title="delete /testsets/{testsetId}">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">delete</a>(testset_id) -> <a href="./src/scorecardpy/types/testset_delete_response.py">TestsetDeleteResponse</a></code>
- <code title="get /testsets/{testsetId}">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">get</a>(testset_id) -> <a href="./src/scorecardpy/types/testset.py">Testset</a></code>

# Testcases

Types:

```python
from scorecardpy.types import Testcase, TestcaseCreateResponse, TestcaseDeleteResponse
```

Methods:

- <code title="post /testsets/{testsetId}/testcases">client.testcases.<a href="./src/scorecardpy/resources/testcases.py">create</a>(testset_id, \*\*<a href="src/scorecardpy/types/testcase_create_params.py">params</a>) -> <a href="./src/scorecardpy/types/testcase_create_response.py">TestcaseCreateResponse</a></code>
- <code title="put /testcases/{testcaseId}">client.testcases.<a href="./src/scorecardpy/resources/testcases.py">update</a>(testcase_id, \*\*<a href="src/scorecardpy/types/testcase_update_params.py">params</a>) -> <a href="./src/scorecardpy/types/testcase.py">Testcase</a></code>
- <code title="get /testsets/{testsetId}/testcases">client.testcases.<a href="./src/scorecardpy/resources/testcases.py">list</a>(testset_id, \*\*<a href="src/scorecardpy/types/testcase_list_params.py">params</a>) -> <a href="./src/scorecardpy/types/testcase.py">SyncPaginatedResponse[Testcase]</a></code>
- <code title="post /testcases/bulk-delete">client.testcases.<a href="./src/scorecardpy/resources/testcases.py">delete</a>(\*\*<a href="src/scorecardpy/types/testcase_delete_params.py">params</a>) -> <a href="./src/scorecardpy/types/testcase_delete_response.py">TestcaseDeleteResponse</a></code>
- <code title="get /testcases/{testcaseId}">client.testcases.<a href="./src/scorecardpy/resources/testcases.py">get</a>(testcase_id) -> <a href="./src/scorecardpy/types/testcase.py">Testcase</a></code>

# Runs

Types:

```python
from scorecardpy.types import Run
```

Methods:

- <code title="post /projects/{projectId}/runs">client.runs.<a href="./src/scorecardpy/resources/runs.py">create</a>(project_id, \*\*<a href="src/scorecardpy/types/run_create_params.py">params</a>) -> <a href="./src/scorecardpy/types/run.py">Run</a></code>

# ExecutionRecords

Types:

```python
from scorecardpy.types import ExecutionRecord
```

Methods:

- <code title="post /runs/{runId}/executionrecords">client.execution_records.<a href="./src/scorecardpy/resources/execution_records.py">create</a>(run_id, \*\*<a href="src/scorecardpy/types/execution_record_create_params.py">params</a>) -> <a href="./src/scorecardpy/types/execution_record.py">ExecutionRecord</a></code>

# Systems

Types:

```python
from scorecardpy.types import System, SystemDeleteResponse
```

Methods:

- <code title="post /projects/{projectId}/systems">client.systems.<a href="./src/scorecardpy/resources/systems.py">create</a>(project_id, \*\*<a href="src/scorecardpy/types/system_create_params.py">params</a>) -> <a href="./src/scorecardpy/types/system.py">System</a></code>
- <code title="patch /systems/{systemId}">client.systems.<a href="./src/scorecardpy/resources/systems.py">update</a>(system_id, \*\*<a href="src/scorecardpy/types/system_update_params.py">params</a>) -> <a href="./src/scorecardpy/types/system.py">System</a></code>
- <code title="get /projects/{projectId}/systems">client.systems.<a href="./src/scorecardpy/resources/systems.py">list</a>(project_id, \*\*<a href="src/scorecardpy/types/system_list_params.py">params</a>) -> <a href="./src/scorecardpy/types/system.py">SyncPaginatedResponse[System]</a></code>
- <code title="delete /systems/{systemId}">client.systems.<a href="./src/scorecardpy/resources/systems.py">delete</a>(system_id) -> <a href="./src/scorecardpy/types/system_delete_response.py">SystemDeleteResponse</a></code>
- <code title="get /systems/{systemId}">client.systems.<a href="./src/scorecardpy/resources/systems.py">get</a>(system_id) -> <a href="./src/scorecardpy/types/system.py">System</a></code>

# SystemConfigs

Types:

```python
from scorecardpy.types import SystemConfig
```

Methods:

- <code title="post /systems/{systemId}/configs">client.system_configs.<a href="./src/scorecardpy/resources/system_configs.py">create</a>(system_id, \*\*<a href="src/scorecardpy/types/system_config_create_params.py">params</a>) -> <a href="./src/scorecardpy/types/system_config.py">SystemConfig</a></code>
- <code title="get /systems/{systemId}/configs">client.system_configs.<a href="./src/scorecardpy/resources/system_configs.py">list</a>(system_id, \*\*<a href="src/scorecardpy/types/system_config_list_params.py">params</a>) -> <a href="./src/scorecardpy/types/system_config.py">SyncPaginatedResponse[SystemConfig]</a></code>
- <code title="get /systems/{systemId}/configs/{systemConfigId}">client.system_configs.<a href="./src/scorecardpy/resources/system_configs.py">get</a>(system_config_id, \*, system_id) -> <a href="./src/scorecardpy/types/system_config.py">SystemConfig</a></code>
