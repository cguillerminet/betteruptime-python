"""
BetterUptime Client.
"""
from __future__ import annotations

from . import resources
from .api import api_client, http_client
from .api.api_client import Client
from .version import version as __version__

__all__ = ["Client", "api_client", "http_client", "resources", "__version__"]
