# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .company_relation_type import CompanyRelationType

__all__ = ["CompanyGetHoldingsV1Response", "Holding"]


class Holding(BaseModel):
    company_id: str
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    name: str
    """Name of the company."""

    nominal_share: float
    """Amount of shares or capital in the company. Example: 100"""

    relation_type: CompanyRelationType
    """Type of relationship between the entity and the company."""

    end: Optional[str] = None
    """
    Date when the ownership ended. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
    """

    percentage_share: Optional[float] = None
    """Share of the company. Example: 0.5 represents 50% ownership"""

    start: Optional[str] = None
    """
    Date when the ownership started. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
    """


class CompanyGetHoldingsV1Response(BaseModel):
    company_id: str
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    holdings: List[Holding]
