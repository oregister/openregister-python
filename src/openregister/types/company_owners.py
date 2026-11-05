# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .source import Source
from .._models import BaseModel
from .entity_type import EntityType
from .company_relation_type import CompanyRelationType
from .company_owner_legal_person import CompanyOwnerLegalPerson
from .company_owner_natural_person import CompanyOwnerNaturalPerson

__all__ = ["CompanyOwners", "Owner", "OwnerRoleDetail"]


class OwnerRoleDetail(BaseModel):
    """The precise role as recorded in the register, plus ready-to-display
    titles.

    A Kommanditist and a Gesellschafter both appear here with
    their register-level role, while `relation_type` only carries the
    coarse bucket.
    """

    code: Literal[
        "DIRECTOR",
        "EMERGENCY_DIRECTOR",
        "EXECUTIVE",
        "CHAIRMAN",
        "DEPUTY_CHAIRMAN",
        "BOARD",
        "PRESIDENT_BOARD",
        "VICE_PRESIDENT_BOARD",
        "PRESIDENT",
        "MEMBER",
        "NON_EXECUTIVE_DIRECTOR",
        "BOARD_SECRETARY",
        "BOARD_TREASURER",
        "BOARD_SPORTS",
        "BOARD_OTHER",
        "REPRESENTATIVE",
        "SECONDARY_REPRESENTATIVE",
        "COURT_ORDERED_REPRESENTATIVE",
        "PROKURA",
        "PROKURA_SINGLE",
        "PROKURA_JOINT",
        "LIQUIDATOR",
        "INSOLVENCY_DIRECTOR",
        "PRELIMINARY_INSOLVENCY_DIRECTOR",
        "OWNER",
        "SHAREHOLDER",
        "PARTNER",
        "PERSONAL_LIABLE_DIRECTOR",
        "LIMITED_PARTNER",
        "OTHER",
    ]
    """
    The precise role as recorded in the register. Example: "EXECUTIVE" for a
    Vorstand, "DIRECTOR" for a Geschäftsführer — both have role "DIRECTOR".
    """

    label_de: str
    """German title, gender-neutral, as shown on openregister.de. Example: "Vorstand" """

    label_de_short: str
    """Abbreviated German title, for dense layouts such as tables. Example: "Vst." """

    label_en: str
    """English title.

    A translation for display, not a legal term — the German title is the one the
    register uses. Example: "Executive Board Member"
    """

    label_en_short: str
    """Abbreviated English title, for dense layouts such as tables. Example: "Exec.

    Board"
    """


class Owner(BaseModel):
    id: Optional[str] = None
    """
    Unique identifier for the shareholder. For companies: Format matches company_id
    pattern For individuals: UUID Example: "DE-HRB-F1103-267645" or UUID May be null
    for certain shareholders.
    """

    legal_person: Optional[CompanyOwnerLegalPerson] = None
    """Details about the legal person."""

    name: str
    """The name of the shareholder. E.g. "Max Mustermann" or "Max Mustermann GmbH" """

    natural_person: Optional[CompanyOwnerNaturalPerson] = None
    """Details about the natural person."""

    nominal_share: float
    """Nominal value of shares in Euro. Example: 100"""

    percentage_share: Optional[float] = None
    """Percentage of company ownership. Example: 5.36 represents 5.36% ownership"""

    relation_type: CompanyRelationType
    """
    Type of relationship between the entity and the company. Use `role_detail` for
    the precise register role.
    """

    role_detail: OwnerRoleDetail
    """The precise role as recorded in the register, plus ready-to-display titles.

    A Kommanditist and a Gesellschafter both appear here with their register-level
    role, while `relation_type` only carries the coarse bucket.
    """

    start: Optional[date] = None
    """Date when the relation started.

    Only available for some types of owners. Format: ISO 8601 (YYYY-MM-DD) Example:
    "2022-01-01"
    """

    type: EntityType
    """The type of shareholder."""


class CompanyOwners(BaseModel):
    best_available: bool
    """
    When true, the returned owner data is the best available but may not reflect the
    most current ownership state. This applies to AG and SE companies where
    ownership data is sourced from Handelsregister decision and articles of
    association documents, which are not filed on every ownership change.
    """

    company_id: str
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    owners: List[Owner]

    sources: List[Source]
    """Sources of the company owners data."""
