"""
BetterUptime Client.
"""
from . import resources, version
from .api import api_client, http_client
from .api.api_client import Client

__all__ = ["Client", "api_client", "http_client", "resources", "version"]
