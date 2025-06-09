# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from openregister import Openregister, AsyncOpenregister
from openregister._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocument:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Openregister, respx_mock: MockRouter) -> None:
        respx_mock.get("/v0/document/document_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        document = client.document.retrieve(
            "document_id",
        )
        assert document.is_closed
        assert document.json() == {"foo": "bar"}
        assert cast(Any, document.is_closed) is True
        assert isinstance(document, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Openregister, respx_mock: MockRouter) -> None:
        respx_mock.get("/v0/document/document_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        document = client.document.with_raw_response.retrieve(
            "document_id",
        )

        assert document.is_closed is True
        assert document.http_request.headers.get("X-Stainless-Lang") == "python"
        assert document.json() == {"foo": "bar"}
        assert isinstance(document, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Openregister, respx_mock: MockRouter) -> None:
        respx_mock.get("/v0/document/document_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.document.with_streaming_response.retrieve(
            "document_id",
        ) as document:
            assert not document.is_closed
            assert document.http_request.headers.get("X-Stainless-Lang") == "python"

            assert document.json() == {"foo": "bar"}
            assert cast(Any, document.is_closed) is True
            assert isinstance(document, StreamedBinaryAPIResponse)

        assert cast(Any, document.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.document.with_raw_response.retrieve(
                "",
            )


class TestAsyncDocument:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncOpenregister, respx_mock: MockRouter) -> None:
        respx_mock.get("/v0/document/document_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        document = await async_client.document.retrieve(
            "document_id",
        )
        assert document.is_closed
        assert await document.json() == {"foo": "bar"}
        assert cast(Any, document.is_closed) is True
        assert isinstance(document, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncOpenregister, respx_mock: MockRouter) -> None:
        respx_mock.get("/v0/document/document_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        document = await async_client.document.with_raw_response.retrieve(
            "document_id",
        )

        assert document.is_closed is True
        assert document.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await document.json() == {"foo": "bar"}
        assert isinstance(document, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenregister, respx_mock: MockRouter) -> None:
        respx_mock.get("/v0/document/document_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.document.with_streaming_response.retrieve(
            "document_id",
        ) as document:
            assert not document.is_closed
            assert document.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await document.json() == {"foo": "bar"}
            assert cast(Any, document.is_closed) is True
            assert isinstance(document, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, document.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.document.with_raw_response.retrieve(
                "",
            )
