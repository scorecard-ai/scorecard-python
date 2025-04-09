# Shared Types

```python
from scorecardpy.types import APIError, Testset
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
from scorecardpy.types import (
    TestsetDeleteResponse,
    TestsetCreateTestcasesResponse,
    TestsetDeleteTestcasesResponse,
)
```

Methods:

- <code title="post /projects/{projectId}/testsets">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">create</a>(project_id, \*\*<a href="src/scorecardpy/types/testset_create_params.py">params</a>) -> <a href="./src/scorecardpy/types/shared/testset.py">Testset</a></code>
- <code title="patch /testsets/{testsetId}">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">update</a>(testset_id, \*\*<a href="src/scorecardpy/types/testset_update_params.py">params</a>) -> <a href="./src/scorecardpy/types/shared/testset.py">Testset</a></code>
- <code title="get /projects/{projectId}/testsets">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">list</a>(project_id, \*\*<a href="src/scorecardpy/types/testset_list_params.py">params</a>) -> <a href="./src/scorecardpy/types/shared/testset.py">SyncPaginatedResponse[Testset]</a></code>
- <code title="delete /testsets/{testsetId}">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">delete</a>(testset_id) -> <a href="./src/scorecardpy/types/testset_delete_response.py">TestsetDeleteResponse</a></code>
- <code title="post /testsets/{testsetId}/testcases">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">create_testcases</a>(testset_id, \*\*<a href="src/scorecardpy/types/testset_create_testcases_params.py">params</a>) -> <a href="./src/scorecardpy/types/testset_create_testcases_response.py">TestsetCreateTestcasesResponse</a></code>
- <code title="delete /testsets/{testsetId}/testcases">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">delete_testcases</a>(testset_id, \*\*<a href="src/scorecardpy/types/testset_delete_testcases_params.py">params</a>) -> <a href="./src/scorecardpy/types/testset_delete_testcases_response.py">TestsetDeleteTestcasesResponse</a></code>
- <code title="get /testsets/{testsetId}">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">get</a>(testset_id) -> <a href="./src/scorecardpy/types/shared/testset.py">Testset</a></code>
- <code title="get /testsets/{testsetId}/testcases">client.testsets.<a href="./src/scorecardpy/resources/testsets.py">list_testcases</a>(testset_id, \*\*<a href="src/scorecardpy/types/testset_list_testcases_params.py">params</a>) -> <a href="./src/scorecardpy/types/testcase.py">SyncPaginatedResponse[Testcase]</a></code>

# Testcases

Types:

```python
from scorecardpy.types import Testcase
```

Methods:

- <code title="put /testcases/{testcaseId}">client.testcases.<a href="./src/scorecardpy/resources/testcases.py">update</a>(testcase_id, \*\*<a href="src/scorecardpy/types/testcase_update_params.py">params</a>) -> <a href="./src/scorecardpy/types/testcase.py">Testcase</a></code>
- <code title="get /testcases/{testcaseId}">client.testcases.<a href="./src/scorecardpy/resources/testcases.py">get</a>(testcase_id) -> <a href="./src/scorecardpy/types/testcase.py">Testcase</a></code>
