# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .entity_type import EntityType

__all__ = ["CompanyListShareholdersResponse", "Shareholder"]


class Shareholder(BaseModel):
    country: str
    """
    Country where the shareholder is located, in ISO 3166-1 alpha-2 format. Example:
    "DE" for Germany
    """

    name: str
    """The name of the shareholder. E.g. "Max Mustermann" or "Max Mustermann GmbH" """

    nominal_share: int
    """Nominal value of shares in Euro. Example: 100"""

    percentage_share: float
    """Percentage of company ownership. Example: 5.36 represents 5.36% ownership"""

    type: EntityType
    """The type of shareholder."""

    id: Optional[str] = None
    """
    Unique identifier for the shareholder. For companies: Format matches company_id
    pattern For individuals: UUID Example: "DE-HRB-F1103-267645" or UUID May be null
    for certain shareholders.
    """


class CompanyListShareholdersResponse(BaseModel):
    date: str
    """
    Date when this shareholder information became effective. Format: ISO 8601
    (YYYY-MM-DD) Example: "2022-01-01"
    """

    document_id: str
    """
    Unique identifier for the document this was taken from. Example:
    "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    """

    shareholders: List[Shareholder]
