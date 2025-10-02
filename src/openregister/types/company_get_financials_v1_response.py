# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CompanyGetFinancialsV1Response", "Merged", "Report"]


class Merged(BaseModel):
    aktiva: "MergedReportTable"
    """Report table with data merged across multiple report periods"""

    passiva: "MergedReportTable"
    """Report table with data merged across multiple report periods"""

    guv: Optional["MergedReportTable"] = None
    """Report table with data merged across multiple report periods"""


class Report(BaseModel):
    aktiva: "ReportTable"

    consolidated: bool
    """Whether the report is a consolidated report or not."""

    passiva: "ReportTable"

    report_end_date: str

    report_id: str
    """
    Unique identifier for the financial report. Example:
    f47ac10b-58cc-4372-a567-0e02b2c3d479
    """

    report_start_date: Optional[str] = None

    guv: Optional["ReportTable"] = None


class CompanyGetFinancialsV1Response(BaseModel):
    merged: Optional[Merged] = None
    """All report periods merged into a single view"""

    reports: List[Report]


from .report_table import ReportTable
from .merged_report_table import MergedReportTable
