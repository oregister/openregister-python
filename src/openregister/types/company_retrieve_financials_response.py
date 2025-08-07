# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CompanyRetrieveFinancialsResponse", "Report", "ReportAktiva", "ReportPassiva", "ReportGuv"]


class ReportAktiva(BaseModel):
    rows: List["ReportRow"]


class ReportPassiva(BaseModel):
    rows: List["ReportRow"]


class ReportGuv(BaseModel):
    rows: List["ReportRow"]


class Report(BaseModel):
    aktiva: ReportAktiva

    consolidated: bool

    passiva: ReportPassiva

    report_end_date: datetime

    report_id: str

    guv: Optional[ReportGuv] = None

    report_start_date: Optional[datetime] = None


class CompanyRetrieveFinancialsResponse(BaseModel):
    reports: List[Report]


from .report_row import ReportRow
