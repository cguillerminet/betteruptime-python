"""
BetterUptime API Client
"""
from betteruptime.api.http_client import HTTPClient
from betteruptime.resources import (
    EscalationPolicy,
    Heartbeat,
    HeartbeatGroup,
    Incident,
    Metadata,
    Monitor,
    MonitorGroup,
    OnCallCalendar,
    StatusPage,
)


class Client:
    """
    BetterUptime API Client.
    """

    _http_client: HTTPClient
    _resources: dict = {}

    def __init__(self, bearer_token: str) -> None:
        self._http_client = HTTPClient(bearer_token=bearer_token)
        self._resources["heartbeat_groups"] = HeartbeatGroup(self._http_client)
        self._resources["heartbeats"] = Heartbeat(self._http_client)
        self._resources["incidents"] = Incident(self._http_client)
        self._resources["metadata"] = Metadata(self._http_client)
        self._resources["monitor_groups"] = MonitorGroup(self._http_client)
        self._resources["monitors"] = Monitor(self._http_client)
        self._resources["on_calls"] = OnCallCalendar(self._http_client)
        self._resources["policies"] = EscalationPolicy(self._http_client)
        self._resources["status_pages"] = StatusPage(self._http_client)

    @property
    def heartbeat_groups(self) -> Heartbeat:
        r"""BetterUptime heartbeat groupss resource. Returns :class:`HeartbeatGroup` object.

        :rtype: betteruptime.resources.heartbeat_groups.HeartbeatGroup
        """
        return self._resources["heartbeat_groups"]

    @property
    def heartbeats(self) -> Heartbeat:
        r"""BetterUptime heartbeats resource. Returns :class:`Heartbeat` object.

        :rtype: betteruptime.resources.heartbeats.Heartbeat
        """
        return self._resources["heartbeats"]

    @property
    def incidents(self) -> Incident:
        r"""BetterUptime incidents resource. Returns :class:`Incident` object.

        :rtype: betteruptime.resources.incidents.Incident
        """
        return self._resources["incidents"]

    @property
    def metadata(self) -> Metadata:
        r"""BetterUptime metadata resource. Returns :class:`Metadata` object.

        :rtype: betteruptime.resources.metadata.Metadata
        """
        return self._resources["metadata"]

    @property
    def monitor_groups(self) -> Monitor:
        r"""BetterUptime monitor groups resource. Returns :class:`MonitorGroup` object.

        :rtype: betteruptime.resources.monitor_groups.MonitorGroup
        """
        return self._resources["monitor_groups"]

    @property
    def monitors(self) -> Monitor:
        r"""BetterUptime monitors resource. Returns :class:`Monitor` object.

        :rtype: betteruptime.resources.monitor.Monitor
        """
        return self._resources["monitors"]

    @property
    def on_calls(self) -> OnCallCalendar:
        r"""BetterUptime on-call calendar resource. Returns :class:`OnCallCalendar` object.

        :rtype: betteruptime.resources.on_call_calendar.OnCallCalendar
        """
        return self._resources["on_calls"]

    @property
    def policies(self) -> EscalationPolicy:
        r"""BetterUptime escalation policies resource. Returns :class:`EscalationPolicy` object.

        :rtype: betteruptime.resources.escalation_policies.EscalationPolicy
        """
        return self._resources["policies"]

    @property
    def status_pages(self) -> StatusPage:
        r"""BetterUptime status pages resource. Returns :class:`StatusPage` object.

        :rtype: betteruptime.resources.status_pages.StatusPage
        """
        return self._resources["status_pages"]
