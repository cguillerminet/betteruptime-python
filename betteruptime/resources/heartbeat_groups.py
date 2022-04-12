"""
BetterUptime Heartbeat Groups Resource
"""
from __future__ import annotations

# from betteruptime.api.exceptions import ApiError
from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import MutableResource

# from typing import Any, Dict


class HeartbeatGroup(MutableResource):
    """
    Represents BetterUptime Heartbeat Groups Resource
    """

    def __init__(self, http_client: HTTPClient, name: str = "heartbeat-groups") -> None:
        super().__init__(http_client, name)

    def __call__(self, resource_id: str) -> HeartbeatGroup:
        new_resource = HeartbeatGroup(http_client=self.http_client)
        new_resource._resource_id = resource_id
        return new_resource

    # @property
    # def heartbeats(self) -> Dict[str, Any]:
    #     """
    #     List heartbeats in this group.
    #     """
    #     if self.resource_id is None:
    #         raise ValueError(
    #             f"A resource_id is mandatory to call {self.__class__.__name__}.heartbeats."
    #             f" You must use {self.__class__.__name__}('12345').heartbeats."
    #         )

    #     result = self.http_client.get(
    #         path=self._get_base_path() / self.resource_id / "heartbeats"
    #     )
    #     if 200 == result.status_code:
    #         return result.json()
    #     raise ApiError(
    #         resource=self.name, status_code=result.status_code, reason=result.reason
    #     )
