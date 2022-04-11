"""
BetterUptime Status Page Sections Resource
"""
from betteruptime.resources.abstract import AbstractResource
from betteruptime.resources.generic import MutableSubResource


class StatusPageSection(MutableSubResource):
    """
    Represents BetterUptime Status Page Section Resource.
    """

    def __init__(self, parent: AbstractResource, name: str = "sections") -> None:
        super().__init__(parent, name)
