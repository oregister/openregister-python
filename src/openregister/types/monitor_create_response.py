# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonitorCreateResponse"]


class MonitorCreateResponse(BaseModel):
    disabled: bool
    """Whether the monitor item is disabled."""

    entity_id: str
    """For `company` this is the register ID (e.g.

    `DE-HRB-F1103-267645`). For `person` this is the person UUID.
    """

    entity_type: Literal["company", "person"]
    """Type of the entity to monitor."""

    preferences: List[
        Literal["basic", "representation", "financials", "documents", "ownership", "holdings", "management_positions"]
    ]
    """
    Preferences for the entity to monitor. Use `WebhookMonitorCompanyPreference`
    values when `entity_type` is `company`, and `WebhookMonitorPersonPreference`
    values when `entity_type` is `person`.
    """
