# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CompanyOwnerNaturalPerson"]


class CompanyOwnerNaturalPerson(BaseModel):
    city: str

    country: str

    date_of_birth: Optional[str] = None

    first_name: str

    full_name: str

    last_name: str
