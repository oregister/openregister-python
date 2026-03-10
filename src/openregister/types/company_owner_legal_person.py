# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CompanyOwnerLegalPerson"]


class CompanyOwnerLegalPerson(BaseModel):
    city: Optional[str] = None

    country: str
    """
    Country where the owner is located, in ISO 3166-1 alpha-2 format. Example: "DE"
    for Germany
    """

    name: str
