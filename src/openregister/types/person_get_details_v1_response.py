# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PersonGetDetailsV1Response", "ManagementPosition"]


class ManagementPosition(BaseModel):
    company_name: str
    """Name of the company. Example: "Descartes Technologies GmbH" """

    register_id: str
    """Register ID of the company. Example: DE-HRB-F1103-267645"""

    role: str
    """Role of the person in the company. Example: "DIRECTOR" """

    end_date: Optional[datetime] = None
    """
    Date when the person ended the management position. Format: ISO 8601
    (YYYY-MM-DD) Example: "2023-01-01"
    """

    start_date: Optional[datetime] = None
    """
    Date when the person started the management position. Format: ISO 8601
    (YYYY-MM-DD) Example: "2022-01-01"
    """


class PersonGetDetailsV1Response(BaseModel):
    id: str
    """Unique person identifier. Example: cc78ab54-d958-49b8-bae7-2f6c0c308837"""

    age: Optional[int] = None
    """Age of the person."""

    city: str
    """City of the person."""

    date_of_birth: Optional[datetime] = None
    """
    Date of birth of the person. Format: ISO 8601 (YYYY-MM-DD) Example: "1990-01-01"
    """

    first_name: str
    """First name of the person."""

    last_name: str
    """Last name of the person."""

    management_positions: List[ManagementPosition]
    """Management positions of the person."""
