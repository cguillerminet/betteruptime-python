"""
BetterUptime Monitors Resource
"""
from __future__ import annotations

from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import ImmutableResource


class EscalationPolicy(ImmutableResource):
    """
    Represents BetterUptime Escalation Policies Resource.
    """

    def __init__(self, http_client: HTTPClient, name: str = "policies") -> None:
        super().__init__(http_client, name)

    def __call__(self, resource_id: str) -> EscalationPolicy:
        new_resource = EscalationPolicy(http_client=self.http_client)
        new_resource._resource_id = resource_id
        return new_resource
