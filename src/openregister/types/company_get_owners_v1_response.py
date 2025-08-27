# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .entity_type import EntityType
from .company_relation_type import CompanyRelationType

__all__ = ["CompanyGetOwnersV1Response", "Owner", "OwnerLegalPerson", "OwnerNaturalPerson"]


class OwnerLegalPerson(BaseModel):
    city: Optional[str] = None

    country: str
    """
    Country where the owner is located, in ISO 3166-1 alpha-2 format. Example: "DE"
    for Germany
    """

    name: str


class OwnerNaturalPerson(BaseModel):
    city: str

    country: str

    date_of_birth: Optional[str] = None

    first_name: str

    full_name: str

    last_name: str


class Owner(BaseModel):
    id: Optional[str] = None
    """
    Unique identifier for the shareholder. For companies: Format matches company_id
    pattern For individuals: UUID Example: "DE-HRB-F1103-267645" or UUID May be null
    for certain shareholders.
    """

    legal_person: Optional[OwnerLegalPerson] = None
    """Details about the legal person."""

    name: str
    """The name of the shareholder. E.g. "Max Mustermann" or "Max Mustermann GmbH" """

    natural_person: Optional[OwnerNaturalPerson] = None
    """Details about the natural person."""

    nominal_share: float
    """Nominal value of shares in Euro. Example: 100"""

    percentage_share: Optional[float] = None
    """Percentage of company ownership. Example: 5.36 represents 5.36% ownership"""

    relation_type: CompanyRelationType
    """Type of relationship between the entity and the company."""

    start: Optional[str] = None
    """Date when the relation started.

    Only available for some types of owners. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
    """

    type: EntityType
    """The type of shareholder."""


class CompanyGetOwnersV1Response(BaseModel):
    company_id: str
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    owners: List[Owner]
