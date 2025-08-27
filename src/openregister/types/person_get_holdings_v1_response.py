# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .company_relation_type import CompanyRelationType

__all__ = ["PersonGetHoldingsV1Response", "Holding"]


class Holding(BaseModel):
    company_id: str
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    end: Optional[str] = None
    """
    Date when the ownership ended. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
    """

    name: str
    """Name of the company."""

    nominal_share: float
    """Amount of shares or capital in the company. Example: 100"""

    percentage_share: Optional[float] = None
    """Share of the company. Example: 0.5 represents 50% ownership"""

    relation_type: CompanyRelationType
    """Type of relationship between the entity and the company."""

    start: Optional[str] = None
    """
    Date when the ownership started. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
    """


class PersonGetHoldingsV1Response(BaseModel):
    holdings: List[Holding]
    """Shareholder and limited partner positions of the person."""

    person_id: str
    """Unique person identifier. Example: cc78ab54-d958-49b8-bae7-2f6c0c308837"""
