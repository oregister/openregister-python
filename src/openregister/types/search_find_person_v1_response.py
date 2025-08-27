# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SearchFindPersonV1Response", "Pagination", "Result"]


class Pagination(BaseModel):
    page: int
    """Current page number."""

    per_page: int
    """Number of results per page."""

    total_pages: int
    """Total number of pages."""

    total_results: int
    """Total number of results."""


class Result(BaseModel):
    id: str
    """Unique person identifier. Example: 1234-5678-9012-345678901234"""

    active: bool
    """Person status - true if active, false if inactive."""

    city: Optional[str] = None
    """City of the person. Example: "Berlin" """

    date_of_birth: str
    """
    Date of birth of the person. Format: ISO 8601 (YYYY-MM-DD) Example: "1990-01-01"
    """

    name: str
    """Name of the person. Example: "Max Mustermann" """


class SearchFindPersonV1Response(BaseModel):
    pagination: Pagination

    results: List[Result]
    """List of people matching the search criteria."""
