"""
BetterUptime Status Page Reports Resource
"""
from betteruptime.resources.abstract import AbstractResource
from betteruptime.resources.generic import MutableSubResource

from .status_updates import StatusPageStatusUpdates


class StatusPageReport(MutableSubResource):
    """
    Represents BetterUptime Status Page Report Resource.
    """

    _status_updates: StatusPageStatusUpdates

    def __init__(self, parent: AbstractResource, name: str = "status-reports") -> None:
        super().__init__(parent, name)
        self.status_updates = StatusPageStatusUpdates(self)

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
