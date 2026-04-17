# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openregister import Openregister, AsyncOpenregister

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransparenzregister:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_credentials_v1(self, client: Openregister) -> None:
        transparenzregister = client.transparenzregister.set_credentials_v1(
            password="password",
            username="username",
        )
        assert transparenzregister is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_credentials_v1_with_all_params(self, client: Openregister) -> None:
        transparenzregister = client.transparenzregister.set_credentials_v1(
            password="password",
            username="username",
            name="name",
        )
        assert transparenzregister is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_credentials_v1(self, client: Openregister) -> None:
        response = client.transparenzregister.with_raw_response.set_credentials_v1(
            password="password",
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transparenzregister = response.parse()
        assert transparenzregister is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_credentials_v1(self, client: Openregister) -> None:
        with client.transparenzregister.with_streaming_response.set_credentials_v1(
            password="password",
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transparenzregister = response.parse()
            assert transparenzregister is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTransparenzregister:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_credentials_v1(self, async_client: AsyncOpenregister) -> None:
        transparenzregister = await async_client.transparenzregister.set_credentials_v1(
            password="password",
            username="username",
        )
        assert transparenzregister is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_credentials_v1_with_all_params(self, async_client: AsyncOpenregister) -> None:
        transparenzregister = await async_client.transparenzregister.set_credentials_v1(
            password="password",
            username="username",
            name="name",
        )
        assert transparenzregister is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_credentials_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.transparenzregister.with_raw_response.set_credentials_v1(
            password="password",
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transparenzregister = await response.parse()
        assert transparenzregister is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_credentials_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.transparenzregister.with_streaming_response.set_credentials_v1(
            password="password",
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transparenzregister = await response.parse()
            assert transparenzregister is None

        assert cast(Any, response.is_closed) is True
