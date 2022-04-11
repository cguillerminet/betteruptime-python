"""
BetterUptime On-Call Calendar Resource
"""
from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import ImmutableResource


class OnCallCalendar(ImmutableResource):
    """
    Represents BetterUptime On-Call Calendar Resource
    """

    def __init__(self, http_client: HTTPClient, name: str = "on-calls") -> None:
        super().__init__(http_client, name)
