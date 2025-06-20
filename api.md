# Search

Types:

```python
from openregister.types import (
    CompanyLegalForm,
    CompanyRegisterType,
    SearchFindCompaniesResponse,
    SearchLookupCompanyByURLResponse,
)
```

Methods:

- <code title="get /v0/search/company">client.search.<a href="./src/openregister/resources/search.py">find_companies</a>(\*\*<a href="src/openregister/types/search_find_companies_params.py">params</a>) -> <a href="./src/openregister/types/search_find_companies_response.py">SearchFindCompaniesResponse</a></code>
- <code title="get /v0/search/lookup">client.search.<a href="./src/openregister/resources/search.py">lookup_company_by_url</a>(\*\*<a href="src/openregister/types/search_lookup_company_by_url_params.py">params</a>) -> <a href="./src/openregister/types/search_lookup_company_by_url_response.py">SearchLookupCompanyByURLResponse</a></code>

# Company

Types:

```python
from openregister.types import (
    CompanyAddress,
    CompanyCapital,
    CompanyName,
    CompanyPurpose,
    CompanyRegister,
    EntityType,
    CompanyRetrieveResponse,
    CompanyListShareholdersResponse,
    CompanyRetrieveContactResponse,
)
```

Methods:

- <code title="get /v0/company/{company_id}">client.company.<a href="./src/openregister/resources/company.py">retrieve</a>(company_id, \*\*<a href="src/openregister/types/company_retrieve_params.py">params</a>) -> <a href="./src/openregister/types/company_retrieve_response.py">CompanyRetrieveResponse</a></code>
- <code title="get /v0/company/{company_id}/shareholders">client.company.<a href="./src/openregister/resources/company.py">list_shareholders</a>(company_id) -> <a href="./src/openregister/types/company_list_shareholders_response.py">CompanyListShareholdersResponse</a></code>
- <code title="get /v0/company/{company_id}/contact">client.company.<a href="./src/openregister/resources/company.py">retrieve_contact</a>(company_id) -> <a href="./src/openregister/types/company_retrieve_contact_response.py">CompanyRetrieveContactResponse</a></code>

# Document

Types:

```python
from openregister.types import DocumentRetrieveResponse
```

Methods:

- <code title="get /v0/document/{document_id}">client.document.<a href="./src/openregister/resources/document.py">retrieve</a>(document_id) -> <a href="./src/openregister/types/document_retrieve_response.py">DocumentRetrieveResponse</a></code>
- <code title="get /v0/document/{document_id}/download">client.document.<a href="./src/openregister/resources/document.py">download</a>(document_id) -> BinaryAPIResponse</code>

# Jobs

## Document

Types:

```python
from openregister.types.jobs import DocumentCreateResponse, DocumentRetrieveResponse
```

Methods:

- <code title="post /v0/jobs/document">client.jobs.document.<a href="./src/openregister/resources/jobs/document.py">create</a>(\*\*<a href="src/openregister/types/jobs/document_create_params.py">params</a>) -> <a href="./src/openregister/types/jobs/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="get /v0/jobs/document/{id}">client.jobs.document.<a href="./src/openregister/resources/jobs/document.py">retrieve</a>(id) -> <a href="./src/openregister/types/jobs/document_retrieve_response.py">DocumentRetrieveResponse</a></code>
