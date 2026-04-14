# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .source import Source
from .._models import BaseModel
from .entity_type import EntityType
from .company_relation_type import CompanyRelationType
from .company_owner_legal_person import CompanyOwnerLegalPerson
from .company_owner_natural_person import CompanyOwnerNaturalPerson

__all__ = ["CompanyGetOwnersV1Response", "Owner"]


class Owner(BaseModel):
    id: Optional[str] = None
    """
    Unique identifier for the shareholder. For companies: Format matches company_id
    pattern For individuals: UUID Example: "DE-HRB-F1103-267645" or UUID May be null
    for certain shareholders.
    """

    legal_person: Optional[CompanyOwnerLegalPerson] = None
    """Details about the legal person."""

    name: str
    """The name of the shareholder. E.g. "Max Mustermann" or "Max Mustermann GmbH" """

    natural_person: Optional[CompanyOwnerNaturalPerson] = None
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
    best_available: bool
    """
    When true, the returned owner data is the best available but may not reflect the
    most current ownership state. This applies to AG and SE companies where
    ownership data is sourced from Handelsregister decision and articles of
    association documents, which are not filed on every ownership change.
    """

    company_id: str
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    owners: List[Owner]

    sources: List[Source]
    """Sources of the company owners data."""
