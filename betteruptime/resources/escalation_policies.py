"""
BetterUptime Monitors Resource
"""
from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import ImmutableResource


class EscalationPolicy(ImmutableResource):
    """
    Represents BetterUptime Escalation Policies Resource.
    """

    def __init__(self, http_client: HTTPClient, name: str = "policies") -> None:
        super().__init__(http_client, name)
