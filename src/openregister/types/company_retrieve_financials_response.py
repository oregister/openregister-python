# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "CompanyRetrieveFinancialsResponse",
    "Report",
    "ReportAktiva",
    "ReportAktivaRow",
    "ReportPassiva",
    "ReportPassivaRow",
    "ReportGuv",
    "ReportGuvRow",
]


class ReportAktivaRow(BaseModel):
    children: List[object]

    formatted_name: str

    name: str

    current_value: Optional[int] = None

    previous_value: Optional[int] = None


class ReportAktiva(BaseModel):
    rows: List[ReportAktivaRow]


class ReportPassivaRow(BaseModel):
    children: List[object]

    formatted_name: str

    name: str

    current_value: Optional[int] = None

    previous_value: Optional[int] = None


class ReportPassiva(BaseModel):
    rows: List[ReportPassivaRow]


class ReportGuvRow(BaseModel):
    children: List[object]

    formatted_name: str

    name: str

    current_value: Optional[int] = None

    previous_value: Optional[int] = None


class ReportGuv(BaseModel):
    rows: List[ReportGuvRow]


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
