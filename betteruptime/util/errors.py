"""
BetterUptime error helpers.
"""
import requests

from betteruptime.typing import JSON


def parse_error_response(response: requests.Response) -> JSON:
    """
    Parse BetterUptime response to extract errors.
    """
    errors = None
    try:
        payload = response.json()
        errors = payload["errors"]
    except requests.exceptions.JSONDecodeError:
        errors = None
    except KeyError:
        errors = None

    return errors
