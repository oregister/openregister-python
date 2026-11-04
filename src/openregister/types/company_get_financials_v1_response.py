# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "CompanyGetFinancialsV1Response",
    "Estimates",
    "EstimatesEbitda",
    "EstimatesEmployees",
    "EstimatesRevenue",
    "Indicator",
    "Merged",
    "Report",
    "ReportAuditor",
    "ReportSource",
    "ReportActivityStatement",
]


class EstimatesEbitda(BaseModel):
    """A modelled value for one fiscal year.

    min and max are not hard
    limits: the true value lies between them with 80% probability.
    """

    confidence: Literal["high", "medium", "low"]
    """
    How narrow the 80% range is, the same tiers the search filters
    estimated\\__\\**\\__confidence use. Revenue and employees are judged by the ratio of
    max to min, EBITDA by the range relative to the latest reported balance sheet
    total (low when there is none).
    """

    date: datetime.date
    """
    End of the fiscal year the estimate applies to, matching the company's reporting
    year end. Format: ISO 8601 (YYYY-MM-DD) Example: "2024-12-31"
    """

    max: int
    """Upper end of the 80% range."""

    min: int
    """Lower end of the 80% range."""

    value: int
    """The estimated figure, the middle of the modelled range."""


class EstimatesEmployees(BaseModel):
    """A modelled value for one fiscal year.

    min and max are not hard
    limits: the true value lies between them with 80% probability.
    """

    confidence: Literal["high", "medium", "low"]
    """
    How narrow the 80% range is, the same tiers the search filters
    estimated\\__\\**\\__confidence use. Revenue and employees are judged by the ratio of
    max to min, EBITDA by the range relative to the latest reported balance sheet
    total (low when there is none).
    """

    date: datetime.date
    """
    End of the fiscal year the estimate applies to, matching the company's reporting
    year end. Format: ISO 8601 (YYYY-MM-DD) Example: "2024-12-31"
    """

    max: int
    """Upper end of the 80% range."""

    min: int
    """Lower end of the 80% range."""

    value: int
    """The estimated figure, the middle of the modelled range."""


class EstimatesRevenue(BaseModel):
    """A modelled value for one fiscal year.

    min and max are not hard
    limits: the true value lies between them with 80% probability.
    """

    confidence: Literal["high", "medium", "low"]
    """
    How narrow the 80% range is, the same tiers the search filters
    estimated\\__\\**\\__confidence use. Revenue and employees are judged by the ratio of
    max to min, EBITDA by the range relative to the latest reported balance sheet
    total (low when there is none).
    """

    date: datetime.date
    """
    End of the fiscal year the estimate applies to, matching the company's reporting
    year end. Format: ISO 8601 (YYYY-MM-DD) Example: "2024-12-31"
    """

    max: int
    """Upper end of the 80% range."""

    min: int
    """Lower end of the 80% range."""

    value: int
    """The estimated figure, the middle of the modelled range."""


class Estimates(BaseModel):
    """Modelled revenue, EBITDA and employees for companies that do not
    report them.

    One estimate per metric, for the latest fiscal year.
    """

    ebitda: Optional[EstimatesEbitda] = None
    """A modelled value for one fiscal year.

    min and max are not hard limits: the true value lies between them with 80%
    probability.
    """

    employees: Optional[EstimatesEmployees] = None
    """A modelled value for one fiscal year.

    min and max are not hard limits: the true value lies between them with 80%
    probability.
    """

    revenue: Optional[EstimatesRevenue] = None
    """A modelled value for one fiscal year.

    min and max are not hard limits: the true value lies between them with 80%
    probability.
    """


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

    apprentices: Optional[int] = None
    """
    The number of apprentices (Auszubildende) of that year, where the report states
    it.
    """

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

    date: datetime.date
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

    securities: Optional[int] = None
    """The securities of that year (in cents)."""

    shareholder_liabilities: Optional[int] = None
    """The shareholder liabilities of that year (in cents)."""

    short_year: bool
    """A short fiscal year (Rumpfgeschäftsjahr), shorter than twelve months"""

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


class ReportAuditor(BaseModel):
    """The auditor who signed the audit opinion.

    Null for unaudited
    reports and reports whose auditor could not be read.
    """

    name: str
    """
    Name of the audit firm or sole auditor as the report prints it. Example: "KPMG
    AG Wirtschaftsprüfungsgesellschaft"
    """

    signatories: List[str]
    """Names of the auditors who signed the opinion."""

    city: Optional[str] = None
    """City the audit opinion was signed in. Example: "München" """

    company_id: Optional[str] = None
    """
    Unique company identifier of the audit firm, if it matches exactly one
    registered company. Example: DE-HRB-F1103-267645
    """


class ReportSource(BaseModel):
    html_url: str
    """Url of the rendered HTML report.

    In the form of a presigned url accessible for 30 minutes.
    """


class ReportActivityStatement(BaseModel):
    activity: Literal[
        "electricity_transmission",
        "electricity_distribution",
        "gas_transmission",
        "gas_distribution",
        "gas_storage",
        "lng_facility",
        "meter_operation",
        "other",
    ]
    """The unbundled activity.

    `meter_operation` is the metering business § 3 Abs. 4 MsbG separates; `other` is
    any further activity the company reports separately, named in `label`.
    """

    aktiva: "ReportTable"

    label: str
    """The activity's name as the report prints it. Example: "Stromnetz" """

    passiva: "ReportTable"

    guv: Optional["ReportTable"] = None


class Report(BaseModel):
    aktiva: "ReportTable"

    auditor: Optional[ReportAuditor] = None
    """The auditor who signed the audit opinion.

    Null for unaudited reports and reports whose auditor could not be read.
    """

    consolidated: bool
    """Whether the report is a consolidated report or not."""

    passiva: "ReportTable"

    published_at: datetime.date
    """
    Date the report was published. A complement or correction is a separate report
    with the same period and a later date. Format: ISO 8601 (YYYY-MM-DD)
    """

    report_end_date: datetime.date
    """Format: ISO 8601 (YYYY-MM-DD)"""

    report_id: str
    """
    Unique identifier for the financial report. Example:
    f47ac10b-58cc-4372-a567-0e02b2c3d479
    """

    report_start_date: Optional[datetime.date] = None
    """Format: ISO 8601 (YYYY-MM-DD)"""

    sources: List[ReportSource]
    """Sources of the report data. Presigned URLs accessible for 30 minutes."""

    activity_statements: Optional[List[ReportActivityStatement]] = None
    """
    Activity statements (Tätigkeitsabschlüsse) of an energy network operator: a
    separate balance sheet and income statement for each activity § 6b Abs. 3 EnWG
    unbundles, such as electricity distribution. Empty for reports that publish
    none.
    """

    guv: Optional["ReportTable"] = None


class CompanyGetFinancialsV1Response(BaseModel):
    estimates: Estimates
    """Modelled revenue, EBITDA and employees for companies that do not report them.

    One estimate per metric, for the latest fiscal year.
    """

    indicators: List[Indicator]
    """Key financial indicators per fiscal year, sorted by date (latest first)."""

    merged: Optional[Merged] = None
    """Financial data merged across all available report periods"""

    reports: List[Report]


from .report_table import ReportTable
from .merged_report_table import MergedReportTable
