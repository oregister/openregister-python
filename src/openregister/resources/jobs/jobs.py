# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .document import (
    DocumentResource,
    AsyncDocumentResource,
    DocumentResourceWithRawResponse,
    AsyncDocumentResourceWithRawResponse,
    DocumentResourceWithStreamingResponse,
    AsyncDocumentResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def document(self) -> DocumentResource:
        return DocumentResource(self._client)

    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def document(self) -> AsyncDocumentResource:
        return AsyncDocumentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

    @cached_property
    def document(self) -> DocumentResourceWithRawResponse:
        return DocumentResourceWithRawResponse(self._jobs.document)


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

    @cached_property
    def document(self) -> AsyncDocumentResourceWithRawResponse:
        return AsyncDocumentResourceWithRawResponse(self._jobs.document)


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

    @cached_property
    def document(self) -> DocumentResourceWithStreamingResponse:
        return DocumentResourceWithStreamingResponse(self._jobs.document)


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

    @cached_property
    def document(self) -> AsyncDocumentResourceWithStreamingResponse:
        return AsyncDocumentResourceWithStreamingResponse(self._jobs.document)
