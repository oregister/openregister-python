# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.transparenzregister import request_create_v1_params
from ...types.transparenzregister.request_get_v1_response import RequestGetV1Response
from ...types.transparenzregister.request_create_v1_response import RequestCreateV1Response

__all__ = ["RequestResource", "AsyncRequestResource"]


class RequestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return RequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return RequestResourceWithStreamingResponse(self)

    def create_v1(
        self,
        *,
        company_id: str | Omit = omit,
        x_credential_label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestCreateV1Response:
        """Submit a Transparenzregister request for a company using its company ID.

        This
        endpoint will initiate the Transparenzregister request process and return a
        request ID for tracking.

        Args:
          company_id: Unique company identifier. Required unless using X-Credential-Label=test.
              Example: DE-HRB-F1103-267645

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Credential-Label": x_credential_label}), **(extra_headers or {})}
        return self._post(
            "/v1/transparenzregister/request",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"company_id": company_id}, request_create_v1_params.RequestCreateV1Params),
            ),
            cast_to=RequestCreateV1Response,
        )

    def get_v1(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestGetV1Response:
        """Get the results of a Transparenzregister request.

        This endpoint handles all
        internal complexity including polling request status, selecting all available
        documents, creating Transparenzregister baskets, and returning download URLs
        when ready. If the request is still processing, it will return a pending status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            path_template("/v1/transparenzregister/request/{request_id}", request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestGetV1Response,
        )


class AsyncRequestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return AsyncRequestResourceWithStreamingResponse(self)

    async def create_v1(
        self,
        *,
        company_id: str | Omit = omit,
        x_credential_label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestCreateV1Response:
        """Submit a Transparenzregister request for a company using its company ID.

        This
        endpoint will initiate the Transparenzregister request process and return a
        request ID for tracking.

        Args:
          company_id: Unique company identifier. Required unless using X-Credential-Label=test.
              Example: DE-HRB-F1103-267645

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Credential-Label": x_credential_label}), **(extra_headers or {})}
        return await self._post(
            "/v1/transparenzregister/request",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"company_id": company_id}, request_create_v1_params.RequestCreateV1Params
                ),
            ),
            cast_to=RequestCreateV1Response,
        )

    async def get_v1(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestGetV1Response:
        """Get the results of a Transparenzregister request.

        This endpoint handles all
        internal complexity including polling request status, selecting all available
        documents, creating Transparenzregister baskets, and returning download URLs
        when ready. If the request is still processing, it will return a pending status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            path_template("/v1/transparenzregister/request/{request_id}", request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestGetV1Response,
        )


class RequestResourceWithRawResponse:
    def __init__(self, request: RequestResource) -> None:
        self._request = request

        self.create_v1 = to_raw_response_wrapper(
            request.create_v1,
        )
        self.get_v1 = to_raw_response_wrapper(
            request.get_v1,
        )


class AsyncRequestResourceWithRawResponse:
    def __init__(self, request: AsyncRequestResource) -> None:
        self._request = request

        self.create_v1 = async_to_raw_response_wrapper(
            request.create_v1,
        )
        self.get_v1 = async_to_raw_response_wrapper(
            request.get_v1,
        )


class RequestResourceWithStreamingResponse:
    def __init__(self, request: RequestResource) -> None:
        self._request = request

        self.create_v1 = to_streamed_response_wrapper(
            request.create_v1,
        )
        self.get_v1 = to_streamed_response_wrapper(
            request.get_v1,
        )


class AsyncRequestResourceWithStreamingResponse:
    def __init__(self, request: AsyncRequestResource) -> None:
        self._request = request

        self.create_v1 = async_to_streamed_response_wrapper(
            request.create_v1,
        )
        self.get_v1 = async_to_streamed_response_wrapper(
            request.get_v1,
        )
