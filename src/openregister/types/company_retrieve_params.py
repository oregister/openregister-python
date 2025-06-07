# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CompanyRetrieveParams"]


class CompanyRetrieveParams(TypedDict, total=False):
    documents: bool
    """
    Include document metadata when set to true. Lists available official documents
    related to the company.
    """

    financials: bool
    """
    Include financial data when set to true. Provides access to financial reports
    and key financial indicators.
    """

    history: bool
    """
    Include historical company data when set to true. This returns past names,
    addresses, and other changed information.
    """
