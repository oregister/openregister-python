# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["JobDocumentCategory"]

JobDocumentCategory: TypeAlias = Literal[
    "current_printout",
    "chronological_printout",
    "historical_printout",
    "structured_information",
    "shareholder_list",
    "articles_of_association",
]
