# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .transparenzregister_report import TransparenzregisterReport
from .transparenzregister_document import TransparenzregisterDocument

__all__ = ["TransparenzregisterExtract"]


class TransparenzregisterExtract(BaseModel):
    """
    Transparenzregister extract resource including processing state, parsed report, and downloadable documents.
    """

    id: str
    """Stable extract identifier. Example: "tre_12345678" """

    status: Literal["completed", "processing", "failed"]
    """Status of the Transparenzregister extract."""

    company_id: Optional[str] = None
    """
    Company identifier associated with this extract request. May be null when using
    sandbox credentials.
    """

    completed_at: Optional[datetime] = None
    """Timestamp when extract processing completed."""

    documents: Optional[List[TransparenzregisterDocument]] = None
    """URLs for downloading available extract documents."""

    ekrn: Optional[str] = None
    """EKRN used to request this extract."""

    reference_number: Optional[str] = None
    """Transparenzregister reference number from the extract."""

    report: Optional[TransparenzregisterReport] = None
    """Parsed Transparenzregister extract report limited to UBO-relevant fields."""

    submitted_at: Optional[datetime] = None
    """Timestamp when extract submission started."""
