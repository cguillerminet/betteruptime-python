"""
BetterUptime Status Page Reports Resource
"""
from __future__ import annotations

from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.abstract import AbstractResource
from betteruptime.resources.generic import MutableSubResource

from .status_updates import StatusPageStatusUpdates


class StatusPageReport(MutableSubResource):
    """
    Represents BetterUptime Status Page Report Resource.
    """

    _status_updates: StatusPageStatusUpdates

    def __init__(self, http_client: HTTPClient, parent: AbstractResource, name: str = "status-reports") -> None:
        super().__init__(http_client=http_client, parent=parent, name=name)
        self.status_updates = StatusPageStatusUpdates(http_client=http_client, parent=self)

    def __call__(self, resource_id: str) -> StatusPageReport:
        new_resource = StatusPageReport(http_client=self.http_client, parent=self.parent)
        new_resource._resource_id = resource_id
        return new_resource

    @property
    def status_updates(self) -> StatusPageStatusUpdates:
        """
        status_updates property getter.
        """
        return self._status_updates

    @status_updates.setter
    def status_updates(self, status_updates: StatusPageStatusUpdates) -> None:
        """
        status_updates property setter.
        """
        self._status_updates = status_updates
