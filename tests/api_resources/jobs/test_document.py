# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from openregister import Openregister, AsyncOpenregister
from openregister.types.jobs import DocumentCreateResponse, DocumentRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocument:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Openregister) -> None:
        document = client.jobs.document.create(
            company_id="company_id",
            document_category="current_printout",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Openregister) -> None:
        response = client.jobs.document.with_raw_response.create(
            company_id="company_id",
            document_category="current_printout",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Openregister) -> None:
        with client.jobs.document.with_streaming_response.create(
            company_id="company_id",
            document_category="current_printout",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Openregister) -> None:
        document = client.jobs.document.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Openregister) -> None:
        response = client.jobs.document.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Openregister) -> None:
        with client.jobs.document.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.jobs.document.with_raw_response.retrieve(
                "",
            )


class TestAsyncDocument:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncOpenregister) -> None:
        document = await async_client.jobs.document.create(
            company_id="company_id",
            document_category="current_printout",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.jobs.document.with_raw_response.create(
            company_id="company_id",
            document_category="current_printout",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenregister) -> None:
        async with async_client.jobs.document.with_streaming_response.create(
            company_id="company_id",
            document_category="current_printout",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenregister) -> None:
        document = await async_client.jobs.document.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.jobs.document.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenregister) -> None:
        async with async_client.jobs.document.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.jobs.document.with_raw_response.retrieve(
                "",
            )
