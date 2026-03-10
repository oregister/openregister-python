# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CompanyDocument"]


class CompanyDocument(BaseModel):
    id: str
    """
    Unique identifier for the document. Example:
    "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    """

    date: str
    """
    Document publication or filing date. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
    """

    latest: bool
    """Whether this is the latest version of the document_type."""

    type: Literal["articles_of_association", "sample_protocol", "shareholder_list"]
    """Categorization of the document:

    - articles_of_association: Company statutes/bylaws
    - sample_protocol: Standard founding protocol
    - shareholder_list: List of company shareholders
    """
