# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination import Pagination
from .insolvency_status import InsolvencyStatus
from .insolvency_debtor_kind import InsolvencyDebtorKind
from .insolvency_proceeding_kind import InsolvencyProceedingKind
from .insolvency_administration_kind import InsolvencyAdministrationKind

__all__ = ["SearchFindInsolvenciesV1Response", "Result"]


class Result(BaseModel):
    id: str
    """Unique insolvency proceeding identifier."""

    administration_kind: Optional[InsolvencyAdministrationKind] = None
    """Kind of administration ordered for the proceeding."""

    administrator_name: Optional[str] = None
    """Name of the insolvency administrator."""

    case_number: str
    """
    Case number of the proceeding at the insolvency court. Example: "36a IN 2792/24"
    """

    city: Optional[str] = None
    """City of the debtor. Example: "Berlin" """

    closed_at: Optional[str] = None
    """Date the proceeding was closed. Format: ISO 8601 (YYYY-MM-DD)"""

    company_id: Optional[str] = None
    """
    Unique company identifier of the debtor, if the debtor could be matched to a
    registered company. Example: DE-HRB-F1103-267645
    """

    court: str
    """Insolvency court handling the proceeding. Example: "Charlottenburg" """

    current_status: InsolvencyStatus
    """Current status of the proceeding."""

    debtor_kind: Optional[InsolvencyDebtorKind] = None
    """Kind of debtor the proceeding concerns.

    - legal_person: legal entities (companies, associations, etc.)
    - natural_person: private individuals
    """

    debtor_legal_form: Optional[str] = None
    """Legal form of the debtor, if the debtor is a company. Example: "gmbh" """

    debtor_name: str
    """Name of the debtor. Example: "Max Mustermann GmbH" """

    has_open_insolvency: bool
    """Whether the proceeding is currently open."""

    insolvency_grounds: Optional[List[str]] = None
    """Grounds for the insolvency, e.g. "illiquidity", "over_indebtedness"."""

    last_event_at: Optional[str] = None
    """Date of the most recent event in the proceeding. Format: ISO 8601 (YYYY-MM-DD)"""

    opened_at: Optional[str] = None
    """Date the proceeding was opened. Format: ISO 8601 (YYYY-MM-DD)"""

    person_id: Optional[str] = None
    """
    Unique person identifier of the debtor, if the debtor could be matched to a
    person.
    """

    proceeding_kind: Optional[InsolvencyProceedingKind] = None
    """Kind of insolvency proceeding."""


class SearchFindInsolvenciesV1Response(BaseModel):
    pagination: Pagination

    results: List[Result]
    """List of insolvency proceedings matching the search criteria."""
