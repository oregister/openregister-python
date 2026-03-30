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
                "basic", "representation", "financials", "documents", "ownership", "holdings", "management_positions"
            ]
        ]
    ]
    """
    Preferences for the entity to monitor. Use `WebhookMonitorCompanyPreference`
    values when `entity_type` is `company`, and `WebhookMonitorPersonPreference`
    values when `entity_type` is `person`.
    """
