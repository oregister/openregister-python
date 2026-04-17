# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ExtractCreateV1Response",
    "Document",
    "Report",
    "ReportGroup",
    "ReportStatusFlags",
    "ReportUbo",
    "ReportUboInterest",
    "ReportUboNaturalPerson",
    "ReportValidity",
    "ReportValidityFrom",
    "ReportValidityUntil",
]


class Document(BaseModel):
    """Download URL for a document with format information."""

    document_id: str
    """Stable UUID for this document."""

    filename: str
    """
    Suggested filename for the download. Example: "registerauszug_company_12345.pdf"
    """

    format: str
    """Format of the downloadable document. Example: "xml", "pdf", "json" """

    url: str
    """
    Download URL for the document. Example:
    "https://api.example.com/download/abc123"
    """


class ReportGroup(BaseModel):
    description: Optional[str] = None

    interest_type: Optional[str] = None

    position: Optional[int] = None


class ReportStatusFlags(BaseModel):
    corrected_by_reference: Optional[str] = None

    corrected_references: Optional[List[str]] = None

    deleted: Optional[bool] = None

    deletion_date: Optional[datetime.date] = None

    discrepancy_note: Optional[str] = None


class ReportUboInterest(BaseModel):
    percentage: Optional[float] = None

    scope: Optional[str] = None

    type: Optional[str] = None


class ReportUboNaturalPerson(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    date_of_birth: Optional[datetime.date] = None

    first_name: Optional[str] = None

    full_name: Optional[str] = None

    last_name: Optional[str] = None

    nationalities: Optional[List[str]] = None
    """ISO 3166-1 alpha-2 nationality codes where available."""

    title: Optional[str] = None


class ReportUbo(BaseModel):
    interest: Optional[ReportUboInterest] = None

    natural_person: Optional[ReportUboNaturalPerson] = None

    position: Optional[int] = None


class ReportValidityFrom(BaseModel):
    date: Optional[datetime.date] = None

    note: Optional[str] = None


class ReportValidityUntil(BaseModel):
    date: Optional[datetime.date] = None

    note: Optional[str] = None


class ReportValidity(BaseModel):
    from_: Optional[ReportValidityFrom] = FieldInfo(alias="from", default=None)

    until: Optional[ReportValidityUntil] = None


class Report(BaseModel):
    """Parsed Transparenzregister extract report limited to UBO-relevant fields."""

    created_at: Optional[datetime.date] = None
    """Extract creation date."""

    fictional_ubo_reason: Optional[str] = None
    """Reason indicating no natural person UBO could be determined."""

    groups: Optional[List[ReportGroup]] = None

    notice_type: Optional[str] = None
    """Type of Transparenzregister notice."""

    status_flags: Optional[ReportStatusFlags] = None

    ubos: Optional[List[ReportUbo]] = None

    validity: Optional[ReportValidity] = None


class ExtractCreateV1Response(BaseModel):
    """
    Transparenzregister extract resource including processing state, parsed report, and downloadable documents.
    """

    id: str
    """Stable extract identifier. Example: "tre_12345678" """

    status: Literal["completed", "processing", "failed"]
    """Status of the Transparenzregister extract."""

    company_id: Optional[str] = None
    """
    Company identifier associated with this extract request. May be null when using
    sandbox credentials.
    """

    completed_at: Optional[datetime.datetime] = None
    """Timestamp when extract processing completed."""

    documents: Optional[List[Document]] = None
    """URLs for downloading available extract documents."""

    ekrn: Optional[str] = None
    """EKRN used to request this extract."""

    reference_number: Optional[str] = None
    """Transparenzregister reference number from the extract."""

    report: Optional[Report] = None
    """Parsed Transparenzregister extract report limited to UBO-relevant fields."""

    submitted_at: Optional[datetime.datetime] = None
    """Timestamp when extract submission started."""
