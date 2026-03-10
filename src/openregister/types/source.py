# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Source"]


class Source(BaseModel):
    document_url: str
    """Url of the source document.

    In the form of a presigned url accessible for 30 minutes.
    """
