"""
BetterUptime API
"""
from typing import Dict, Optional

# API settings
_API_HOST: str = "https://betteruptime.com"
_API_MAX_RETRIES: int = 3
_API_PROXIES: Optional[Dict[str, str]] = None
_API_TIMEOUT: float = 30.0
_API_VERIFY: bool = True
_API_VERSION: str = "v2"
