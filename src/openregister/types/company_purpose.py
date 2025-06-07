# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CompanyPurpose"]


class CompanyPurpose(BaseModel):
    purpose: str
    """
    Official description of the company's business activities and objectives. This
    is the registered purpose as stated in official documents.
    """

    start_date: str
    """
    Date when this purpose became effective. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
    """
