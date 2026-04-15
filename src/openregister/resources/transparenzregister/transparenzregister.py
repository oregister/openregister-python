# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import transparenzregister_set_credentials_v1_params
from .request import (
    RequestResource,
    AsyncRequestResource,
    RequestResourceWithRawResponse,
    AsyncRequestResourceWithRawResponse,
    RequestResourceWithStreamingResponse,
    AsyncRequestResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["TransparenzregisterResource", "AsyncTransparenzregisterResource"]


class TransparenzregisterResource(SyncAPIResource):
    @cached_property
    def request(self) -> RequestResource:
        return RequestResource(self._client)

    @cached_property
    def with_raw_response(self) -> TransparenzregisterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return TransparenzregisterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransparenzregisterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return TransparenzregisterResourceWithStreamingResponse(self)

    def set_credentials_v1(
        self,
        *,
        password: str,
        username: str,
        credential_label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Store username and password credentials for accessing the Transparenzregister
        API. These credentials will be used for subsequent requests to retrieve company
        documents.

        Args:
          password: Password for Transparenzregister API access.

          username:
              Username for Transparenzregister API access. Example:
              "testnutzer-eis@transparenzregister.de"

          credential_label: Label to identify this set of credentials. Allows storing multiple
              Transparenzregister credentials per user (e.g., for different accounts or
              clients). Defaults to 'default' if not provided. Example: "client_a"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/transparenzregister/credentials",
            body=maybe_transform(
                {
                    "password": password,
                    "username": username,
                    "credential_label": credential_label,
                },
                transparenzregister_set_credentials_v1_params.TransparenzregisterSetCredentialsV1Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTransparenzregisterResource(AsyncAPIResource):
    @cached_property
    def request(self) -> AsyncRequestResource:
        return AsyncRequestResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTransparenzregisterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransparenzregisterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransparenzregisterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return AsyncTransparenzregisterResourceWithStreamingResponse(self)

    async def set_credentials_v1(
        self,
        *,
        password: str,
        username: str,
        credential_label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Store username and password credentials for accessing the Transparenzregister
        API. These credentials will be used for subsequent requests to retrieve company
        documents.

        Args:
          password: Password for Transparenzregister API access.

          username:
              Username for Transparenzregister API access. Example:
              "testnutzer-eis@transparenzregister.de"

          credential_label: Label to identify this set of credentials. Allows storing multiple
              Transparenzregister credentials per user (e.g., for different accounts or
              clients). Defaults to 'default' if not provided. Example: "client_a"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/transparenzregister/credentials",
            body=await async_maybe_transform(
                {
                    "password": password,
                    "username": username,
                    "credential_label": credential_label,
                },
                transparenzregister_set_credentials_v1_params.TransparenzregisterSetCredentialsV1Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TransparenzregisterResourceWithRawResponse:
    def __init__(self, transparenzregister: TransparenzregisterResource) -> None:
        self._transparenzregister = transparenzregister

        self.set_credentials_v1 = to_raw_response_wrapper(
            transparenzregister.set_credentials_v1,
        )

    @cached_property
    def request(self) -> RequestResourceWithRawResponse:
        return RequestResourceWithRawResponse(self._transparenzregister.request)


class AsyncTransparenzregisterResourceWithRawResponse:
    def __init__(self, transparenzregister: AsyncTransparenzregisterResource) -> None:
        self._transparenzregister = transparenzregister

        self.set_credentials_v1 = async_to_raw_response_wrapper(
            transparenzregister.set_credentials_v1,
        )

    @cached_property
    def request(self) -> AsyncRequestResourceWithRawResponse:
        return AsyncRequestResourceWithRawResponse(self._transparenzregister.request)


class TransparenzregisterResourceWithStreamingResponse:
    def __init__(self, transparenzregister: TransparenzregisterResource) -> None:
        self._transparenzregister = transparenzregister

        self.set_credentials_v1 = to_streamed_response_wrapper(
            transparenzregister.set_credentials_v1,
        )

    @cached_property
    def request(self) -> RequestResourceWithStreamingResponse:
        return RequestResourceWithStreamingResponse(self._transparenzregister.request)


class AsyncTransparenzregisterResourceWithStreamingResponse:
    def __init__(self, transparenzregister: AsyncTransparenzregisterResource) -> None:
        self._transparenzregister = transparenzregister

        self.set_credentials_v1 = async_to_streamed_response_wrapper(
            transparenzregister.set_credentials_v1,
        )

    @cached_property
    def request(self) -> AsyncRequestResourceWithStreamingResponse:
        return AsyncRequestResourceWithStreamingResponse(self._transparenzregister.request)
