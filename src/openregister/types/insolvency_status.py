# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["InsolvencyStatus"]

InsolvencyStatus: TypeAlias = Literal[
    "preliminary",
    "opened",
    "rejected_no_assets",
    "mass_insufficient",
    "plan_supervised",
    "lifted",
    "discontinued",
    "discharge_pending",
    "discharge_granted",
    "discharge_denied",
    "discharge_revoked",
    "unknown",
]
