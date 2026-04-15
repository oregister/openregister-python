# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RequestCreateV1Response"]


class RequestCreateV1Response(BaseModel):
    """Response from submitting a document request."""

    request_id: str
    """Request ID for tracking the document request. Example: "req_12345678" """
