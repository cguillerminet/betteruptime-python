"""
BetterUptime API Client
"""
from typing import Dict, Union

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

BetterUptimeResource = Union[
    EscalationPolicy,
    Heartbeat,
    HeartbeatGroup,
    Incident,
    Metadata,
    Monitor,
    MonitorGroup,
    OnCallCalendar,
    StatusPage,
]


class Client:
    """
    BetterUptime API Client.
    """

    _http_client: HTTPClient
    _resources: Dict[
        str,
        BetterUptimeResource,
    ] = {}

    _heartbeat_groups: HeartbeatGroup
    _heartbeats: Heartbeat
    _incidents: Incident
    _metadata: Metadata
    _monitor_groups: MonitorGroup
    _monitors: Monitor
    _on_calls: OnCallCalendar
    _policies: EscalationPolicy
    _status_pages: StatusPage

    def __init__(self, bearer_token: str) -> None:
        self._http_client = HTTPClient(bearer_token=bearer_token)
        self._heartbeat_groups = HeartbeatGroup(self._http_client)
        self._heartbeats = Heartbeat(self._http_client)
        self._incidents = Incident(self._http_client)
        self._metadata = Metadata(self._http_client)
        self._monitor_groups = MonitorGroup(self._http_client)
        self._monitors = Monitor(self._http_client)
        self._on_calls = OnCallCalendar(self._http_client)
        self._policies = EscalationPolicy(self._http_client)
        self._status_pages = StatusPage(self._http_client)

    @property
    def heartbeat_groups(self) -> HeartbeatGroup:
        r"""BetterUptime heartbeat groupss resource. Returns :class:`HeartbeatGroup` object.

        :rtype: betteruptime.resources.heartbeat_groups.HeartbeatGroup
        """
        return self._heartbeat_groups

    @property
    def heartbeats(self) -> Heartbeat:
        r"""BetterUptime heartbeats resource. Returns :class:`Heartbeat` object.

        :rtype: betteruptime.resources.heartbeats.Heartbeat
        """
        return self._heartbeats

    @property
    def incidents(self) -> Incident:
        r"""BetterUptime incidents resource. Returns :class:`Incident` object.

        :rtype: betteruptime.resources.incidents.Incident
        """
        return self._incidents

    @property
    def metadata(self) -> Metadata:
        r"""BetterUptime metadata resource. Returns :class:`Metadata` object.

        :rtype: betteruptime.resources.metadata.Metadata
        """
        return self._metadata

    @property
    def monitor_groups(self) -> MonitorGroup:
        r"""BetterUptime monitor groups resource. Returns :class:`MonitorGroup` object.

        :rtype: betteruptime.resources.monitor_groups.MonitorGroup
        """
        return self._monitor_groups

    @property
    def monitors(self) -> Monitor:
        r"""BetterUptime monitors resource. Returns :class:`Monitor` object.

        :rtype: betteruptime.resources.monitor.Monitor
        """
        return self._monitors

    @property
    def on_calls(self) -> OnCallCalendar:
        r"""BetterUptime on-call calendar resource. Returns :class:`OnCallCalendar` object.

        :rtype: betteruptime.resources.on_call_calendar.OnCallCalendar
        """
        return self._on_calls

    @property
    def policies(self) -> EscalationPolicy:
        r"""BetterUptime escalation policies resource. Returns :class:`EscalationPolicy` object.

        :rtype: betteruptime.resources.escalation_policies.EscalationPolicy
        """
        return self._policies

    @property
    def status_pages(self) -> StatusPage:
        r"""BetterUptime status pages resource. Returns :class:`StatusPage` object.

        :rtype: betteruptime.resources.status_pages.StatusPage
        """
        return self._status_pages
