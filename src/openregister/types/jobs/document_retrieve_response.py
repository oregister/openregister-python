# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DocumentRetrieveResponse"]


class DocumentRetrieveResponse(BaseModel):
    status: Literal["pending", "completed", "failed"]

    date: Optional[str] = None
    """
    Date when the job was created. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
    """

    url: Optional[str] = None
