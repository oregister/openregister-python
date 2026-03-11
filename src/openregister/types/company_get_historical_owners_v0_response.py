# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CompanyGetHistoricalOwnersV0Response", "Owner", "OwnerOwnershipHistory"]


class OwnerOwnershipHistory(BaseModel):
    document_date: datetime
    """Date of the document"""

    document_id: str
    """Document where this ownership data was found"""

    nominal_shares: int
    """Nominal value of shares in this document"""

    percentage_shares: float
    """Percentage ownership in this document"""


class Owner(BaseModel):
    id: str
    """Unique identifier for the owner.

    For companies, this is the company register ID (e.g. DE-HRB-F1103-267645) which
    can be used to look up the company. For natural persons, this is the entity
    UUID. For other entity types (foreign companies, foundations, etc.), this is
    empty.
    """

    entity_type: Literal[
        "natural_person",
        "german_company",
        "foreign_company",
        "german_government_entity",
        "german_foundation",
        "german_multiple_shareholder",
    ]
    """Type of the owner entity"""

    first_appearance: datetime
    """Date when this owner first appeared"""

    name: str
    """Name of the owner"""

    ownership_history: List[OwnerOwnershipHistory]
    """Historical ownership data across all documents"""

    status: Literal["active", "removed"]
    """Current status of the owner"""

    country: Optional[str] = None
    """Country of the owner"""

    last_appearance: Optional[datetime] = None
    """Date when this owner last appeared (null if still active)"""


class CompanyGetHistoricalOwnersV0Response(BaseModel):
    owners: List[Owner]
