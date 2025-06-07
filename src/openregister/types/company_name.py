# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .company_legal_form import CompanyLegalForm

__all__ = ["CompanyName"]


class CompanyName(BaseModel):
    legal_form: CompanyLegalForm
    """
    Legal form of the company at this point in time. Example: "gmbh" for
    Gesellschaft mit beschränkter Haftung
    """

    name: str
    """
    Official company name including any legal form designations. Example: "Descartes
    Technologies UG (haftungsbeschränkt)"
    """

    start_date: str
    """
    Date when this name became effective. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
    """
