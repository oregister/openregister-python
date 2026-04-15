# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RequestGetV1Response", "DownloadURL"]


class DownloadURL(BaseModel):
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


class RequestGetV1Response(BaseModel):
    """
    Response containing document request results and download URLs.
    All internal complexity (document IDs, baskets, polling) is handled automatically.
    """

    request_id: str
    """Request ID that was used to submit the request. Example: "req_12345678" """

    status: Literal["completed", "processing", "failed"]
    """Status of the Transparenzregister request."""

    download_urls: Optional[List[DownloadURL]] = None
    """URLs for downloading all available documents."""
