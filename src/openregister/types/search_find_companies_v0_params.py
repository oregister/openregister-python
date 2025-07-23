# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .company_legal_form import CompanyLegalForm
from .company_register_type import CompanyRegisterType

__all__ = ["SearchFindCompaniesV0Params"]


class SearchFindCompaniesV0Params(TypedDict, total=False):
    active: bool
    """
    Filter for active or inactive companies. Set to true for active companies only,
    false for inactive only.
    """

    incorporation_date: str
    """
    Date of incorporation of the company. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
    """

    legal_form: CompanyLegalForm
    """
    Legal form of the company. Example: "gmbh" for "Gesellschaft mit beschränkter
    Haftung"
    """

    page: int
    """Page number for pagination."""

    per_page: int
    """Number of results per page (max 50)."""

    query: str
    """
    Text search query to find companies by name. Example: "Descartes Technologies
    UG"
    """

    register_court: str
    """Court where the company is registered. Example: "Berlin (Charlottenburg)" """

    register_number: str
    """Company register number for exact matching. Example: "230633" """

    register_type: CompanyRegisterType
    """Type of register to filter results. Example: "HRB" (Commercial Register B)"""
