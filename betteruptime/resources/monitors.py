"""
BetterUptime Monitors Resource
"""
from __future__ import annotations

from typing import Any

from requests import codes

from betteruptime.api.exceptions import ApiError
from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import MutableResource


class Monitor(MutableResource):
    """
    Represents BetterUptime Monitors Resource
    """

    def __init__(self, http_client: HTTPClient, name: str = "monitors") -> None:
        super().__init__(http_client, name)

    def __call__(self, resource_id: str) -> Monitor:
        new_resource = Monitor(http_client=self.http_client)
        new_resource._resource_id = resource_id
        return new_resource

    def get_by_name(self, name: str) -> Any:
        """
        Get a single monitor by name.
        """
        if name is None:
            raise ValueError(
                f"An url is mandatory to call {self.__class__.__name__}.get_by_name()."
                f" You must use {self.__class__.__name__}.get_by_name('Backend')."
            )

        result = self.http_client.get(path=self._get_base_path().update_query(pronounceable_name=name))
        if 200 == result.status_code:
            exists = result.json()
            if len(exists["data"]) == 1:
                return {"data": exists["data"][0]}
            raise ApiError(resource=self.name, status_code=codes["not_found"], reason="Not Found")
        raise ApiError(resource=self.name, status_code=result.status_code, reason=result.reason)

    def get_by_url(self, url: str) -> Any:
        """
        Get a single monitor by url.
        """
        if url is None:
            raise ValueError(
                f"An url is mandatory to call {self.__class__.__name__}.get_by_url()."
                f" You must use {self.__class__.__name__}.get_by_url('http://my.company')."
            )

        result = self.http_client.get(path=self._get_base_path().update_query(url=url))
        if 200 == result.status_code:
            exists = result.json()
            if len(exists["data"]) == 1:
                return {"data": exists["data"][0]}
            raise ApiError(resource=self.name, status_code=codes["not_found"], reason="Not Found")
        raise ApiError(resource=self.name, status_code=result.status_code, reason=result.reason)
