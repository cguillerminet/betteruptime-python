"""
BetterUptime Metadata Resource
"""
from __future__ import annotations

from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import MutableResource


class Metadata(MutableResource):
    """
    Represents BetterUptime Metadata Resource.
    """

    def __init__(self, http_client: HTTPClient, name: str = "metadata") -> None:
        super().__init__(http_client, name)

    def __call__(self, resource_id: str) -> Metadata:
        new_resource = Metadata(http_client=self.http_client)
        new_resource._resource_id = resource_id
        return new_resource
