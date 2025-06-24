# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .entity_type import EntityType
from .company_name import CompanyName
from .company_address import CompanyAddress
from .company_capital import CompanyCapital
from .company_purpose import CompanyPurpose
from .company_register import CompanyRegister
from .company_legal_form import CompanyLegalForm

__all__ = [
    "CompanyRetrieveResponse",
    "Representation",
    "Document",
    "Financials",
    "FinancialsIndicator",
    "FinancialsReport",
]


class Representation(BaseModel):
    city: str
    """City where the representative is located. Example: "Berlin" """

    country: str
    """
    Country where the representative is located, in ISO 3166-1 alpha-2 format.
    Example: "DE" for Germany
    """

    name: str
    """The name of the representative. E.g. "Max Mustermann" or "Max Mustermann GmbH" """

    role: Literal[
        "DIRECTOR", "PROKURA", "SHAREHOLDER", "OWNER", "PARTNER", "PERSONAL_LIABLE_DIRECTOR", "LIQUIDATOR", "OTHER"
    ]
    """The role of the representation. E.g. "DIRECTOR" """

    start_date: str
    """
    Date when this representative role became effective. Format: ISO 8601
    (YYYY-MM-DD) Example: "2022-01-01"
    """

    type: EntityType
    """Whether the representation is a natural person or a legal entity."""

    id: Optional[str] = None
    """
    Unique identifier for the representative. For companies: Format matches
    company_id pattern For individuals: UUID Example: "DE-HRB-F1103-267645" or UUID
    May be null for certain representatives.
    """

    date_of_birth: Optional[str] = None
    """Date of birth of the representative.

    Only provided for type=natural_person. May still be null for natural persons if
    it is not available. Format: ISO 8601 (YYYY-MM-DD) Example: "1990-01-01"
    """

    end_date: Optional[str] = None
    """
    Date when this representative role ended (if applicable). Format: ISO 8601
    (YYYY-MM-DD) Example: "2022-01-01"
    """

    first_name: Optional[str] = None
    """First name of the representative.

    Only provided for type=natural_person. Example: "Max"
    """

    last_name: Optional[str] = None
    """Last name of the representative.

    Only provided for type=natural_person. Example: "Mustermann"
    """


class Document(BaseModel):
    id: str
    """
    Unique identifier for the document. Example:
    "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    """

    date: str
    """
    Document publication or filing date. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
    """

    latest: bool
    """Whether this is the latest version of the document_type."""

    type: Literal["articles_of_association", "sample_protocol", "shareholder_list"]
    """Categorization of the document:

    - articles_of_association: Company statutes/bylaws
    - sample_protocol: Standard founding protocol
    - shareholder_list: List of company shareholders
    """


class FinancialsIndicator(BaseModel):
    date: str
    """
    Date to which this financial indicator applies. Format: ISO 8601 (YYYY-MM-DD)
    Example: "2022-01-01"
    """

    report_id: str
    """The identifier for the financial report this indicator originates from.

    E.g. "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    """

    type: Literal[
        "balance_sheet_total",
        "net_income",
        "revenue",
        "cash",
        "employees",
        "equity",
        "real_estate",
        "materials",
        "pension_provisions",
        "salaries",
        "taxes",
        "liabilities",
        "capital_reserves",
    ]
    """The type of indicator."""

    value: int
    """
    Value of the indicator in the smallest currency unit (cents). Example: 2099
    represents €20.99 for monetary values For non-monetary values (e.g., employees),
    the actual number.
    """


class FinancialsReport(BaseModel):
    id: str
    """The unique identifier for the financial report.

    E.g. "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    """

    name: str
    """The name of the financial report. E.g. "Jahresabschluss 2022" """

    published_at: str
    """The date when the financial report was published. E.g. "2022-01-01" """


class Financials(BaseModel):
    indicators: List[FinancialsIndicator]
    """
    Key financial metrics extracted from the reports. Includes balance sheet totals,
    revenue, and other important figures.
    """

    reports: List[FinancialsReport]
    """The financial reports of the company."""


class CompanyRetrieveResponse(BaseModel):
    id: str
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    address: CompanyAddress
    """Current registered address of the company."""

    incorporated_at: str
    """
    Date when the company was officially registered. Format: ISO 8601 (YYYY-MM-DD)
    Example: "2022-01-01"
    """

    legal_form: CompanyLegalForm
    """
    Legal form of the company. Example: "gmbh" for Gesellschaft mit beschränkter
    Haftung
    """

    name: CompanyName
    """Current official name of the company."""

    register: CompanyRegister
    """Current registration information of the company."""

    representation: List[Representation]
    """
    List of individuals or entities authorized to represent the company. Includes
    directors, officers, and authorized signatories.
    """

    status: Literal["active", "inactive", "liquidation"]
    """Current status of the company:

    - active: Operating normally
    - inactive: No longer operating
    - liquidation: In the process of being dissolved
    """

    addresses: Optional[List[CompanyAddress]] = None
    """
    Historical addresses, only included when history=true. Shows how the company
    address changed over time.
    """

    capital: Optional[CompanyCapital] = None
    """Current registered capital of the company."""

    capitals: Optional[List[CompanyCapital]] = None
    """
    Historical capital changes, only included when history=true. Shows how the
    company capital changed over time.
    """

    documents: Optional[List[Document]] = None
    """
    Available official documents related to the company, only included when
    documents=true.
    """

    financials: Optional[Financials] = None
    """
    Financial reports and key financial indicators, only included when
    financials=true.
    """

    names: Optional[List[CompanyName]] = None
    """
    Historical company names, only included when history=true. Shows how the company
    name changed over time.
    """

    purpose: Optional[CompanyPurpose] = None
    """Current official business purpose of the company."""

    purposes: Optional[List[CompanyPurpose]] = None
    """
    Historical business purposes, only included when history=true. Shows how the
    company purpose changed over time.
    """

    registers: Optional[List[CompanyRegister]] = None
    """
    Historical registration changes, only included when history=true. Shows how
    registration details changed over time.
    """

    terminated_at: Optional[str] = None
    """
    Date when the company was officially terminated (if applicable). Format: ISO
    8601 (YYYY-MM-DD) Example: "2022-01-01"
    """
