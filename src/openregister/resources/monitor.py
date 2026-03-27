# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import monitor_create_params
from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.monitor_list_response import MonitorListResponse
from ..types.monitor_create_response import MonitorCreateResponse

__all__ = ["MonitorResource", "AsyncMonitorResource"]


class MonitorResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MonitorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return MonitorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonitorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return MonitorResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        entity_id: str,
        entity_type: Literal["company", "person"],
        preferences: List[
            Literal[
                "basic", "representation", "financials", "documents", "ownership", "holdings", "management_positions"
            ]
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorCreateResponse:
        """
        Create webhook monitor item

        Args:
          entity_id: For `company` this is the register ID (e.g. `DE-HRB-F1103-267645`). For `person`
              this is the person UUID.

          entity_type: Type of the entity to monitor.

          preferences: Preferences for the entity to monitor. Use `WebhookMonitorCompanyPreference`
              values when `entity_type` is `company`, and `WebhookMonitorPersonPreference`
              values when `entity_type` is `person`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/monitor",
            body=maybe_transform(
                {
                    "entity_id": entity_id,
                    "entity_type": entity_type,
                    "preferences": preferences,
                },
                monitor_create_params.MonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorCreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListResponse:
        """List webhook monitor items"""
        return self._get(
            "/v1/monitor",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorListResponse,
        )

    def delete(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete webhook monitor item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/monitor/{entity_id}", entity_id=entity_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMonitorResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMonitorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMonitorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonitorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return AsyncMonitorResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        entity_id: str,
        entity_type: Literal["company", "person"],
        preferences: List[
            Literal[
                "basic", "representation", "financials", "documents", "ownership", "holdings", "management_positions"
            ]
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorCreateResponse:
        """
        Create webhook monitor item

        Args:
          entity_id: For `company` this is the register ID (e.g. `DE-HRB-F1103-267645`). For `person`
              this is the person UUID.

          entity_type: Type of the entity to monitor.

          preferences: Preferences for the entity to monitor. Use `WebhookMonitorCompanyPreference`
              values when `entity_type` is `company`, and `WebhookMonitorPersonPreference`
              values when `entity_type` is `person`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/monitor",
            body=await async_maybe_transform(
                {
                    "entity_id": entity_id,
                    "entity_type": entity_type,
                    "preferences": preferences,
                },
                monitor_create_params.MonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorCreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListResponse:
        """List webhook monitor items"""
        return await self._get(
            "/v1/monitor",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorListResponse,
        )

    async def delete(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete webhook monitor item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/monitor/{entity_id}", entity_id=entity_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MonitorResourceWithRawResponse:
    def __init__(self, monitor: MonitorResource) -> None:
        self._monitor = monitor

        self.create = to_raw_response_wrapper(
            monitor.create,
        )
        self.list = to_raw_response_wrapper(
            monitor.list,
        )
        self.delete = to_raw_response_wrapper(
            monitor.delete,
        )


class AsyncMonitorResourceWithRawResponse:
    def __init__(self, monitor: AsyncMonitorResource) -> None:
        self._monitor = monitor

        self.create = async_to_raw_response_wrapper(
            monitor.create,
        )
        self.list = async_to_raw_response_wrapper(
            monitor.list,
        )
        self.delete = async_to_raw_response_wrapper(
            monitor.delete,
        )


class MonitorResourceWithStreamingResponse:
    def __init__(self, monitor: MonitorResource) -> None:
        self._monitor = monitor

        self.create = to_streamed_response_wrapper(
            monitor.create,
        )
        self.list = to_streamed_response_wrapper(
            monitor.list,
        )
        self.delete = to_streamed_response_wrapper(
            monitor.delete,
        )


class AsyncMonitorResourceWithStreamingResponse:
    def __init__(self, monitor: AsyncMonitorResource) -> None:
        self._monitor = monitor

        self.create = async_to_streamed_response_wrapper(
            monitor.create,
        )
        self.list = async_to_streamed_response_wrapper(
            monitor.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            monitor.delete,
        )
