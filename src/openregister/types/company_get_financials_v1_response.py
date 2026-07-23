# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import date

from .._models import BaseModel

__all__ = ["CompanyGetFinancialsV1Response", "Indicator", "Merged", "Report", "ReportSource"]


class Indicator(BaseModel):
    """
    The indicators of the company for a given year.
    Values of the indicator are given in the smallest currency unit (cents).
    Example: 2099 represents €20.99 for monetary values
    For non-monetary values (e.g., employees), the actual number.
    """

    active_accruals: Optional[int] = None
    """The active accruals of that year (in cents)."""

    affiliated_liabilities: Optional[int] = None
    """The affiliated liabilities of that year (in cents)."""

    balance_sheet_total: Optional[int] = None
    """The balance sheet total of that year (in cents)."""

    bank_debt: Optional[int] = None
    """The bank debt of that year (in cents)."""

    capital_reserves: Optional[int] = None
    """The capital reserves of that year (in cents)."""

    cash: Optional[int] = None
    """The cash of that year (in cents)."""

    commission_expense: Optional[int] = None
    """Commission expense (Provisionsaufwendungen) of that year (in cents)."""

    commission_income: Optional[int] = None
    """Commission income (Provisionserträge) of that year (in cents)."""

    current_assets: Optional[int] = None
    """The current assets of that year (in cents)."""

    date: str
    """
    Date to which this financial indicators apply. Format: ISO 8601 (YYYY-MM-DD)
    Example: "2022-01-01"
    """

    ebit: Optional[int] = None
    """The earnings before interest and taxes of that year (in cents)."""

    ebitda: Optional[int] = None
    """
    The earnings before interest, taxes, depreciation, and amortization of that year
    (in cents).
    """

    employees: Optional[int] = None
    """The number of employees of that year."""

    equity: Optional[int] = None
    """The equity of that year (in cents)."""

    financial_assets: Optional[int] = None
    """The financial assets of that year (in cents)."""

    financial_debt: Optional[int] = None
    """The financial debt of that year (in cents)."""

    financial_depreciation: Optional[int] = None
    """
    The signed financial asset depreciation, write-down, or reversal of that year
    (in cents).
    """

    fixed_assets: Optional[int] = None
    """The fixed assets of that year (in cents)."""

    gross_profit: Optional[int] = None
    """The gross profit (Rohergebnis) of that year (in cents)."""

    income_after_tax: Optional[int] = None
    """The income after income taxes of that year (in cents)."""

    income_before_tax: Optional[int] = None
    """The income before income taxes of that year (in cents)."""

    intangible_assets: Optional[int] = None
    """The intangible assets of that year (in cents)."""

    interest_expense: Optional[int] = None
    """The interest expense of that year (in cents)."""

    interest_income: Optional[int] = None
    """The interest income of that year (in cents)."""

    inventory: Optional[int] = None
    """The inventory of that year (in cents)."""

    liabilities: Optional[int] = None
    """The liabilities of that year (in cents)."""

    materials: Optional[int] = None
    """The materials of that year (in cents)."""

    net_income: Optional[int] = None
    """The net income of that year (in cents)."""

    operating_depreciation: Optional[int] = None
    """The operating depreciation and amortization of that year (in cents)."""

    other_liabilities: Optional[int] = None
    """The other liabilities of that year (in cents)."""

    other_operating_expenses: Optional[int] = None
    """The other operating expenses of that year (in cents)."""

    other_operating_income: Optional[int] = None
    """The other operating income of that year (in cents)."""

    other_provisions: Optional[int] = None
    """The other provisions of that year (in cents)."""

    other_taxes: Optional[int] = None
    """Other taxes (Sonstige Steuern) of that year (in cents)."""

    parent_net_income: Optional[int] = None
    """The parent-attributed net income of that year (in cents)."""

    passive_accruals: Optional[int] = None
    """The passive accruals of that year (in cents)."""

    pension_provisions: Optional[int] = None
    """The pension provisions of that year (in cents)."""

    profit_carryforward: Optional[int] = None
    """The profit carryforward of that year (in cents)."""

    provisions: Optional[int] = None
    """The provisions of that year (in cents)."""

    real_estate: Optional[int] = None
    """The real estate of that year (in cents)."""

    receivables: Optional[int] = None
    """The receivables of that year (in cents)."""

    report_id: str
    """The report id (source) of the indicators."""

    retained_earnings: Optional[int] = None
    """The retained earnings of that year (in cents)."""

    revenue: Optional[int] = None
    """The revenue of that year (in cents)."""

    salaries: Optional[int] = None
    """The salaries of that year (in cents)."""

    shareholder_liabilities: Optional[int] = None
    """The shareholder liabilities of that year (in cents)."""

    tangible_assets: Optional[int] = None
    """The tangible assets of that year (in cents)."""

    taxes: Optional[int] = None
    """The taxes of that year (in cents)."""

    trade_payables: Optional[int] = None
    """The trade payables of that year (in cents)."""

    trade_receivables: Optional[int] = None
    """The trade receivables of that year (in cents)."""


class Merged(BaseModel):
    """Financial data merged across all available report periods"""

    aktiva: "MergedReportTable"
    """Report table with data merged across multiple report periods"""

    passiva: "MergedReportTable"
    """Report table with data merged across multiple report periods"""

    guv: Optional["MergedReportTable"] = None
    """Report table with data merged across multiple report periods"""


class ReportSource(BaseModel):
    html_url: str
    """Url of the rendered HTML report.

    In the form of a presigned url accessible for 30 minutes.
    """


class Report(BaseModel):
    aktiva: "ReportTable"

    consolidated: bool
    """Whether the report is a consolidated report or not."""

    passiva: "ReportTable"

    report_end_date: date

    report_id: str
    """
    Unique identifier for the financial report. Example:
    f47ac10b-58cc-4372-a567-0e02b2c3d479
    """

    report_start_date: Optional[date] = None

    sources: List[ReportSource]
    """Sources of the report data. Presigned URLs accessible for 30 minutes."""

    guv: Optional["ReportTable"] = None


class CompanyGetFinancialsV1Response(BaseModel):
    indicators: List[Indicator]
    """Key financial indicators per fiscal year, sorted by date (latest first)."""

    merged: Optional[Merged] = None
    """Financial data merged across all available report periods"""

    reports: List[Report]


from .report_table import ReportTable
from .merged_report_table import MergedReportTable
