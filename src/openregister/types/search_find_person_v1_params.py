# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SearchFindPersonV1Params", "Filter", "Pagination", "Query"]


class SearchFindPersonV1Params(TypedDict, total=False):
    filters: Iterable[Filter]
    """Filters to filter people."""

    pagination: Pagination
    """Pagination parameters."""

    query: Query
    """Search query to filter people."""


class Filter(TypedDict, total=False):
    field: Required[Literal["date_of_birth", "city", "active"]]

    keywords: SequenceNotStr[str]

    max: str

    min: str

    value: str

    values: SequenceNotStr[str]


class Pagination(TypedDict, total=False):
    """Pagination parameters."""

    page: int
    """Page number to return."""

    per_page: int
    """Number of results per page."""


class Query(TypedDict, total=False):
    """Search query to filter people."""

    value: Required[str]
    """Search query to filter people."""
