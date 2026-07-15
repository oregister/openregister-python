# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UsageGetCreditsV1Response", "Period"]


class Period(BaseModel):
    reset_at: datetime

    type: Literal["billing_cycle", "rolling_30_days"]
    """
    billing_cycle for paid plans; rolling_30_days for the free plan, where the
    window starts with the first request.
    """


class UsageGetCreditsV1Response(BaseModel):
    included_credits: int

    overage_credits: int
    """Credits above the included allowance."""

    paid: bool

    period: Period

    remaining_credits: int
    """Never negative; zero once usage exceeds included credits."""

    used_credits: int
