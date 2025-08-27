# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ReportRow"]


class ReportRow(BaseModel):
    children: List["ReportRow"]

    current_value: Optional[int] = None

    formatted_name: str

    name: str

    previous_value: Optional[int] = None
