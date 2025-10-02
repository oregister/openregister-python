# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["ReportTable"]


class ReportTable(BaseModel):
    rows: List["ReportRow"]


from .report_row import ReportRow
