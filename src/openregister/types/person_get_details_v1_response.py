# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PersonGetDetailsV1Response", "ManagementPosition", "ManagementPositionRoleDetail"]


class ManagementPositionRoleDetail(BaseModel):
    """The precise role as recorded in the register, plus ready-to-display
    titles.

    A Vorstand and a Geschäftsführer differ here.
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


class ManagementPosition(BaseModel):
    """All current and past management positions of the person."""

    company_name: str
    """Name of the company. Example: "Descartes Technologies GmbH" """

    register_id: str
    """Register ID of the company. Example: DE-HRB-F1103-267645"""

    role: str
    """Raw role string as stored, kept for backwards compatibility.

    It is register-level rather than bucketed, and for Prokura it carries a German
    string ("Einzelprokura", "Gesamtprokura", "Prokura"). Prefer `role_detail`.
    Example: "EXECUTIVE"
    """

    role_detail: ManagementPositionRoleDetail
    """The precise role as recorded in the register, plus ready-to-display titles.

    A Vorstand and a Geschäftsführer differ here.
    """

    start_date: date
    """
    Date when the person started the management position. Format: ISO 8601
    (YYYY-MM-DD) Example: "2022-01-01"
    """

    end_date: Optional[date] = None
    """
    Date when the person ended the management position. Format: ISO 8601
    (YYYY-MM-DD) Example: "2023-01-01"
    """


class PersonGetDetailsV1Response(BaseModel):
    id: str
    """Unique person identifier. Example: cc78ab54-d958-49b8-bae7-2f6c0c308837"""

    age: Optional[int] = None
    """Age of the person."""

    city: str
    """City of the person."""

    date_of_birth: Optional[date] = None
    """
    Date of birth of the person. Format: ISO 8601 (YYYY-MM-DD) Example: "1990-01-01"
    """

    first_name: str
    """First name of the person."""

    last_name: str
    """Last name of the person."""

    management_positions: List[ManagementPosition]
    """Management positions of the person."""
