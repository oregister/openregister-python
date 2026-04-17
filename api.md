# Search

Types:

```python
from openregister.types import (
    CompanyLegalForm,
    CompanyRegisterType,
    CompanySearch,
    CompanySearchResponseItem,
    Pagination,
    SearchFilterBase,
    SearchRequestPagination,
    SearchAutocompleteCompaniesV1Response,
    SearchFindPersonV1Response,
    SearchLookupCompanyByURLResponse,
)
```

Methods:

- <code title="get /v1/autocomplete/company">client.search.<a href="./src/openregister/resources/search.py">autocomplete_companies_v1</a>(\*\*<a href="src/openregister/types/search_autocomplete_companies_v1_params.py">params</a>) -> <a href="./src/openregister/types/search_autocomplete_companies_v1_response.py">SearchAutocompleteCompaniesV1Response</a></code>
- <code title="post /v1/search/company">client.search.<a href="./src/openregister/resources/search.py">find_companies_v1</a>(\*\*<a href="src/openregister/types/search_find_companies_v1_params.py">params</a>) -> <a href="./src/openregister/types/company_search.py">CompanySearch</a></code>
- <code title="post /v1/search/person">client.search.<a href="./src/openregister/resources/search.py">find_person_v1</a>(\*\*<a href="src/openregister/types/search_find_person_v1_params.py">params</a>) -> <a href="./src/openregister/types/search_find_person_v1_response.py">SearchFindPersonV1Response</a></code>
- <code title="get /v0/search/lookup">client.search.<a href="./src/openregister/resources/search.py">lookup_company_by_url</a>(\*\*<a href="src/openregister/types/search_lookup_company_by_url_params.py">params</a>) -> <a href="./src/openregister/types/search_lookup_company_by_url_response.py">SearchLookupCompanyByURLResponse</a></code>

# Company

Types:

```python
from openregister.types import (
    CompanyAddress,
    CompanyCapital,
    CompanyDocument,
    CompanyName,
    CompanyOwnerLegalPerson,
    CompanyOwnerNaturalPerson,
    CompanyPurpose,
    CompanyRegister,
    CompanyRelationType,
    EntityType,
    MergedReportRow,
    MergedReportTable,
    ReportRow,
    ReportTable,
    RepresentationRole,
    Source,
    CompanyGetContactV0Response,
    CompanyGetDetailsV1Response,
    CompanyGetFinancialsV1Response,
    CompanyGetHistoricalOwnersV1Response,
    CompanyGetHoldingsV1Response,
    CompanyGetOwnersV1Response,
    CompanyGetUbosV1Response,
)
```

Methods:

- <code title="get /v0/company/{company_id}/contact">client.company.<a href="./src/openregister/resources/company.py">get_contact_v0</a>(company_id) -> <a href="./src/openregister/types/company_get_contact_v0_response.py">CompanyGetContactV0Response</a></code>
- <code title="get /v1/company/{company_id}">client.company.<a href="./src/openregister/resources/company.py">get_details_v1</a>(company_id, \*\*<a href="src/openregister/types/company_get_details_v1_params.py">params</a>) -> <a href="./src/openregister/types/company_get_details_v1_response.py">CompanyGetDetailsV1Response</a></code>
- <code title="get /v1/company/{company_id}/financials">client.company.<a href="./src/openregister/resources/company.py">get_financials_v1</a>(company_id) -> <a href="./src/openregister/types/company_get_financials_v1_response.py">CompanyGetFinancialsV1Response</a></code>
- <code title="get /v1/company/{company_id}/owners/historical">client.company.<a href="./src/openregister/resources/company.py">get_historical_owners_v1</a>(company_id) -> <a href="./src/openregister/types/company_get_historical_owners_v1_response.py">CompanyGetHistoricalOwnersV1Response</a></code>
- <code title="get /v1/company/{company_id}/holdings">client.company.<a href="./src/openregister/resources/company.py">get_holdings_v1</a>(company_id) -> <a href="./src/openregister/types/company_get_holdings_v1_response.py">CompanyGetHoldingsV1Response</a></code>
- <code title="get /v1/company/{company_id}/owners">client.company.<a href="./src/openregister/resources/company.py">get_owners_v1</a>(company_id, \*\*<a href="src/openregister/types/company_get_owners_v1_params.py">params</a>) -> <a href="./src/openregister/types/company_get_owners_v1_response.py">CompanyGetOwnersV1Response</a></code>
- <code title="get /v1/company/{company_id}/ubo">client.company.<a href="./src/openregister/resources/company.py">get_ubos_v1</a>(company_id) -> <a href="./src/openregister/types/company_get_ubos_v1_response.py">CompanyGetUbosV1Response</a></code>

# Document

Types:

```python
from openregister.types import Document, DocumentGetRealtimeV1Response
```

Methods:

- <code title="get /v1/document/{document_id}">client.document.<a href="./src/openregister/resources/document.py">get_cached_v1</a>(document_id) -> <a href="./src/openregister/types/document.py">Document</a></code>
- <code title="get /v1/document">client.document.<a href="./src/openregister/resources/document.py">get_realtime_v1</a>(\*\*<a href="src/openregister/types/document_get_realtime_v1_params.py">params</a>) -> <a href="./src/openregister/types/document_get_realtime_v1_response.py">DocumentGetRealtimeV1Response</a></code>

# Person

Types:

```python
from openregister.types import PersonGetDetailsV1Response, PersonGetHoldingsV1Response
```

Methods:

- <code title="get /v1/person/{person_id}">client.person.<a href="./src/openregister/resources/person.py">get_details_v1</a>(person_id) -> <a href="./src/openregister/types/person_get_details_v1_response.py">PersonGetDetailsV1Response</a></code>
- <code title="get /v1/person/{person_id}/holdings">client.person.<a href="./src/openregister/resources/person.py">get_holdings_v1</a>(person_id) -> <a href="./src/openregister/types/person_get_holdings_v1_response.py">PersonGetHoldingsV1Response</a></code>

# Monitor

Types:

```python
from openregister.types import MonitorCreateResponse, MonitorListResponse
```

Methods:

- <code title="post /v1/monitor">client.monitor.<a href="./src/openregister/resources/monitor.py">create</a>(\*\*<a href="src/openregister/types/monitor_create_params.py">params</a>) -> <a href="./src/openregister/types/monitor_create_response.py">MonitorCreateResponse</a></code>
- <code title="get /v1/monitor">client.monitor.<a href="./src/openregister/resources/monitor.py">list</a>() -> <a href="./src/openregister/types/monitor_list_response.py">MonitorListResponse</a></code>
- <code title="delete /v1/monitor/{entity_id}">client.monitor.<a href="./src/openregister/resources/monitor.py">delete</a>(entity_id) -> None</code>

# Transparenzregister

Methods:

- <code title="post /v1/transparenzregister/credentials">client.transparenzregister.<a href="./src/openregister/resources/transparenzregister/transparenzregister.py">set_credentials_v1</a>(\*\*<a href="src/openregister/types/transparenzregister_set_credentials_v1_params.py">params</a>) -> None</code>

## Extract

Types:

```python
from openregister.types.transparenzregister import ExtractCreateV1Response, ExtractGetV1Response
```

Methods:

- <code title="post /v1/transparenzregister/extracts">client.transparenzregister.extract.<a href="./src/openregister/resources/transparenzregister/extract.py">create_v1</a>(\*\*<a href="src/openregister/types/transparenzregister/extract_create_v1_params.py">params</a>) -> <a href="./src/openregister/types/transparenzregister/extract_create_v1_response.py">ExtractCreateV1Response</a></code>
- <code title="get /v1/transparenzregister/extracts/{extract_id}">client.transparenzregister.extract.<a href="./src/openregister/resources/transparenzregister/extract.py">get_v1</a>(extract_id) -> <a href="./src/openregister/types/transparenzregister/extract_get_v1_response.py">ExtractGetV1Response</a></code>
