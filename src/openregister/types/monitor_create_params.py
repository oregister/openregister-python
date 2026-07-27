# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MonitorCreateParams"]


class MonitorCreateParams(TypedDict, total=False):
    entity_id: Required[str]
    """For `company` this is the register ID (e.g.

    `DE-HRB-F1103-267645`). For `person` this is the person UUID.
    """

    entity_type: Required[Literal["company", "person"]]
    """Type of the entity to monitor."""

    preferences: Required[
        List[
            Literal[
                "basic",
                "representation",
                "financials",
                "documents",
                "ownership",
                "holdings",
                "management_positions",
                "insolvencies",
            ]
        ]
    ]
    """
    Preferences for the entity to monitor. Use `WebhookMonitorCompanyPreference`
    values when `entity_type` is `company`, and `WebhookMonitorPersonPreference`
    values when `entity_type` is `person`.
    """

    update_frequency: Literal["daily", "weekly"]
    """
    How often the monitored company is checked for register updates. Defaults to
    `weekly` if not provided.

    Only supported when `entity_type` is `company`. Requests for `person` monitors
    that include this field are rejected with a validation error.

    Daily monitors are billed at a premium: 50 credits at creation and 50 credits
    per month while active, instead of the standard 25.
    """
