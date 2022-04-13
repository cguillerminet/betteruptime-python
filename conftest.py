"""
pytest configuration
"""
from typing import Any, Dict

import pytest

import betteruptime


@pytest.fixture()
def client() -> betteruptime.Client:
    """
    BetterUptime Client instance.
    """
    return betteruptime.Client(bearer_token="fake")


def clean_response(response):
    """Remove some info from the response before writing cassettes."""
    remove_headers = {
        "Set-Cookie",
        "set-cookie",
        "Date",
        "x-request-id",
        "x-runtime",
        "alt-svc",
        "NEL",
        "Expect-CT",
        "Report-To",
    }
    if isinstance(response["headers"], dict):
        # Normal client stores headers as dict
        for header_name in remove_headers:
            response["headers"].pop(header_name, None)
    return response


@pytest.fixture(scope="module", autouse=True)
def vcr_config() -> Dict[str, Any]:
    """
    vcr configuration
    """
    return {
        "filter_headers": ["authorization"],
        "before_record_response": clean_response,
    }
