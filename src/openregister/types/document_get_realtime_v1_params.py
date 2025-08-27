# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DocumentGetRealtimeV1Params"]


class DocumentGetRealtimeV1Params(TypedDict, total=False):
    company_id: Required[str]

    document_category: Required[
        Literal[
            "current_printout",
            "chronological_printout",
            "historical_printout",
            "structured_information",
            "shareholder_list",
            "articles_of_association",
        ]
    ]
