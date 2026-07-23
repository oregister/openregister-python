# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .source import Source
from .._models import BaseModel
from .entity_type import EntityType
from .company_name import CompanyName
from .company_address import CompanyAddress
from .company_capital import CompanyCapital
from .company_purpose import CompanyPurpose
from .company_document import CompanyDocument
from .company_register import CompanyRegister
from .insolvency_status import InsolvencyStatus
from .company_legal_form import CompanyLegalForm
from .representation_role import RepresentationRole
from .insolvency_proceeding_kind import InsolvencyProceedingKind
from .insolvency_administration_kind import InsolvencyAdministrationKind

__all__ = [
    "CompanyGetDetailsV1Response",
    "Acquisition",
    "AssetSpinOff",
    "Contact",
    "ContactSocialMedia",
    "Indicator",
    "IndustryCodes",
    "IndustryCodesWz2025",
    "MergedInto",
    "ProfitTransferAgreement",
    "Representation",
    "RepresentationLegalPerson",
    "RepresentationNaturalPerson",
    "Insolvency",
]


class Acquisition(BaseModel):
    agreement_date: Optional[str] = None
    """
    Date the underlying contract (Verschmelzungsvertrag) was concluded, as cited in
    the register entry. Null when the register text does not cite a contract date.
    Entries sharing an agreement_date belong to the same transaction. Format: ISO
    8601 (YYYY-MM-DD)
    """

    company_id: str
    """
    Unique company identifier of the company that was merged into this company.
    Example: DE-HRB-F1103-267645
    """

    name: str
    """Current name of the company that was merged into this company."""

    registration_date: str
    """Date the merger was registered. Format: ISO 8601 (YYYY-MM-DD)"""


class AssetSpinOff(BaseModel):
    agreement_date: Optional[str] = None
    """
    Date the underlying contract (Ausgliederungsvertrag) was concluded, as cited in
    the register entry. Null when the register text does not cite a contract date.
    Entries sharing an agreement_date belong to the same transaction. Format: ISO
    8601 (YYYY-MM-DD)
    """

    company_id: str
    """
    Unique company identifier of the company that received the assets. Example:
    DE-HRB-F1103-267645
    """

    name: str
    """Current name of the company that received the assets."""

    registration_date: str
    """Date the spin-off was registered. Format: ISO 8601 (YYYY-MM-DD)"""


class ContactSocialMedia(BaseModel):
    facebook: Optional[str] = None

    github: Optional[str] = None

    instagram: Optional[str] = None

    linkedin: Optional[str] = None

    tiktok: Optional[str] = None

    twitter: Optional[str] = None

    xing: Optional[str] = None

    youtube: Optional[str] = None


class Contact(BaseModel):
    """Contact information of the company."""

    social_media: ContactSocialMedia

    website_url: str

    email: Optional[str] = None

    phone: Optional[str] = None

    vat_id: Optional[str] = None


class Indicator(BaseModel):
    """
    A focused subset of the key company indicators for a given year.
    Values of the indicator are given in the smallest currency unit (cents).
    Example: 2099 represents €20.99 for monetary values.
    For non-monetary values (e.g., employees), the actual number.
    """

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
    """Industry codes from WZ 2025."""

    code: str


class IndustryCodes(BaseModel):
    """Industry codes of the company."""

    wz2025: List[IndustryCodesWz2025] = FieldInfo(alias="WZ2025")


class MergedInto(BaseModel):
    """
    If the company ceased to exist through a merger (Verschmelzung),
    the company it was merged into.
    """

    agreement_date: Optional[str] = None
    """
    Date the underlying contract (Verschmelzungsvertrag) was concluded, as cited in
    the register entry. Null when the register text does not cite a contract date.
    Entries sharing an agreement_date belong to the same transaction. Format: ISO
    8601 (YYYY-MM-DD)
    """

    company_id: str
    """
    Unique company identifier of the company this company was merged into. Example:
    DE-HRB-F1103-267645
    """

    name: str
    """Current name of the company this company was merged into."""

    registration_date: str
    """Date the merger was registered. Format: ISO 8601 (YYYY-MM-DD)"""


class ProfitTransferAgreement(BaseModel):
    """
    The company's current profit and loss transfer agreement
    (Gewinnabführungsvertrag), if one exists. The referenced company
    is the parent receiving this company's profit (Organträger).
    Null if the company has no active agreement.
    """

    agreement_date: Optional[str] = None
    """
    Date the underlying contract (Gewinnabführungsvertrag) was concluded, as cited
    in the register entry. Null when the register text does not cite a contract
    date. Entries sharing an agreement_date belong to the same transaction. Format:
    ISO 8601 (YYYY-MM-DD)
    """

    company_id: str
    """
    Unique company identifier of the parent company receiving this company's profit
    (Organträger). Example: DE-HRB-F1103-267645
    """

    name: str
    """Current name of the parent company."""

    registration_date: str
    """Date the agreement was registered. Format: ISO 8601 (YYYY-MM-DD)"""


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

    authority: Optional[str] = None
    """
    The representative's current individual representation authority (individuelle
    Vertretungsbefugnis), as published in the register. Null if no special authority
    is recorded. Example: "einzelvertretungsberechtigt mit der Befugnis, im Namen
    der Gesellschaft mit sich im eigenen Namen Rechtsgeschäfte abzuschließen"
    """

    end_date: Optional[str] = None
    """
    Date when this representative role ended (if applicable). Format: ISO 8601
    (YYYY-MM-DD) Example: "2022-01-01"
    """

    name: str
    """The name of the representative. E.g. "Max Mustermann" or "Max Mustermann GmbH" """

    role: RepresentationRole
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


class Insolvency(BaseModel):
    """
    Basic information about an insolvency proceeding of the company.
    Use the insolvency endpoint to retrieve all events of the proceeding.
    """

    id: str
    """Unique identifier of the insolvency proceeding."""

    case_number: str
    """Case number of the proceeding at the court. Example: "36d IN 3382/25" """

    court: str
    """Insolvency court handling the proceeding."""

    current_status: InsolvencyStatus
    """Current status of the insolvency proceeding."""

    administration_kind: Optional[InsolvencyAdministrationKind] = None
    """Kind of administration ordered for the proceeding."""

    closed_at: Optional[datetime] = None
    """Date the proceeding was closed."""

    opened_at: Optional[datetime] = None
    """Date the proceeding was opened."""

    proceeding_kind: Optional[InsolvencyProceedingKind] = None
    """Kind of insolvency proceeding."""


class CompanyGetDetailsV1Response(BaseModel):
    id: str
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    acquisitions: List[Acquisition]
    """
    Companies that were merged into this company (Verschmelzung durch Aufnahme, as
    the acquiring entity).
    """

    address: CompanyAddress
    """Current registered address of the company."""

    addresses: List[CompanyAddress]
    """Historical addresses. Shows how the company address changed over time."""

    asset_spin_offs: List[AssetSpinOff]
    """Spin-offs (Ausgliederung, § 123 Abs.

    3 UmwG) in which this company transferred assets to another company as the
    transferring entity.
    """

    capital: Optional[CompanyCapital] = None
    """Current registered capital of the company."""

    capitals: List[CompanyCapital]
    """Historical capital changes. Shows how the company capital changed over time."""

    contact: Optional[Contact] = None
    """Contact information of the company."""

    documents: List[CompanyDocument]
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

    merged_into: Optional[MergedInto] = None
    """
    If the company ceased to exist through a merger (Verschmelzung), the company it
    was merged into.
    """

    name: CompanyName
    """Current official name of the company."""

    names: List[CompanyName]
    """Historical company names. Shows how the company name changed over time."""

    notarized_at: Optional[str] = None
    """
    Date of the notarized company agreement (Gesellschaftsvertrag or Satzung).
    Format: ISO 8601 (YYYY-MM-DD) Example: "2021-12-21"
    """

    profit_transfer_agreement: Optional[ProfitTransferAgreement] = None
    """
    The company's current profit and loss transfer agreement
    (Gewinnabführungsvertrag), if one exists. The referenced company is the parent
    receiving this company's profit (Organträger). Null if the company has no active
    agreement.
    """

    purpose: Optional[CompanyPurpose] = None
    """Current official business purpose of the company."""

    purposes: List[CompanyPurpose]
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

    representation_rule: Optional[str] = None
    """
    The company's current general representation rule (allgemeine
    Vertretungsregelung), as published in the register. Example: "Ist nur ein
    Geschäftsführer bestellt, so vertritt er die Gesellschaft allein. Sind mehrere
    Geschäftsführer bestellt, so wird die Gesellschaft durch zwei Geschäftsführer
    oder durch einen Geschäftsführer gemeinsam mit einem Prokuristen vertreten."
    """

    sources: List[Source]
    """Sources of the company data."""

    status: Literal["active", "inactive", "liquidation"]
    """Current status of the company:

    - active: Operating normally
    - inactive: No longer operating
    - liquidation: In the process of being dissolved
    """

    terminated_at: Optional[str] = None
    """
    Date when the company was officially terminated (if applicable). Format: ISO
    8601 (YYYY-MM-DD) Example: "2024-01-01"
    """

    insolvencies: Optional[List[Insolvency]] = None
    """
    Insolvency proceedings of the company, if any. Contains basic information per
    proceeding; use the insolvency endpoint to retrieve all events of a proceeding.
    """

    lei: Optional[str] = None
    """Legal Entity Identifier (LEI), if available."""
