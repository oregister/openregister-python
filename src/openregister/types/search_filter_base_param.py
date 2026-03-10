# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["SearchFilterBaseParam"]


class SearchFilterBaseParam(TypedDict, total=False):
    """Filter by field.

    The property sets `value`, `values`, `keywords` and `min`/`max`
    are mutually exclusive. Dates must be YYYY-MM-DD.
    """

    keywords: SequenceNotStr[str]

    max: str

    min: str

    value: str

    values: SequenceNotStr[str]
