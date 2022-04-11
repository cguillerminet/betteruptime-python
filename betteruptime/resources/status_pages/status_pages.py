"""
BetterUptime Status Pages Resource
"""
from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.generic import MutableResource

from .reports import StatusPageReport
from .resources import StatusPageResource
from .sections import StatusPageSection


class StatusPage(MutableResource):
    """
    Represents BetterUptime Status Page Resource.
    """

    _reports: StatusPageReport
    _resources: StatusPageResource
    _sections: StatusPageSection

    def __init__(self, http_client: HTTPClient, name: str = "status-pages") -> None:
        super().__init__(http_client, name)
        self.reports = StatusPageReport(self)
        self.resources = StatusPageResource(self)
        self.sections = StatusPageSection(self)

    @property
    def reports(self) -> StatusPageReport:
        """
        reports property getter.
        """
        return self._reports

    @reports.setter
    def reports(self, reports: StatusPageReport) -> None:
        """
        reports property setter.
        """
        self._reports = reports

    @property
    def resources(self) -> StatusPageResource:
        """
        resources property getter.
        """
        return self._resources

    @resources.setter
    def resources(self, resources: StatusPageResource) -> None:
        """
        resources property setter.
        """
        self._resources = resources

    @property
    def sections(self) -> StatusPageSection:
        """
        sections property getter.
        """
        return self._sections

    @sections.setter
    def sections(self, sections: StatusPageSection) -> None:
        """
        sections property setter.
        """
        self._sections = sections
