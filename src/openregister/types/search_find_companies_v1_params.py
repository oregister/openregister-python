# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .search_filter_base_param import SearchFilterBaseParam
from .search_request_pagination_param import SearchRequestPaginationParam

__all__ = ["SearchFindCompaniesV1Params", "Filter", "Location", "Query"]


class SearchFindCompaniesV1Params(TypedDict, total=False):
    filters: Iterable[Filter]
    """Filters to filter companies."""

    location: Location
    """Location to filter companies."""

    pagination: SearchRequestPaginationParam
    """Pagination parameters."""

    query: Query
    """Search query to filter companies."""


class Filter(SearchFilterBaseParam, total=False):
    """Filter by field.

    The property sets `value`, `values`, `keywords` and `min`/`max`
    are mutually exclusive. Dates must be YYYY-MM-DD.
    """

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
            "number_of_owners",
            "has_sole_owner",
            "has_representative_owner",
            "is_family_owned",
            "youngest_owner_age",
            "purpose",
            "has_lei",
            "lei",
        ]
    ]


class Location(TypedDict, total=False):
    """Location to filter companies."""

    latitude: Required[float]
    """Latitude to filter on."""

    longitude: Required[float]
    """Longitude to filter on."""

    radius: float
    """Radius in kilometers to filter on. Example: 10"""


class Query(TypedDict, total=False):
    """Search query to filter companies."""

    value: Required[str]
    """Search query to filter companies."""
