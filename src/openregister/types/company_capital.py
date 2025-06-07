# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CompanyCapital"]


class CompanyCapital(BaseModel):
    amount: float
    """
    Capital amount as a decimal number. Example: 100000.00 represents 100,000.00
    monetary units
    """

    currency: Literal["EUR", "DEM", "USD"]
    """Currency code for the capital amount. Example: "EUR" for Euro"""

    start_date: str
    """
    Date when this capital amount became effective. Format: ISO 8601 (YYYY-MM-DD)
    Example: "2023-01-01"
    """
