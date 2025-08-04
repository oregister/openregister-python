# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchFindPersonParams", "Filter", "Pagination", "Query"]


class SearchFindPersonParams(TypedDict, total=False):
    filters: Iterable[Filter]
    """Filters to filter people."""

    pagination: Pagination
    """Pagination parameters."""

    query: Query
    """Search query to filter people."""


class Filter(TypedDict, total=False):
    field: Literal[
        "date_of_birth",
        "city",
        "active",
        "status",
        "legal_form",
        "register_number",
        "register_court",
        "register_type",
        "incorporated_at",
        "zip",
        "address",
        "balance_sheet_total",
        "revenue",
        "cash",
        "employees",
        "equity",
        "real_estate",
        "materials",
        "pension_provisions",
        "salaries",
        "taxes",
        "liabilities",
        "capital_reserves",
        "net_income",
        "industry_codes",
        "capital_amount",
        "capital_currency",
    ]

    keywords: List[str]
    """Keywords to filter on."""

    max: str
    """Maximum value to filter on."""

    min: str
    """Minimum value to filter on."""

    value: str
    """Value to filter on."""

    values: List[str]
    """Values to filter on."""


class Pagination(TypedDict, total=False):
    page: int
    """Page number to return."""

    per_page: int
    """Number of results per page."""


class Query(TypedDict, total=False):
    value: Required[str]
    """Search query to filter people."""
