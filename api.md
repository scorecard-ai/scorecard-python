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
from scorecardpy.types import (
    TestsetCreateResponse,
    TestsetRetrieveResponse,
    TestsetUpdateResponse,
    TestsetListResponse,
    TestsetDeleteResponse,
)
```

Methods:

- <code title="post /projects/{projectId}/testsets">client.testsets.<a href="./src/scorecardpy/resources/testsets/testsets.py">create</a>(project_id, \*\*<a href="src/scorecardpy/types/testset_create_params.py">params</a>) -> <a href="./src/scorecardpy/types/testset_create_response.py">TestsetCreateResponse</a></code>
- <code title="get /testsets/{testsetId}">client.testsets.<a href="./src/scorecardpy/resources/testsets/testsets.py">retrieve</a>(testset_id) -> <a href="./src/scorecardpy/types/testset_retrieve_response.py">TestsetRetrieveResponse</a></code>
- <code title="patch /testsets/{testsetId}">client.testsets.<a href="./src/scorecardpy/resources/testsets/testsets.py">update</a>(testset_id, \*\*<a href="src/scorecardpy/types/testset_update_params.py">params</a>) -> <a href="./src/scorecardpy/types/testset_update_response.py">TestsetUpdateResponse</a></code>
- <code title="get /projects/{projectId}/testsets">client.testsets.<a href="./src/scorecardpy/resources/testsets/testsets.py">list</a>(project_id, \*\*<a href="src/scorecardpy/types/testset_list_params.py">params</a>) -> <a href="./src/scorecardpy/types/testset_list_response.py">SyncPaginatedResponse[TestsetListResponse]</a></code>
- <code title="delete /testsets/{testsetId}">client.testsets.<a href="./src/scorecardpy/resources/testsets/testsets.py">delete</a>(testset_id) -> <a href="./src/scorecardpy/types/testset_delete_response.py">TestsetDeleteResponse</a></code>

## Testcases

Types:

```python
from scorecardpy.types.testsets import (
    TestcaseCreateResponse,
    TestcaseListResponse,
    TestcaseDeleteResponse,
)
```

Methods:

- <code title="post /testsets/{testsetId}/testcases">client.testsets.testcases.<a href="./src/scorecardpy/resources/testsets/testcases.py">create</a>(testset_id, \*\*<a href="src/scorecardpy/types/testsets/testcase_create_params.py">params</a>) -> <a href="./src/scorecardpy/types/testsets/testcase_create_response.py">TestcaseCreateResponse</a></code>
- <code title="get /testsets/{testsetId}/testcases">client.testsets.testcases.<a href="./src/scorecardpy/resources/testsets/testcases.py">list</a>(testset_id, \*\*<a href="src/scorecardpy/types/testsets/testcase_list_params.py">params</a>) -> <a href="./src/scorecardpy/types/testsets/testcase_list_response.py">SyncPaginatedResponse[TestcaseListResponse]</a></code>
- <code title="delete /testsets/{testsetId}/testcases">client.testsets.testcases.<a href="./src/scorecardpy/resources/testsets/testcases.py">delete</a>(testset_id, \*\*<a href="src/scorecardpy/types/testsets/testcase_delete_params.py">params</a>) -> <a href="./src/scorecardpy/types/testsets/testcase_delete_response.py">TestcaseDeleteResponse</a></code>

# Testcases

Types:

```python
from scorecardpy.types import TestcaseRetrieveResponse, TestcaseUpdateResponse
```

Methods:

- <code title="get /testcases/{testcaseId}">client.testcases.<a href="./src/scorecardpy/resources/testcases.py">retrieve</a>(testcase_id) -> <a href="./src/scorecardpy/types/testcase_retrieve_response.py">TestcaseRetrieveResponse</a></code>
- <code title="put /testcases/{testcaseId}">client.testcases.<a href="./src/scorecardpy/resources/testcases.py">update</a>(testcase_id, \*\*<a href="src/scorecardpy/types/testcase_update_params.py">params</a>) -> <a href="./src/scorecardpy/types/testcase_update_response.py">TestcaseUpdateResponse</a></code>
