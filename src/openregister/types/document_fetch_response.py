# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentFetchResponse"]


class DocumentFetchResponse(BaseModel):
    category: Literal[
        "current_printout",
        "chronological_printout",
        "historical_printout",
        "structured_information",
        "shareholder_list",
        "articles_of_association",
    ]

    file_date: Optional[str] = None

    file_name: Optional[str] = None

    url: str
