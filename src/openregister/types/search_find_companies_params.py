# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .company_legal_form import CompanyLegalForm
from .company_register_type import CompanyRegisterType

__all__ = ["SearchFindCompaniesParams"]


class SearchFindCompaniesParams(TypedDict, total=False):
    active: bool
    """
    Filter for active or inactive companies. Set to true for active companies only,
    false for inactive only.
    """

    legal_form: CompanyLegalForm
    """
    Legal form of the company. Example: "gmbh" for "Gesellschaft mit beschränkter
    Haftung"
    """

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
