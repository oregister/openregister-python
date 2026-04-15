# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransparenzregisterSetCredentialsV1Params"]


class TransparenzregisterSetCredentialsV1Params(TypedDict, total=False):
    password: Required[str]
    """Password for Transparenzregister API access."""

    username: Required[str]
    """
    Username for Transparenzregister API access. Example:
    "testnutzer-eis@transparenzregister.de"
    """

    credential_label: str
    """Label to identify this set of credentials.

    Allows storing multiple Transparenzregister credentials per user (e.g., for
    different accounts or clients). Defaults to 'default' if not provided. Example:
    "client_a"
    """
