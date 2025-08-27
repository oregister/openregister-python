# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentGetCachedV1Response"]


class DocumentGetCachedV1Response(BaseModel):
    id: str
    """The unique identifier for the document.

    E.g. "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    """

    date: str
    """The date of the document. E.g. "2022-01-01" """

    name: str
    """The name of the document. E.g. "Musterprotokoll vom 01.01.2022" """

    type: Literal["articles_of_association", "sample_protocol", "shareholder_list"]
    """The type of document."""

    url: str
    """The URL of the document.

    It can be downloaded from there. Only valid for 15 minutes after the request.
    """
