"""
BetterUptime Status Page Resources Resource
"""
from __future__ import annotations

from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.abstract import AbstractResource
from betteruptime.resources.generic import MutableSubResource


class StatusPageResource(MutableSubResource):
    """
    Represents BetterUptime Status Page Resources Resource.
    """

    def __init__(self, http_client: HTTPClient, parent: AbstractResource, name: str = "resources") -> None:
        super().__init__(http_client=http_client, parent=parent, name=name)

    def __call__(self, resource_id: str) -> StatusPageResource:
        new_resource = StatusPageResource(http_client=self.http_client, parent=self.parent)
        new_resource._resource_id = resource_id
        return new_resource
