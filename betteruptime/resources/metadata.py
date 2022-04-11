"""
BetterUptime Metadata Resource
"""
from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import MutableResource


class Metadata(MutableResource):
    """
    Represents BetterUptime Metadata Resource.
    """

    def __init__(self, http_client: HTTPClient, name: str = "metadata") -> None:
        super().__init__(http_client, name)
