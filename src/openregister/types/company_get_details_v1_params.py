# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CompanyGetDetailsV1Params"]


class CompanyGetDetailsV1Params(TypedDict, total=False):
    realtime: bool
    """
    Get the most up-to-date company information directly from the Handelsregister.
    When set to true, we fetch the latest data in real-time from the official German
    commercial register, ensuring you receive the most current company details.
    Note: Real-time requests take longer but guarantee the freshest data available.
    """
