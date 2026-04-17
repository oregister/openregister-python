# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from openregister import Openregister, AsyncOpenregister
from openregister.types.transparenzregister import TransparenzregisterExtract

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_v1(self, client: Openregister) -> None:
        extract = client.transparenzregister.extract.create_v1()
        assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_v1_with_all_params(self, client: Openregister) -> None:
        extract = client.transparenzregister.extract.create_v1(
            company_id="company_id",
            x_credential_name="X-Credential-Name",
        )
        assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_v1(self, client: Openregister) -> None:
        response = client.transparenzregister.extract.with_raw_response.create_v1()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_v1(self, client: Openregister) -> None:
        with client.transparenzregister.extract.with_streaming_response.create_v1() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_v1(self, client: Openregister) -> None:
        extract = client.transparenzregister.extract.get_v1(
            "extract_id",
        )
        assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_v1(self, client: Openregister) -> None:
        response = client.transparenzregister.extract.with_raw_response.get_v1(
            "extract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_v1(self, client: Openregister) -> None:
        with client.transparenzregister.extract.with_streaming_response.get_v1(
            "extract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_v1(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extract_id` but received ''"):
            client.transparenzregister.extract.with_raw_response.get_v1(
                "",
            )


class TestAsyncExtract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_v1(self, async_client: AsyncOpenregister) -> None:
        extract = await async_client.transparenzregister.extract.create_v1()
        assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_v1_with_all_params(self, async_client: AsyncOpenregister) -> None:
        extract = await async_client.transparenzregister.extract.create_v1(
            company_id="company_id",
            x_credential_name="X-Credential-Name",
        )
        assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.transparenzregister.extract.with_raw_response.create_v1()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.transparenzregister.extract.with_streaming_response.create_v1() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_v1(self, async_client: AsyncOpenregister) -> None:
        extract = await async_client.transparenzregister.extract.get_v1(
            "extract_id",
        )
        assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.transparenzregister.extract.with_raw_response.get_v1(
            "extract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.transparenzregister.extract.with_streaming_response.get_v1(
            "extract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(TransparenzregisterExtract, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_v1(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extract_id` but received ''"):
            await async_client.transparenzregister.extract.with_raw_response.get_v1(
                "",
            )
