# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .insolvency_status import InsolvencyStatus
from .insolvency_debtor_kind import InsolvencyDebtorKind
from .insolvency_proceeding_kind import InsolvencyProceedingKind
from .insolvency_administration_kind import InsolvencyAdministrationKind

__all__ = ["InsolvencyGetDetailsV1Response", "Event", "EventDetails", "EventDetailsMeeting"]


class EventDetailsMeeting(BaseModel):
    """A creditor meeting or hearing announced in the publication."""

    kind: str

    at: Optional[str] = None

    location: Optional[str] = None


class EventDetails(BaseModel):
    """Structured details extracted from the publication, where available."""

    insolvency_grounds: List[str]

    meetings: List[EventDetailsMeeting]

    administrator_address: Optional[str] = None

    administrator_name: Optional[str] = None

    claims_filing_deadline: Optional[str] = None

    closed_at: Optional[str] = None

    discharge_granted: Optional[bool] = None

    distribution_available: Optional[str] = None

    distribution_claims_total: Optional[str] = None


class Event(BaseModel):
    """
    A single published event of an insolvency proceeding, derived from an
    official court publication.
    """

    id: str
    """Unique identifier of the event."""

    details: EventDetails
    """Structured details extracted from the publication, where available."""

    event_type: Literal[
        "preliminary_measures",
        "preliminary_measures_lifted",
        "proceedings_opened",
        "rejected_insufficient_assets",
        "in_proceeding_decision",
        "mass_insufficiency_notified",
        "distribution_announced",
        "distribution_record_filed",
        "final_distribution_announced",
        "proceedings_lifted",
        "proceedings_discontinued",
        "proceedings_terminated",
        "post_termination_decision",
        "subsequent_distribution_ordered",
        "discharge_pending",
        "discharge_granted",
        "discharge_denied",
        "discharge_revoked",
        "plan_confirmed",
        "plan_supervision_ordered",
        "plan_supervision_terminated",
        "other",
    ]
    """Lifecycle event type of the insolvency proceeding."""

    published_at: date
    """Date the event was published by the court. Format: ISO 8601 (YYYY-MM-DD)"""

    report_type: Literal[
        "security_measures",
        "rejection_for_insufficiency_of_assets",
        "openings",
        "decisions_in_proceedings",
        "misc",
        "decisions_after_termination",
        "distribution_lists",
        "decisions_in_discharge_proceedings",
        "supervised_insolvency_plans",
    ]
    """Category of the official publication the event was derived from."""

    summary: str
    """Short summary of the publication."""

    decision_date: Optional[date] = None
    """Date of the court decision, if published. Format: ISO 8601 (YYYY-MM-DD)"""

    effective_at: Optional[datetime] = None
    """Date the decision takes effect, if published."""


class InsolvencyGetDetailsV1Response(BaseModel):
    """An insolvency proceeding with all of its published events."""

    id: str
    """Unique identifier of the insolvency proceeding."""

    case_number: str
    """Case number of the proceeding at the court. Example: "36d IN 3382/25" """

    company_id: Optional[str] = None
    """Unique company identifier of the debtor, if the debtor is a registered company.

    Example: DE-HRB-F1103-267645
    """

    court: str
    """Insolvency court handling the proceeding."""

    current_status: InsolvencyStatus
    """Current status of the insolvency proceeding."""

    debtor_name: str
    """Name of the debtor as published by the court."""

    events: List[Event]
    """All published events of the proceeding, ordered by date."""

    insolvency_grounds: List[str]
    """Grounds for the insolvency (e.g. Zahlungsunfähigkeit, Überschuldung)."""

    administration_kind: Optional[InsolvencyAdministrationKind] = None
    """Kind of administration ordered for the proceeding."""

    administrator_address: Optional[str] = None
    """Address of the insolvency administrator."""

    administrator_name: Optional[str] = None
    """Name of the insolvency administrator."""

    claims_filing_deadline: Optional[date] = None
    """Deadline for creditors to file their claims. Format: ISO 8601 (YYYY-MM-DD)"""

    closed_at: Optional[date] = None
    """Date the proceeding was closed. Format: ISO 8601 (YYYY-MM-DD)"""

    debtor_kind: Optional[InsolvencyDebtorKind] = None
    """Kind of debtor the proceeding concerns.

    - legal_person: legal entities (companies, associations, etc.)
    - natural_person: private individuals
    """

    debtor_legal_form: Optional[str] = None
    """Legal form of the debtor as published by the court."""

    distribution_available: Optional[float] = None
    """Amount available for distribution, in euros."""

    distribution_claims_total: Optional[float] = None
    """Total registered claims in the distribution, in euros."""

    first_event_at: Optional[date] = None
    """
    Publication date of the first known event of the proceeding. Format: ISO 8601
    (YYYY-MM-DD)
    """

    last_event_at: Optional[date] = None
    """
    Publication date of the most recent known event of the proceeding. Format: ISO
    8601 (YYYY-MM-DD)
    """

    opened_at: Optional[date] = None
    """Date the proceeding was opened. Format: ISO 8601 (YYYY-MM-DD)"""

    proceeding_kind: Optional[InsolvencyProceedingKind] = None
    """Kind of insolvency proceeding."""
