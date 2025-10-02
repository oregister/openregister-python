# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = [
    "CompanyGetFinancialsV1Response",
    "Merged",
    "MergedAktiva",
    "MergedAktivaRow",
    "MergedPassiva",
    "MergedPassivaRow",
    "MergedGuv",
    "MergedGuvRow",
    "Report",
    "ReportAktiva",
    "ReportPassiva",
    "ReportGuv",
]


class MergedAktivaRow(BaseModel):
    children: List[object]

    formatted_name: str

    name: str

    values: Dict[str, int]
    """Report end date to value mapping (ISO date string as key)"""


class MergedAktiva(BaseModel):
    rows: List[MergedAktivaRow]


class MergedPassivaRow(BaseModel):
    children: List[object]

    formatted_name: str

    name: str

    values: Dict[str, int]
    """Report end date to value mapping (ISO date string as key)"""


class MergedPassiva(BaseModel):
    rows: List[MergedPassivaRow]


class MergedGuvRow(BaseModel):
    children: List[object]

    formatted_name: str

    name: str

    values: Dict[str, int]
    """Report end date to value mapping (ISO date string as key)"""


class MergedGuv(BaseModel):
    rows: List[MergedGuvRow]


class Merged(BaseModel):
    aktiva: MergedAktiva
    """Report table with data merged across multiple report periods"""

    passiva: MergedPassiva
    """Report table with data merged across multiple report periods"""

    guv: Optional[MergedGuv] = None
    """Report table with data merged across multiple report periods"""


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

    report_end_date: str

    report_id: str
    """
    Unique identifier for the financial report. Example:
    f47ac10b-58cc-4372-a567-0e02b2c3d479
    """

    report_start_date: Optional[str] = None

    guv: Optional[ReportGuv] = None


class CompanyGetFinancialsV1Response(BaseModel):
    merged: Optional[Merged] = None
    """All report periods merged into a single view"""

    reports: List[Report]


from .report_row import ReportRow
