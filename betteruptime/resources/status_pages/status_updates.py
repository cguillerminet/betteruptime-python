"""
BetterUptime Status Page Status Updates Resource
"""
from betteruptime.resources.abstract import AbstractSubResource
from betteruptime.resources.generic import MutableSubResource


class StatusPageStatusUpdates(MutableSubResource):
    """
    Represents BetterUptime Status Page Status Update Resource.
    """

    def __init__(
        self, parent: AbstractSubResource, name: str = "status-updates"
    ) -> None:
        super().__init__(parent, name)
