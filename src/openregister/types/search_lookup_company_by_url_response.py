# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SearchLookupCompanyByURLResponse"]


class SearchLookupCompanyByURLResponse(BaseModel):
    company_id: str
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    email: Optional[str] = None
    """Email address of the company. Example: "info@maxmustermann.de" """

    phone: Optional[str] = None
    """Phone number of the company. Example: "+49 123 456 789" """

    vat_id: Optional[str] = None
    """Value Added Tax identification number. Example: "DE123456789" """
