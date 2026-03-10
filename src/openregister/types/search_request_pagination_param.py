# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SearchRequestPaginationParam"]


class SearchRequestPaginationParam(TypedDict, total=False):
    page: int
    """Page number to return."""

    per_page: int
    """Number of results per page."""
