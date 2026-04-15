# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from openregister import Openregister, AsyncOpenregister
from openregister.types.transparenzregister import (
    RequestGetV1Response,
    RequestCreateV1Response,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRequest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_v1(self, client: Openregister) -> None:
        request = client.transparenzregister.request.create_v1()
        assert_matches_type(RequestCreateV1Response, request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_v1_with_all_params(self, client: Openregister) -> None:
        request = client.transparenzregister.request.create_v1(
            company_id="company_id",
            x_credential_label="X-Credential-Label",
        )
        assert_matches_type(RequestCreateV1Response, request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_v1(self, client: Openregister) -> None:
        response = client.transparenzregister.request.with_raw_response.create_v1()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(RequestCreateV1Response, request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_v1(self, client: Openregister) -> None:
        with client.transparenzregister.request.with_streaming_response.create_v1() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(RequestCreateV1Response, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_v1(self, client: Openregister) -> None:
        request = client.transparenzregister.request.get_v1(
            "request_id",
        )
        assert_matches_type(RequestGetV1Response, request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_v1(self, client: Openregister) -> None:
        response = client.transparenzregister.request.with_raw_response.get_v1(
            "request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(RequestGetV1Response, request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_v1(self, client: Openregister) -> None:
        with client.transparenzregister.request.with_streaming_response.get_v1(
            "request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(RequestGetV1Response, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_v1(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.transparenzregister.request.with_raw_response.get_v1(
                "",
            )


class TestAsyncRequest:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_v1(self, async_client: AsyncOpenregister) -> None:
        request = await async_client.transparenzregister.request.create_v1()
        assert_matches_type(RequestCreateV1Response, request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_v1_with_all_params(self, async_client: AsyncOpenregister) -> None:
        request = await async_client.transparenzregister.request.create_v1(
            company_id="company_id",
            x_credential_label="X-Credential-Label",
        )
        assert_matches_type(RequestCreateV1Response, request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.transparenzregister.request.with_raw_response.create_v1()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(RequestCreateV1Response, request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.transparenzregister.request.with_streaming_response.create_v1() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(RequestCreateV1Response, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_v1(self, async_client: AsyncOpenregister) -> None:
        request = await async_client.transparenzregister.request.get_v1(
            "request_id",
        )
        assert_matches_type(RequestGetV1Response, request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.transparenzregister.request.with_raw_response.get_v1(
            "request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(RequestGetV1Response, request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.transparenzregister.request.with_streaming_response.get_v1(
            "request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(RequestGetV1Response, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_v1(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.transparenzregister.request.with_raw_response.get_v1(
                "",
            )
