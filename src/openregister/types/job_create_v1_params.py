# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .job_type import JobType
from .job_document_category import JobDocumentCategory

__all__ = ["JobCreateV1Params"]


class JobCreateV1Params(TypedDict, total=False):
    company_id: Required[str]
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    type: Required[JobType]

    document_category: JobDocumentCategory
