# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .company_legal_form import CompanyLegalForm
from .company_register_type import CompanyRegisterType

__all__ = ["CompanySearch", "Pagination", "Result"]


class Pagination(BaseModel):
    page: int
    """Current page number."""

    per_page: int
    """Number of results per page."""

    total_pages: int
    """Total number of pages."""

    total_results: int
    """Total number of results."""


class Result(BaseModel):
    active: bool
    """Company status - true if active, false if inactive."""

    company_id: str
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    country: Optional[str] = None
    """
    Country where the company is registered using ISO 3166-1 alpha-2 code. Example:
    "DE" for Germany
    """

    legal_form: CompanyLegalForm
    """
    Legal form of the company. Example: "gmbh" for Gesellschaft mit beschränkter
    Haftung
    """

    name: str
    """Official registered company name. Example: "Max Mustermann GmbH" """

    register_court: str
    """Court where the company is registered. Example: "Berlin (Charlottenburg)" """

    register_number: str
    """Registration number in the company register. Example: "230633" """

    register_type: CompanyRegisterType
    """Type of company register. Example: "HRB" for Commercial Register B"""


class CompanySearch(BaseModel):
    pagination: Pagination

    results: List[Result]
    """List of companies matching the search criteria."""
