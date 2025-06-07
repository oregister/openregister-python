# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SearchLookupCompanyByURLParams"]


class SearchLookupCompanyByURLParams(TypedDict, total=False):
    url: Required[str]
    """Website URL to search for. Example: "https://openregister.de" """
