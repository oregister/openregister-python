# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .search_filter_base_param import SearchFilterBaseParam
from .search_request_pagination_param import SearchRequestPaginationParam

__all__ = ["SearchFindPersonV1Params", "Filter", "Query"]


class SearchFindPersonV1Params(TypedDict, total=False):
    filters: Iterable[Filter]
    """Filters to filter people."""

    pagination: SearchRequestPaginationParam
    """Pagination parameters."""

    query: Query
    """Search query to filter people."""


class Filter(SearchFilterBaseParam, total=False):
    """Filter by field.

    The property sets `value`, `values`, `keywords` and `min`/`max`
    are mutually exclusive. Dates must be YYYY-MM-DD.
    """

    field: Required[Literal["date_of_birth", "city", "active"]]


class Query(TypedDict, total=False):
    """Search query to filter people."""

    value: Required[str]
    """Search query to filter people."""
