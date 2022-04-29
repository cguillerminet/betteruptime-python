"""
BetterUptime Monitor Groups Resource
"""
from __future__ import annotations

from typing import Generator

from yarl import URL

from betteruptime.api.exceptions import ApiError
from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import MutableResource
from betteruptime.typing import JSON
from betteruptime.util.errors import parse_error_response


class MonitorGroup(MutableResource):
    """
    Represents BetterUptime Monitor Groups Resource
    """

    def __init__(self, http_client: HTTPClient, name: str = "monitor-groups") -> None:
        super().__init__(http_client, name)

    def __call__(self, resource_id: str) -> MonitorGroup:
        new_resource = MonitorGroup(http_client=self.http_client)
        new_resource._resource_id = resource_id
        return new_resource

    def monitors(self, page: int = 1) -> JSON:
        """
        List paginated monitors in this group.
        """
        if self.resource_id is None:
            raise ValueError(
                f"A resource_id is mandatory to call {self.__class__.__name__}.monitors."
                f" You must use {self.__class__.__name__}('12345').monitors."
            )

        result = self.http_client.get(
            path=(self._get_base_path() / self.resource_id / "monitors").update_query(page=page)
        )
        if 200 == result.status_code:
            payload: JSON = result.json()
            return payload

        raise ApiError(
            resource=self.name,
            status_code=result.status_code,
            reason=result.reason,
            errors=parse_error_response(result),
        )

    def monitors_iter(self, page: int = 1) -> Generator[JSON, None, None]:
        """
        List all monitor items by itering over all pages.
        """
        while True:
            result = self.monitors(page=page)
            assert isinstance(result, dict)
            for monitor in result["data"]:
                yield monitor
            if result["pagination"]["next"]:
                next_url: URL = URL(result["pagination"]["next"])
                page = int(next_url.query["page"])
            else:
                break
