# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CompanyAddress"]


class CompanyAddress(BaseModel):
    city: str
    """City or locality name. Example: "Berlin" """

    country: str
    """Country name. Example: "Germany" """

    formatted_value: str
    """
    Complete address formatted as a single string. Example: "Musterstraße 1, 10117
    Berlin, Germany"
    """

    start_date: str
    """
    Date when this address became effective. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
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
