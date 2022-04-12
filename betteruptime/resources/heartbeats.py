"""
BetterUptime Heartbeats Resource
"""
from __future__ import annotations

from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import MutableResource


class Heartbeat(MutableResource):
    """
    Represents BetterUptime Heartbeats Resource
    """

    def __init__(self, http_client: HTTPClient, name: str = "heartbeats") -> None:
        super().__init__(http_client, name)

    def __call__(self, resource_id: str) -> Heartbeat:
        new_resource = Heartbeat(http_client=self.http_client)
        new_resource._resource_id = resource_id
        return new_resource
