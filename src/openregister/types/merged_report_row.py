# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List

from .._models import BaseModel

__all__ = ["MergedReportRow"]


class MergedReportRow(BaseModel):
    children: List["MergedReportRow"]

    formatted_name: str

    name: str

    values: Dict[str, int]
    """Report end date to value mapping (ISO date string as key)"""
