"""
BetterUptime Incidents Resource
"""
from __future__ import annotations

from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import MutableResource


class Incident(MutableResource):
    """
    Represents BetterUptime Incidents Resource
    """

    def __init__(self, http_client: HTTPClient, name: str = "incidents") -> None:
        super().__init__(http_client, name)

    def __call__(self, resource_id: str) -> Incident:
        new_resource = Incident(http_client=self.http_client)
        new_resource._resource_id = resource_id
        return new_resource
