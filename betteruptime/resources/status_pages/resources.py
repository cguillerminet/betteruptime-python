"""
BetterUptime Status Page Resources Resource
"""
from betteruptime.resources.abstract import AbstractResource
from betteruptime.resources.generic import MutableSubResource


class StatusPageResource(MutableSubResource):
    """
    Represents BetterUptime Status Page Resources Resource.
    """

    def __init__(self, parent: AbstractResource, name: str = "resources") -> None:
        super().__init__(parent, name)
