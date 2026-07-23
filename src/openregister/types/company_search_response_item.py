# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .company_legal_form import CompanyLegalForm
from .company_register_type import CompanyRegisterType

__all__ = ["CompanySearchResponseItem", "Address"]


class Address(BaseModel):
    """Current registered address of the company, taken from the search index."""

    city: str
    """City or locality name. Example: "Berlin" """

    country: str
    """Country of the address using ISO 3166-1 alpha-2 code. Example: "DE" for Germany"""

    formatted_value: str
    """
    Complete address formatted as a single string. Example: "Musterstraße 1, 10117
    Berlin"
    """

    extra: Optional[str] = None
    """
    Additional address information such as c/o or attention line. Example: "c/o Max
    Mustermann"
    """

    postal_code: Optional[str] = None
    """Postal or ZIP code. Example: "10117" """

    street: Optional[str] = None
    """Street name and number. Example: "Musterstraße 1" """


class CompanySearchResponseItem(BaseModel):
    active: bool
    """Company status - true if active, false if inactive."""

    address: Optional[Address] = None
    """Current registered address of the company, taken from the search index."""

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

    purpose: Optional[str] = None
    """Current official business purpose of the company, taken from the search index."""

    register_court: str
    """Court where the company is registered. Example: "Berlin (Charlottenburg)" """

    register_number: str
    """Registration number in the company register. Example: "230633" """

    register_type: CompanyRegisterType
    """Type of company register. Example: "HRB" for Commercial Register B"""
