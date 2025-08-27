# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .entity_type import EntityType
from .company_name import CompanyName
from .company_address import CompanyAddress
from .company_capital import CompanyCapital
from .company_purpose import CompanyPurpose
from .company_register import CompanyRegister
from .company_legal_form import CompanyLegalForm

__all__ = [
    "CompanyGetDetailsV1Response",
    "Document",
    "Indicator",
    "IndustryCodes",
    "IndustryCodesWz2025",
    "Representation",
    "RepresentationLegalPerson",
    "RepresentationNaturalPerson",
]


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


class Indicator(BaseModel):
    balance_sheet_total: Optional[int] = None
    """The balance sheet total of that year (in cents)."""

    capital_reserves: Optional[int] = None
    """The capital reserves of that year (in cents)."""

    cash: Optional[int] = None
    """The cash of that year (in cents)."""

    date: str
    """
    Date to which this financial indicators apply. Format: ISO 8601 (YYYY-MM-DD)
    Example: "2022-01-01"
    """

    employees: Optional[int] = None
    """The number of employees of that year."""

    equity: Optional[int] = None
    """The equity of that year (in cents)."""

    liabilities: Optional[int] = None
    """The liabilities of that year (in cents)."""

    materials: Optional[int] = None
    """The materials of that year (in cents)."""

    net_income: Optional[int] = None
    """The net income of that year (in cents)."""

    pension_provisions: Optional[int] = None
    """The pension provisions of that year (in cents)."""

    real_estate: Optional[int] = None
    """The real estate of that year (in cents)."""

    report_id: str
    """The report id (source) of the indicators."""

    revenue: Optional[int] = None
    """The revenue of that year (in cents)."""

    salaries: Optional[int] = None
    """The salaries of that year (in cents)."""

    taxes: Optional[int] = None
    """The taxes of that year (in cents)."""


class IndustryCodesWz2025(BaseModel):
    code: str


class IndustryCodes(BaseModel):
    wz2025: List[IndustryCodesWz2025] = FieldInfo(alias="WZ2025")


class RepresentationLegalPerson(BaseModel):
    city: Optional[str] = None

    country: str
    """
    Country where the representative is located, in ISO 3166-1 alpha-2 format.
    Example: "DE" for Germany
    """

    name: str


class RepresentationNaturalPerson(BaseModel):
    city: Optional[str] = None
    """City where the representative is located. Example: "Berlin" """

    date_of_birth: Optional[str] = None
    """
    Date of birth of the representative. May still be null for natural persons if it
    is not available. Format: ISO 8601 (YYYY-MM-DD) Example: "1990-01-01"
    """

    first_name: Optional[str] = None
    """First name of the representative. Example: "Max" """

    last_name: Optional[str] = None
    """Last name of the representative. Example: "Mustermann" """


class Representation(BaseModel):
    id: Optional[str] = None
    """
    Unique identifier for the representative. For companies: Format matches
    company_id pattern For individuals: UUID Example: "DE-HRB-F1103-267645" or UUID
    May be null for certain representatives.
    """

    end_date: Optional[str] = None
    """
    Date when this representative role ended (if applicable). Format: ISO 8601
    (YYYY-MM-DD) Example: "2022-01-01"
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

    legal_person: Optional[RepresentationLegalPerson] = None

    natural_person: Optional[RepresentationNaturalPerson] = None


class CompanyGetDetailsV1Response(BaseModel):
    id: str
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    address: CompanyAddress
    """Current registered address of the company."""

    addresses: List[CompanyAddress]
    """Historical addresses. Shows how the company address changed over time."""

    capital: Optional[CompanyCapital] = None
    """Current registered capital of the company."""

    capitals: List[Optional[CompanyCapital]]
    """Historical capital changes. Shows how the company capital changed over time."""

    documents: List[Document]
    """Available official documents related to the company."""

    incorporated_at: str
    """
    Date when the company was officially registered. Format: ISO 8601 (YYYY-MM-DD)
    Example: "2022-01-01"
    """

    indicators: List[Indicator]
    """Key company indicators like net income, employee count, revenue, etc.."""

    industry_codes: IndustryCodes
    """Industry codes of the company."""

    legal_form: CompanyLegalForm
    """
    Legal form of the company. Example: "gmbh" for Gesellschaft mit beschränkter
    Haftung
    """

    name: CompanyName
    """Current official name of the company."""

    names: List[CompanyName]
    """Historical company names. Shows how the company name changed over time."""

    purpose: Optional[CompanyPurpose] = None
    """Current official business purpose of the company."""

    purposes: List[Optional[CompanyPurpose]]
    """Historical business purposes. Shows how the company purpose changed over time."""

    register: CompanyRegister
    """Current registration information of the company."""

    registers: List[CompanyRegister]
    """
    Historical registration changes. Shows how registration details changed over
    time.
    """

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

    terminated_at: Optional[str] = None
    """
    Date when the company was officially terminated (if applicable). Format: ISO
    8601 (YYYY-MM-DD) Example: "2022-01-01"
    """
