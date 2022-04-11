"""
BetterUptime Heartbeats Resource
"""
from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import MutableResource


class Heartbeat(MutableResource):
    """
    Represents BetterUptime Heartbeats Resource
    """

    def __init__(self, http_client: HTTPClient, name: str = "heartbeats") -> None:
        super().__init__(http_client, name)
