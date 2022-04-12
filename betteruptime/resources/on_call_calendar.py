"""
BetterUptime On-Call Calendar Resource
"""
from __future__ import annotations

from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import ImmutableResource


class OnCallCalendar(ImmutableResource):
    """
    Represents BetterUptime On-Call Calendar Resource
    """

    def __init__(self, http_client: HTTPClient, name: str = "on-calls") -> None:
        super().__init__(http_client, name)

    def __call__(self, resource_id: str) -> OnCallCalendar:
        new_resource = OnCallCalendar(http_client=self.http_client)
        new_resource._resource_id = resource_id
        return new_resource
