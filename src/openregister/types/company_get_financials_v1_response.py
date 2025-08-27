# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CompanyGetFinancialsV1Response", "Report", "ReportAktiva", "ReportPassiva", "ReportGuv"]


class ReportAktiva(BaseModel):
    rows: List["ReportRow"]


class ReportPassiva(BaseModel):
    rows: List["ReportRow"]


class ReportGuv(BaseModel):
    rows: List["ReportRow"]


class Report(BaseModel):
    aktiva: ReportAktiva

    consolidated: bool
    """Whether the report is a consolidated report or not."""

    passiva: ReportPassiva

    report_end_date: datetime

    report_id: str
    """
    Unique identifier for the financial report. Example:
    f47ac10b-58cc-4372-a567-0e02b2c3d479
    """

    report_start_date: Optional[datetime] = None

    guv: Optional[ReportGuv] = None


class CompanyGetFinancialsV1Response(BaseModel):
    reports: List[Report]


from .report_row import ReportRow
