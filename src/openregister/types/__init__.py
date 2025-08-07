# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import report_row, company_retrieve_financials_response
from .. import _compat
from .report_row import ReportRow as ReportRow
from .entity_type import EntityType as EntityType
from .company_name import CompanyName as CompanyName
from .company_search import CompanySearch as CompanySearch
from .company_address import CompanyAddress as CompanyAddress
from .company_capital import CompanyCapital as CompanyCapital
from .company_purpose import CompanyPurpose as CompanyPurpose
from .company_register import CompanyRegister as CompanyRegister
from .company_legal_form import CompanyLegalForm as CompanyLegalForm
from .company_register_type import CompanyRegisterType as CompanyRegisterType
from .company_relation_type import CompanyRelationType as CompanyRelationType
from .company_retrieve_params import CompanyRetrieveParams as CompanyRetrieveParams
from .company_retrieve_response import CompanyRetrieveResponse as CompanyRetrieveResponse
from .search_find_person_params import SearchFindPersonParams as SearchFindPersonParams
from .document_retrieve_response import DocumentRetrieveResponse as DocumentRetrieveResponse
from .search_find_person_response import SearchFindPersonResponse as SearchFindPersonResponse
from .company_get_owners_v1_response import CompanyGetOwnersV1Response as CompanyGetOwnersV1Response
from .search_find_companies_v0_params import SearchFindCompaniesV0Params as SearchFindCompaniesV0Params
from .search_find_companies_v1_params import SearchFindCompaniesV1Params as SearchFindCompaniesV1Params
from .company_get_holdings_v1_response import CompanyGetHoldingsV1Response as CompanyGetHoldingsV1Response
from .company_retrieve_contact_response import CompanyRetrieveContactResponse as CompanyRetrieveContactResponse
from .company_list_shareholders_response import CompanyListShareholdersResponse as CompanyListShareholdersResponse
from .search_lookup_company_by_url_params import SearchLookupCompanyByURLParams as SearchLookupCompanyByURLParams
from .company_retrieve_financials_response import CompanyRetrieveFinancialsResponse as CompanyRetrieveFinancialsResponse
from .search_lookup_company_by_url_response import SearchLookupCompanyByURLResponse as SearchLookupCompanyByURLResponse
from .search_autocomplete_companies_v1_params import (
    SearchAutocompleteCompaniesV1Params as SearchAutocompleteCompaniesV1Params,
)
from .search_autocomplete_companies_v1_response import (
    SearchAutocompleteCompaniesV1Response as SearchAutocompleteCompaniesV1Response,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V2:
    report_row.ReportRow.model_rebuild(_parent_namespace_depth=0)
    company_retrieve_financials_response.CompanyRetrieveFinancialsResponse.model_rebuild(_parent_namespace_depth=0)
else:
    report_row.ReportRow.update_forward_refs()  # type: ignore
    company_retrieve_financials_response.CompanyRetrieveFinancialsResponse.update_forward_refs()  # type: ignore
