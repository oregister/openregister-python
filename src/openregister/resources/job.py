# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import JobType, JobDocumentCategory, job_create_v1_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.job import Job
from .._base_client import make_request_options
from ..types.job_type import JobType
from ..types.job_document_category import JobDocumentCategory

__all__ = ["JobResource", "AsyncJobResource"]


class JobResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return JobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return JobResourceWithStreamingResponse(self)

    def create_v1(
        self,
        *,
        company_id: str,
        type: JobType,
        document_category: JobDocumentCategory | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """Start a realtime request without waiting for it.

        The request returns at once
        with a pending job. Use this instead of `realtime=true` when your client cannot
        keep a request open for the minutes the Handelsregister may take.

        Job types:

        - `company`: refreshes the company from the Handelsregister, like
          `GET /v1/company/{company_id}?realtime=true`.
        - `owners`: refreshes the company's owners, like
          `GET /v1/company/{company_id}/owners?realtime=true`.
        - `document`: fetches one document, like `GET /v1/document`. Requires
          `document_category`.

        Follow a job either way, or both:

        - Poll `GET /v1/jobs/{job_id}` until `status` is `completed` or `failed`. A
          completed job carries its result in `results`: the document for a `document`
          job, the company or its owners for a `company` or `owners` job.
        - Configure a webhook endpoint: when the job finishes, OpenRegister sends a
          `job.completed` or `job.failed` webhook to it. The job can be polled all the
          same.

        Jobs are available on paid plans. A completed job costs what the same request
        with `realtime=true` costs: 20 credits for `company` and `owners`, 10 for
        `document`. Failed jobs and polling are free.

        Args:
          company_id: Unique company identifier. Example: DE-HRB-F1103-267645

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/jobs",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "type": type,
                    "document_category": document_category,
                },
                job_create_v1_params.JobCreateV1Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )

    def get_v1(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """Get a job's status and, once it completed, its result in `results`.

        Polling is
        free.

        - `document` jobs return `results.document` with a download URL, presigned again
          on every read.
        - `company` jobs return `results.company`, the same as
          `GET /v1/company/{company_id}`.
        - `owners` jobs return `results.owners`, the same as
          `GET /v1/company/{company_id}/owners`.

        Results are returned for 12 hours after the job finished (`expires_at`); after
        that, `results` is null and the regular endpoints serve the data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template("/v1/jobs/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )


class AsyncJobResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return AsyncJobResourceWithStreamingResponse(self)

    async def create_v1(
        self,
        *,
        company_id: str,
        type: JobType,
        document_category: JobDocumentCategory | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """Start a realtime request without waiting for it.

        The request returns at once
        with a pending job. Use this instead of `realtime=true` when your client cannot
        keep a request open for the minutes the Handelsregister may take.

        Job types:

        - `company`: refreshes the company from the Handelsregister, like
          `GET /v1/company/{company_id}?realtime=true`.
        - `owners`: refreshes the company's owners, like
          `GET /v1/company/{company_id}/owners?realtime=true`.
        - `document`: fetches one document, like `GET /v1/document`. Requires
          `document_category`.

        Follow a job either way, or both:

        - Poll `GET /v1/jobs/{job_id}` until `status` is `completed` or `failed`. A
          completed job carries its result in `results`: the document for a `document`
          job, the company or its owners for a `company` or `owners` job.
        - Configure a webhook endpoint: when the job finishes, OpenRegister sends a
          `job.completed` or `job.failed` webhook to it. The job can be polled all the
          same.

        Jobs are available on paid plans. A completed job costs what the same request
        with `realtime=true` costs: 20 credits for `company` and `owners`, 10 for
        `document`. Failed jobs and polling are free.

        Args:
          company_id: Unique company identifier. Example: DE-HRB-F1103-267645

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/jobs",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "type": type,
                    "document_category": document_category,
                },
                job_create_v1_params.JobCreateV1Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )

    async def get_v1(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """Get a job's status and, once it completed, its result in `results`.

        Polling is
        free.

        - `document` jobs return `results.document` with a download URL, presigned again
          on every read.
        - `company` jobs return `results.company`, the same as
          `GET /v1/company/{company_id}`.
        - `owners` jobs return `results.owners`, the same as
          `GET /v1/company/{company_id}/owners`.

        Results are returned for 12 hours after the job finished (`expires_at`); after
        that, `results` is null and the regular endpoints serve the data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template("/v1/jobs/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )


class JobResourceWithRawResponse:
    def __init__(self, job: JobResource) -> None:
        self._job = job

        self.create_v1 = to_raw_response_wrapper(
            job.create_v1,
        )
        self.get_v1 = to_raw_response_wrapper(
            job.get_v1,
        )


class AsyncJobResourceWithRawResponse:
    def __init__(self, job: AsyncJobResource) -> None:
        self._job = job

        self.create_v1 = async_to_raw_response_wrapper(
            job.create_v1,
        )
        self.get_v1 = async_to_raw_response_wrapper(
            job.get_v1,
        )


class JobResourceWithStreamingResponse:
    def __init__(self, job: JobResource) -> None:
        self._job = job

        self.create_v1 = to_streamed_response_wrapper(
            job.create_v1,
        )
        self.get_v1 = to_streamed_response_wrapper(
            job.get_v1,
        )


class AsyncJobResourceWithStreamingResponse:
    def __init__(self, job: AsyncJobResource) -> None:
        self._job = job

        self.create_v1 = async_to_streamed_response_wrapper(
            job.create_v1,
        )
        self.get_v1 = async_to_streamed_response_wrapper(
            job.get_v1,
        )
