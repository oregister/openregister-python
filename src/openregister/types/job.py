# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .job_type import JobType
from .job_document_category import JobDocumentCategory
from .company_get_owners_v1_response import CompanyGetOwnersV1Response
from .company_get_details_v1_response import CompanyGetDetailsV1Response

__all__ = ["Job", "Results", "ResultsDocument"]


class ResultsDocument(BaseModel):
    """The fetched document of a `document` job."""

    file_date: Optional[date] = None

    file_name: Optional[str] = None

    url: str
    """Download URL of the document. It expires; read the job again for a new one."""


class Results(BaseModel):
    """The result of a completed job. Only the field of the job's type is set."""

    company: Optional[CompanyGetDetailsV1Response] = None
    """The refreshed company of a `company` job."""

    document: Optional[ResultsDocument] = None
    """The fetched document of a `document` job."""

    owners: Optional[CompanyGetOwnersV1Response] = None
    """The refreshed owners of an `owners` job."""


class Job(BaseModel):
    id: str
    """Unique job identifier. Example: f47ac10b-58cc-4372-a567-0e02b2c3d479"""

    company_id: str
    """Company the job refreshes.

    For `company` and `owners` jobs this is the company's latest register ID, which
    differs from the requested one when the company moved to another register.
    Example: DE-HRB-F1103-267645
    """

    created_at: datetime

    document_category: Optional[JobDocumentCategory] = None

    expires_at: Optional[datetime] = None
    """Until when a completed job returns `results`, 12 hours after it finished."""

    finished_at: Optional[datetime] = None

    reason: Optional[Literal["not_available", "timeout", "internal_error"]] = None
    """Why a failed job failed:

    - `not_available`: the register holds no such document for this company.
    - `timeout`: the Handelsregister did not answer in time; try again later.
    - `internal_error`: any other failure.
    """

    results: Optional[Results] = None
    """The result of a completed job. Only the field of the job's type is set."""

    status: Literal["pending", "completed", "failed"]

    type: JobType
