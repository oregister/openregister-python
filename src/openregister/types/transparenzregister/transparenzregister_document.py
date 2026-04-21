# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["TransparenzregisterDocument"]


class TransparenzregisterDocument(BaseModel):
    """Download URL for a document with format information."""

    document_id: str
    """Stable UUID for this document."""

    filename: str
    """
    Suggested filename for the download. Example: "registerauszug_company_12345.pdf"
    """

    format: str
    """Format of the downloadable document. Example: "xml", "pdf", "json" """

    url: str
    """
    Download URL for the document. Example:
    "https://api.example.com/download/abc123"
    """
