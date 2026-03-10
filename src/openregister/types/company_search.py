# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .pagination import Pagination
from .company_search_response_item import CompanySearchResponseItem

__all__ = ["CompanySearch"]


class CompanySearch(BaseModel):
    pagination: Pagination

    results: List[CompanySearchResponseItem]
    """List of companies matching the search criteria."""
