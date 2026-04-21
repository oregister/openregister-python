# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["TransparenzregisterStatusFlags"]


class TransparenzregisterStatusFlags(BaseModel):
    corrected_by_reference: Optional[str] = None

    corrected_references: Optional[List[str]] = None

    deleted: Optional[bool] = None

    deletion_date: Optional[date] = None

    discrepancy_note: Optional[str] = None
