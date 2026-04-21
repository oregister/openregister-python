# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ExtractCreateV1Response"]


class ExtractCreateV1Response(BaseModel):
    """
    Response from creating a Transparenzregister extract.
    Only fields known at creation time are present.
    Poll `GET /v1/transparenzregister/extracts/{extract_id}` to retrieve report and documents.
    """

    id: str
    """Stable extract identifier.

    Use this to poll the get-extract endpoint. Example: "tre_12345678"
    """

    company_id: Optional[str] = None
    """
    Company identifier associated with this extract request. May be null when using
    sandbox credentials.
    """

    ekrn: Optional[str] = None
    """EKRN used to request this extract."""

    status: Literal["processing"]
    """
    Always `processing` on create. Poll the get-extract endpoint for terminal state.
    """

    submitted_at: datetime
    """Timestamp when extract submission started."""
