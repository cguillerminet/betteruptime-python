"""
API & HTTP Clients exceptions.
"""
from betteruptime.typing import JSON


class BetterUptimeException(Exception):
    """
    Base class for BetterUptime API exceptions.  Use this for patterns like the following:
        try:
            # do something with the BetterUptime API
        except betteruptime.api.exceptions.BetterUptimeException:
            # handle any BetterUptime-specific exceptions
    """


class ProxyError(BetterUptimeException):
    """
    HTTP connection to the configured proxy server failed.
    """

    def __init__(self, method: str, url: str, exception: Exception):
        message = (
            f"Could not request {method} {url}: Unable to connect to proxy. "
            "Please check the proxy configuration and try again."
        )
        super().__init__(message)


class ClientError(BetterUptimeException):
    """
    HTTP connection to BetterUptime endpoint is not possible.
    """

    def __init__(self, method: str, url: str, exception: Exception):
        message = (
            f"Could not request {method} {url}: {exception}. "
            "Please check the network connection or try again later. "
        )
        super().__init__(message)


class HttpTimeout(BetterUptimeException):
    """
    HTTP connection timeout.
    """

    def __init__(self, method: str, url: str, timeout: float):
        message = (
            f"{method} {url} timed out after {timeout}. "
            "Please try again later. "
            "If the problem persists, please contact support@BetterUptimehq.com"
        )
        super().__init__(message)


class HttpBackoff(BetterUptimeException):
    """
    Backing off after too many timeouts.
    """

    def __init__(self, backoff_period: float):
        message = f"Too many timeouts. Won't try again for {backoff_period} seconds. "
        super().__init__(message)


class HTTPError(BetterUptimeException):
    """
    BetterUptime returned a HTTP error.
    """

    def __init__(self, status_code: int = 400, reason: str = ""):
        reason = f" - {reason}" if reason else ""
        message = f"BetterUptime returned a bad HTTP response code: {status_code}{reason}. " "Please try again later. "

        super().__init__(message)


class ApiError(BetterUptimeException):
    """
    BetterUptime returned an API error (known HTTPError).
    Matches the following status codes: 400, 401, 403, 404, 409, 422, 429.
    """

    def __init__(
        self,
        resource: str,
        errors: JSON,
        status_code: int = 400,
        reason: str = "",
        message: str = "",
    ):
        reason = f" - {reason}" if reason else ""
        message = message if message else ""
        message = (
            f"BetterUptime returned the following HTTP response code: "
            f"{status_code}{reason} "
            f"while querying '{resource}' resource."
            f"{message}"
        )

        super().__init__(message)
        self.resource = resource
        self.status_code = status_code
        self.reason = reason
        self.message = message
        self.errors = errors
