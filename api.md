# Search

Types:

```python
from openregister.types import (
    CompanyLegalForm,
    CompanyRegisterType,
    CompanySearch,
    SearchAutocompleteCompaniesV1Response,
    SearchFindPersonResponse,
    SearchLookupCompanyByURLResponse,
)
```

Methods:

- <code title="get /v1/autocomplete/company">client.search.<a href="./src/openregister/resources/search.py">autocomplete_companies_v1</a>(\*\*<a href="src/openregister/types/search_autocomplete_companies_v1_params.py">params</a>) -> <a href="./src/openregister/types/search_autocomplete_companies_v1_response.py">SearchAutocompleteCompaniesV1Response</a></code>
- <code title="get /v0/search/company">client.search.<a href="./src/openregister/resources/search.py">find_companies_v0</a>(\*\*<a href="src/openregister/types/search_find_companies_v0_params.py">params</a>) -> <a href="./src/openregister/types/company_search.py">CompanySearch</a></code>
- <code title="post /v1/search/company">client.search.<a href="./src/openregister/resources/search.py">find_companies_v1</a>(\*\*<a href="src/openregister/types/search_find_companies_v1_params.py">params</a>) -> <a href="./src/openregister/types/company_search.py">CompanySearch</a></code>
- <code title="post /v1/search/person">client.search.<a href="./src/openregister/resources/search.py">find_person</a>(\*\*<a href="src/openregister/types/search_find_person_params.py">params</a>) -> <a href="./src/openregister/types/search_find_person_response.py">SearchFindPersonResponse</a></code>
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
    CompanyRelationType,
    EntityType,
    CompanyRetrieveResponse,
    CompanyGetHoldingsV1Response,
    CompanyGetOwnersV1Response,
    CompanyListShareholdersResponse,
    CompanyRetrieveContactResponse,
    CompanyRetrieveFinancialsResponse,
)
```

Methods:

- <code title="get /v0/company/{company_id}">client.company.<a href="./src/openregister/resources/company.py">retrieve</a>(company_id, \*\*<a href="src/openregister/types/company_retrieve_params.py">params</a>) -> <a href="./src/openregister/types/company_retrieve_response.py">CompanyRetrieveResponse</a></code>
- <code title="get /v1/company/{company_id}/holdings">client.company.<a href="./src/openregister/resources/company.py">get_holdings_v1</a>(company_id) -> <a href="./src/openregister/types/company_get_holdings_v1_response.py">CompanyGetHoldingsV1Response</a></code>
- <code title="get /v1/company/{company_id}/owners">client.company.<a href="./src/openregister/resources/company.py">get_owners_v1</a>(company_id) -> <a href="./src/openregister/types/company_get_owners_v1_response.py">CompanyGetOwnersV1Response</a></code>
- <code title="get /v0/company/{company_id}/shareholders">client.company.<a href="./src/openregister/resources/company.py">list_shareholders</a>(company_id) -> <a href="./src/openregister/types/company_list_shareholders_response.py">CompanyListShareholdersResponse</a></code>
- <code title="get /v0/company/{company_id}/contact">client.company.<a href="./src/openregister/resources/company.py">retrieve_contact</a>(company_id) -> <a href="./src/openregister/types/company_retrieve_contact_response.py">CompanyRetrieveContactResponse</a></code>
- <code title="get /v1/company/{company_id}/financials">client.company.<a href="./src/openregister/resources/company.py">retrieve_financials</a>(company_id) -> <a href="./src/openregister/types/company_retrieve_financials_response.py">CompanyRetrieveFinancialsResponse</a></code>

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
