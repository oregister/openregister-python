# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SearchAutocompleteCompaniesV1Params"]


class SearchAutocompleteCompaniesV1Params(TypedDict, total=False):
    query: Required[str]
    """
    Text search query to find companies by name. Example: "Descartes Technologies
    UG"
    """
