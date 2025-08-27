# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CompanyGetContactV0Response"]


class CompanyGetContactV0Response(BaseModel):
    source_url: str
    """Where the contact information was found. Example: "https://openregister.de" """

    email: Optional[str] = None
    """Company contact email address. Example: "founders@openregister.de" """

    phone: Optional[str] = None
    """Company phone number. Example: "+49 030 12345678" """

    vat_id: Optional[str] = None
    """Value Added Tax identification number.

    (Umsatzsteuer-Identifikationsnummer) Example: "DE370146530"
    """
