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
from ...types.transparenzregister import extract_create_v1_params
from ...types.transparenzregister.transparenzregister_extract import TransparenzregisterExtract

__all__ = ["ExtractResource", "AsyncExtractResource"]


class ExtractResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return ExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return ExtractResourceWithStreamingResponse(self)

    def create_v1(
        self,
        *,
        company_id: str | Omit = omit,
        x_credential_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransparenzregisterExtract:
        """
        Submit a Transparenzregister extract request and return an extract resource with
        processing status.

        Sandbox integration testing (recommended for all non-production testing):

        - Send `X-Credential-Name: sandbox`.
        - Do not send `company_id` (an empty body `{}` is valid).
        - OpenRegister uses the Transparenzregister test environment and built-in test
          authentication.
        - The request is submitted with the fixed test EKRN `DE727032388716`.
        - The response has `company_id: null`.

        Production usage:

        - Omit `X-Credential-Name` or use `default` / another stored credential name.
        - `company_id` is required and must resolve to exactly one Transparenzregister
          legal entity.

        Args:
          company_id: Unique company identifier. Required unless `X-Credential-Name` is set to
              `sandbox`. In sandbox mode this field should be omitted. Example:
              DE-HRB-F1103-267645

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Credential-Name": x_credential_name}), **(extra_headers or {})}
        return self._post(
            "/v1/transparenzregister/extracts",
            body=maybe_transform({"company_id": company_id}, extract_create_v1_params.ExtractCreateV1Params),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransparenzregisterExtract,
        )

    def get_v1(
        self,
        extract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransparenzregisterExtract:
        """Get the results of a Transparenzregister extract request.

        This endpoint handles
        all internal complexity including polling request status, selecting all
        available documents, creating Transparenzregister baskets, and returning
        download URLs when ready. If the request is still processing, it will return a
        pending status. Polling reuses the credential mode stored on the extract at
        create time. Sandbox extracts keep using the Transparenzregister test client
        automatically; no credential header is accepted on this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extract_id:
            raise ValueError(f"Expected a non-empty value for `extract_id` but received {extract_id!r}")
        return self._get(
            path_template("/v1/transparenzregister/extracts/{extract_id}", extract_id=extract_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransparenzregisterExtract,
        )


class AsyncExtractResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return AsyncExtractResourceWithStreamingResponse(self)

    async def create_v1(
        self,
        *,
        company_id: str | Omit = omit,
        x_credential_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransparenzregisterExtract:
        """
        Submit a Transparenzregister extract request and return an extract resource with
        processing status.

        Sandbox integration testing (recommended for all non-production testing):

        - Send `X-Credential-Name: sandbox`.
        - Do not send `company_id` (an empty body `{}` is valid).
        - OpenRegister uses the Transparenzregister test environment and built-in test
          authentication.
        - The request is submitted with the fixed test EKRN `DE727032388716`.
        - The response has `company_id: null`.

        Production usage:

        - Omit `X-Credential-Name` or use `default` / another stored credential name.
        - `company_id` is required and must resolve to exactly one Transparenzregister
          legal entity.

        Args:
          company_id: Unique company identifier. Required unless `X-Credential-Name` is set to
              `sandbox`. In sandbox mode this field should be omitted. Example:
              DE-HRB-F1103-267645

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Credential-Name": x_credential_name}), **(extra_headers or {})}
        return await self._post(
            "/v1/transparenzregister/extracts",
            body=await async_maybe_transform(
                {"company_id": company_id}, extract_create_v1_params.ExtractCreateV1Params
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransparenzregisterExtract,
        )

    async def get_v1(
        self,
        extract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransparenzregisterExtract:
        """Get the results of a Transparenzregister extract request.

        This endpoint handles
        all internal complexity including polling request status, selecting all
        available documents, creating Transparenzregister baskets, and returning
        download URLs when ready. If the request is still processing, it will return a
        pending status. Polling reuses the credential mode stored on the extract at
        create time. Sandbox extracts keep using the Transparenzregister test client
        automatically; no credential header is accepted on this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extract_id:
            raise ValueError(f"Expected a non-empty value for `extract_id` but received {extract_id!r}")
        return await self._get(
            path_template("/v1/transparenzregister/extracts/{extract_id}", extract_id=extract_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransparenzregisterExtract,
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.create_v1 = to_raw_response_wrapper(
            extract.create_v1,
        )
        self.get_v1 = to_raw_response_wrapper(
            extract.get_v1,
        )


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.create_v1 = async_to_raw_response_wrapper(
            extract.create_v1,
        )
        self.get_v1 = async_to_raw_response_wrapper(
            extract.get_v1,
        )


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.create_v1 = to_streamed_response_wrapper(
            extract.create_v1,
        )
        self.get_v1 = to_streamed_response_wrapper(
            extract.get_v1,
        )


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.create_v1 = async_to_streamed_response_wrapper(
            extract.create_v1,
        )
        self.get_v1 = async_to_streamed_response_wrapper(
            extract.get_v1,
        )
