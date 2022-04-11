"""
BetterUptime Monitors Resource
"""
from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import MutableResource


class Monitor(MutableResource):
    """
    Represents BetterUptime Monitors Resource
    """

    def __init__(self, http_client: HTTPClient, name: str = "monitors") -> None:
        super().__init__(http_client, name)
