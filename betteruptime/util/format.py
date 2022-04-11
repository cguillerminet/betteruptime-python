"""
BetterUptime format helpers.
"""
# 3rdp
from yarl import URL


def construct_url(url: URL, path: URL) -> str:
    """Helper to construct URL"""
    return f"{str(url).rstrip('/')}/{str(path).strip('/')}"
