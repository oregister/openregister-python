# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["TransparenzregisterUboNaturalPerson"]


class TransparenzregisterUboNaturalPerson(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    date_of_birth: Optional[date] = None

    first_name: Optional[str] = None

    full_name: Optional[str] = None

    last_name: Optional[str] = None

    nationalities: Optional[List[str]] = None
    """ISO 3166-1 alpha-2 nationality codes where available."""

    title: Optional[str] = None
