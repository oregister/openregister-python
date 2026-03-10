# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Pagination"]


class Pagination(BaseModel):
    page: int
    """Current page number."""

    per_page: int
    """Number of results per page."""

    total_pages: int
    """Total number of pages."""

    total_results: int
    """Total number of results."""
