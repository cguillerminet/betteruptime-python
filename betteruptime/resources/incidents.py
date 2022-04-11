"""
BetterUptime Incidents Resource
"""
from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import MutableResource


class Incident(MutableResource):
    """
    Represents BetterUptime Incidents Resource
    """

    def __init__(self, http_client: HTTPClient, name: str = "incidents") -> None:
        super().__init__(http_client, name)
