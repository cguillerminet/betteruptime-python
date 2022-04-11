"""
HTTP Client for BetterUptime API client.
"""
# stdlib
import logging
import platform
from threading import Lock
from typing import Any, Optional

import requests

# betteruptime
from betteruptime import version
from betteruptime.api import (
    _API_HOST,
    _API_MAX_RETRIES,
    _API_PROXIES,
    _API_TIMEOUT,
    _API_VERIFY,
    _API_VERSION,
)
from betteruptime.api.exceptions import ClientError, HTTPError, HttpTimeout, ProxyError
from betteruptime.util.format import construct_url
from yarl import URL

logger: logging.Logger = logging.getLogger("betteruptime.api")


def _get_user_agent_header():

    return (
        f"betteruptimepy/{version.__version__} (python {platform.python_version()};"
        f" os {platform.system().lower()}; arch {platform.machine().lower()})"
    )


def _remove_context(exc):
    """Python3: remove context from chained exceptions to prevent leaking API keys in tracebacks."""
    exc.__cause__ = None
    return exc


class HTTPClient:
    """
    HTTP client based on 3rd party `requests` module, using a single session.
    This allows us to keep the session alive to spare some execution time.
    """

    _bearer_token: Optional[str] = None
    _headers: dict = {
        "Accept": "application/json",
        "User-Agent": _get_user_agent_header(),
    }
    _session: Optional[requests.Session] = None
    _session_lock: Lock = Lock()

    def __init__(
        self,
        api_url: str = _API_HOST,
        api_version: str = _API_VERSION,
        bearer_token: Optional[str] = None,
    ) -> None:
        self.base_url: URL = URL(api_url.strip("/")) / "api" / api_version.strip("/")
        self._bearer_token = bearer_token
        self._headers.update({"Authorization": f"Bearer {self._bearer_token}"})

    @classmethod
    def request(
        cls,
        method: str,
        url: str,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        json: Any = None,
        timeout: float = _API_TIMEOUT,
        allow_redirects: bool = True,
        proxies: Optional[dict] = _API_PROXIES,
        verify: bool = _API_VERIFY,
        max_retries: int = _API_MAX_RETRIES,
    ) -> requests.Response:
        """
        Sends a request.
        Returns :class:`Response <Response>` object.

        :param method: method for the request.
        :param url: URL for the request.
        :param params: (optional) Dictionary or bytes to be sent in the query
            string for the :class:`Request`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the
            :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the
            :class:`Request`.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol or protocol and
            hostname to the URL of the proxy.
        :param verify: (optional) boolean,  controls whether we verify
            the server's TLS certificate. Defaults to ``True``. When set to
            ``False``, requests will accept any TLS certificate presented by
            the server, and will ignore hostname mismatches and/or expired
            certificates, which will make your application vulnerable to
            man-in-the-middle (MitM) attacks. Setting verify to ``False``
            may be useful during local development or testing.
        :rtype: requests.Response
        """
        try:
            with cls._session_lock:
                if cls._session is None:
                    cls._session = requests.Session()
                    http_adapter = requests.adapters.HTTPAdapter(
                        max_retries=max_retries
                    )
                    cls._session.mount("https://", http_adapter)
                    cls._session.headers.update(cls._headers)

            result = cls._session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json,
                timeout=timeout,
                allow_redirects=allow_redirects,
                proxies=proxies,
                verify=verify,
            )

            result.raise_for_status()
        except requests.exceptions.ProxyError as exc:
            raise _remove_context(ProxyError(method, url, exc)) from exc
        except requests.ConnectionError as exc:
            raise _remove_context(ClientError(method, url, exc)) from exc
        except requests.exceptions.Timeout as exc:
            raise _remove_context(HttpTimeout(method, url, timeout)) from exc
        except requests.exceptions.HTTPError as exc:
            if exc.response.status_code in (400, 401, 403, 404, 409, 422, 429):
                # This gets caught afterwards and raises an ApiError exception
                pass
            else:
                raise _remove_context(
                    HTTPError(exc.response.status_code, result.reason)
                ) from exc
        except TypeError as exc:
            raise TypeError(
                "Your installed version of `requests` library seems not compatible with"
                "BetterUptime's usage. We recommend upgrading it ('pip install -U requests')."
            ) from exc

        return result

    def get(self, path: URL, **kwargs) -> requests.Response:
        r"""Sends a GET request. Returns :class:`Response` object.

        :param path: PATH for the request.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        kwargs.setdefault("allow_redirects", True)
        return self.request("GET", construct_url(self.base_url, path), **kwargs)

    def options(self, path: URL, **kwargs) -> requests.Response:
        r"""Sends a OPTIONS request. Returns :class:`Response` object.

        :param path: UPATHRL for the request.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        kwargs.setdefault("allow_redirects", True)
        return self.request("OPTIONS", construct_url(self.base_url, path), **kwargs)

    def head(self, path: URL, **kwargs) -> requests.Response:
        r"""Sends a HEAD request. Returns :class:`Response` object.

        :param path: PATH for the request.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        kwargs.setdefault("allow_redirects", False)
        return self.request("HEAD", construct_url(self.base_url, path), **kwargs)

    def post(self, path: URL, json: Any = None, **kwargs) -> requests.Response:
        r"""Sends a POST request. Returns :class:`Response` object.

        :param path: PATH for the request.
        :param json: (optional) json to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        return self.request(
            "POST", construct_url(self.base_url, path), json=json, **kwargs
        )

    def put(self, path: URL, json: Any = None, **kwargs) -> requests.Response:
        r"""Sends a PUT request. Returns :class:`Response` object.

        :param path: PATH for the request.
        :param json: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        return self.request(
            "PUT", construct_url(self.base_url, path), json=json, **kwargs
        )

    def patch(self, path: URL, json: Any = None, **kwargs) -> requests.Response:
        r"""Sends a PATCH request. Returns :class:`Response` object.

        :param path: PATH for the request.
        :param json: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        return self.request(
            "PATCH", construct_url(self.base_url, path), json=json, **kwargs
        )

    def delete(self, path: URL, **kwargs) -> requests.Response:
        r"""Sends a DELETE request. Returns :class:`Response` object.

        :param path: PATH for the request.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        return self.request("DELETE", construct_url(self.base_url, path), **kwargs)
