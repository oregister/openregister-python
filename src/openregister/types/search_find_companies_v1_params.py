# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchFindCompaniesV1Params", "Filter", "Location", "Pagination", "Query"]


class SearchFindCompaniesV1Params(TypedDict, total=False):
    filters: Iterable[Filter]
    """Filters to filter companies."""

    location: Location
    """Location to filter companies."""

    pagination: Pagination
    """Pagination parameters."""

    query: Query
    """Search query to filter companies."""


class Filter(TypedDict, total=False):
    field: Required[
        Literal[
            "status",
            "legal_form",
            "register_number",
            "register_court",
            "register_type",
            "city",
            "active",
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
    ]

    keywords: List[str]

    max: str

    min: str

    value: str

    values: List[str]


class Location(TypedDict, total=False):
    latitude: Required[float]
    """Latitude to filter on."""

    longitude: Required[float]
    """Longitude to filter on."""

    radius: float
    """Radius in kilometers to filter on. Example: 10"""


class Pagination(TypedDict, total=False):
    page: int
    """Page number to return."""

    per_page: int
    """Number of results per page."""


class Query(TypedDict, total=False):
    value: Required[str]
    """Search query to filter companies."""
