# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .company_search_response_item import CompanySearchResponseItem

__all__ = ["SearchAutocompleteCompaniesV1Response"]


class SearchAutocompleteCompaniesV1Response(BaseModel):
    results: List[CompanySearchResponseItem]
    """List of companies matching the search criteria."""
