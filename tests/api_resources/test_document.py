# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from openregister import Openregister, AsyncOpenregister
from openregister.types import (
    DocumentGetCachedV1Response,
    DocumentGetRealtimeV1Response,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocument:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_cached_v1(self, client: Openregister) -> None:
        document = client.document.get_cached_v1(
            "document_id",
        )
        assert_matches_type(DocumentGetCachedV1Response, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_cached_v1(self, client: Openregister) -> None:
        response = client.document.with_raw_response.get_cached_v1(
            "document_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentGetCachedV1Response, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_cached_v1(self, client: Openregister) -> None:
        with client.document.with_streaming_response.get_cached_v1(
            "document_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentGetCachedV1Response, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_cached_v1(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.document.with_raw_response.get_cached_v1(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_realtime_v1(self, client: Openregister) -> None:
        document = client.document.get_realtime_v1(
            company_id="company_id",
            document_category="current_printout",
        )
        assert_matches_type(DocumentGetRealtimeV1Response, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_realtime_v1(self, client: Openregister) -> None:
        response = client.document.with_raw_response.get_realtime_v1(
            company_id="company_id",
            document_category="current_printout",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentGetRealtimeV1Response, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_realtime_v1(self, client: Openregister) -> None:
        with client.document.with_streaming_response.get_realtime_v1(
            company_id="company_id",
            document_category="current_printout",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentGetRealtimeV1Response, document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocument:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_cached_v1(self, async_client: AsyncOpenregister) -> None:
        document = await async_client.document.get_cached_v1(
            "document_id",
        )
        assert_matches_type(DocumentGetCachedV1Response, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_cached_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.document.with_raw_response.get_cached_v1(
            "document_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentGetCachedV1Response, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_cached_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.document.with_streaming_response.get_cached_v1(
            "document_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentGetCachedV1Response, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_cached_v1(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.document.with_raw_response.get_cached_v1(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_realtime_v1(self, async_client: AsyncOpenregister) -> None:
        document = await async_client.document.get_realtime_v1(
            company_id="company_id",
            document_category="current_printout",
        )
        assert_matches_type(DocumentGetRealtimeV1Response, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_realtime_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.document.with_raw_response.get_realtime_v1(
            company_id="company_id",
            document_category="current_printout",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentGetRealtimeV1Response, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_realtime_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.document.with_streaming_response.get_realtime_v1(
            company_id="company_id",
            document_category="current_printout",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentGetRealtimeV1Response, document, path=["response"])

        assert cast(Any, response.is_closed) is True
