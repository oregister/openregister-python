# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .search_filter_base_param import SearchFilterBaseParam
from .search_request_pagination_param import SearchRequestPaginationParam

__all__ = ["SearchFindInsolvenciesV1Params", "Filter", "Query"]


class SearchFindInsolvenciesV1Params(TypedDict, total=False):
    filters: Iterable[Filter]
    """Filters to filter insolvency proceedings."""

    pagination: SearchRequestPaginationParam
    """Pagination parameters."""

    query: Query
    """Search query to filter insolvency proceedings."""


class Filter(SearchFilterBaseParam, total=False):
    """Filter by field.

    The property sets `value`, `values`, `keywords` and `min`/`max`
    are mutually exclusive. Dates must be YYYY-MM-DD.
    """

    field: Required[
        Literal[
            "debtor_kind",
            "debtor_legal_form",
            "court",
            "city",
            "current_status",
            "has_open_insolvency",
            "proceeding_kind",
            "administration_kind",
            "insolvency_grounds",
            "opened_at",
            "closed_at",
            "last_event_at",
            "claims_filing_deadline",
            "company_id",
            "person_id",
        ]
    ]
    """
    Field of the insolvency proceeding to filter on. Date fields (opened_at,
    closed_at, last_event_at, claims_filing_deadline) support min/max ranges with
    values in the format YYYY-MM-DD.
    """


class Query(TypedDict, total=False):
    """Search query to filter insolvency proceedings."""

    value: Required[str]
    """
    Search query to filter insolvency proceedings. Matches against debtor name, case
    number, administrator name and court.
    """
