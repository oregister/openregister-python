# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.insolvency_get_details_v1_response import InsolvencyGetDetailsV1Response

__all__ = ["InsolvencyResource", "AsyncInsolvencyResource"]


class InsolvencyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InsolvencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return InsolvencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsolvencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return InsolvencyResourceWithStreamingResponse(self)

    def get_details_v1(
        self,
        insolvency_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsolvencyGetDetailsV1Response:
        """
        Get detailed insolvency proceeding information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not insolvency_id:
            raise ValueError(f"Expected a non-empty value for `insolvency_id` but received {insolvency_id!r}")
        return self._get(
            path_template("/v1/insolvency/{insolvency_id}", insolvency_id=insolvency_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsolvencyGetDetailsV1Response,
        )


class AsyncInsolvencyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInsolvencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsolvencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsolvencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return AsyncInsolvencyResourceWithStreamingResponse(self)

    async def get_details_v1(
        self,
        insolvency_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsolvencyGetDetailsV1Response:
        """
        Get detailed insolvency proceeding information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not insolvency_id:
            raise ValueError(f"Expected a non-empty value for `insolvency_id` but received {insolvency_id!r}")
        return await self._get(
            path_template("/v1/insolvency/{insolvency_id}", insolvency_id=insolvency_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsolvencyGetDetailsV1Response,
        )


class InsolvencyResourceWithRawResponse:
    def __init__(self, insolvency: InsolvencyResource) -> None:
        self._insolvency = insolvency

        self.get_details_v1 = to_raw_response_wrapper(
            insolvency.get_details_v1,
        )


class AsyncInsolvencyResourceWithRawResponse:
    def __init__(self, insolvency: AsyncInsolvencyResource) -> None:
        self._insolvency = insolvency

        self.get_details_v1 = async_to_raw_response_wrapper(
            insolvency.get_details_v1,
        )


class InsolvencyResourceWithStreamingResponse:
    def __init__(self, insolvency: InsolvencyResource) -> None:
        self._insolvency = insolvency

        self.get_details_v1 = to_streamed_response_wrapper(
            insolvency.get_details_v1,
        )


class AsyncInsolvencyResourceWithStreamingResponse:
    def __init__(self, insolvency: AsyncInsolvencyResource) -> None:
        self._insolvency = insolvency

        self.get_details_v1 = async_to_streamed_response_wrapper(
            insolvency.get_details_v1,
        )
