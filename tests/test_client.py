"""
Client tests
"""
import types

import pytest
from pytest_mock import MockerFixture

import betteruptime
from betteruptime.api.exceptions import ApiError

pytestmark = pytest.mark.vcr


class TestClient:
    """
    BetterUptime API Client tests
    """

    def test_bearer_token_set(self, client: betteruptime.Client) -> None:
        """
        Test if Bearer token is set
        """
        assert "Authorization" in client.status_pages.http_client._headers
        assert client.status_pages.http_client._headers["Authorization"] == "Bearer fake"

    def test_401(self, client: betteruptime.Client) -> None:
        """
        Test that an invalid token raises an ApiError
        """
        with pytest.raises(ApiError) as excinfo:
            client.status_pages.list()
        assert 401 == excinfo.value.status_code

    def test_list_heartbeat_groups(self, client: betteruptime.Client) -> None:
        """
        Test list heartbeat groups.
        """
        heartbeat_groups = client.heartbeat_groups.list()
        assert isinstance(heartbeat_groups, dict)
        assert "data" in heartbeat_groups
        assert isinstance(heartbeat_groups["data"], list)
        assert len(heartbeat_groups["data"]) == 0

    def test_list_heartbeats(self, client: betteruptime.Client) -> None:
        """
        Test list heartbeats.
        """
        heartbeats = client.heartbeats.list()
        assert isinstance(heartbeats, dict)
        assert "data" in heartbeats
        assert isinstance(heartbeats["data"], list)
        assert len(heartbeats["data"]) == 0

    def test_list_incidents(self, client: betteruptime.Client) -> None:
        """
        Test list incidents.
        """
        incidents = client.incidents.list()
        assert isinstance(incidents, dict)
        assert "data" in incidents
        assert isinstance(incidents["data"], list)
        assert len(incidents["data"]) == 0

    def test_list_metadata(self, client: betteruptime.Client) -> None:
        """
        Test list metadata.
        """
        metadata = client.metadata.list()
        assert isinstance(metadata, dict)
        assert "data" in metadata
        assert isinstance(metadata["data"], list)
        assert len(metadata["data"]) == 0

    def test_list_monitors(self, client: betteruptime.Client) -> None:
        """
        Test list monitors.
        """
        monitors = client.monitors.list()
        assert isinstance(monitors, dict)
        assert "data" in monitors
        assert isinstance(monitors["data"], list)
        assert len(monitors["data"]) == 1
        assert "id" in monitors["data"][0]
        assert monitors["data"][0]["id"] == "123456"
        assert "type" in monitors["data"][0]
        assert monitors["data"][0]["type"] == "monitor"

    def test_list_monitor_groups(self, client: betteruptime.Client) -> None:
        """
        Test list monitor groups.
        """
        monitor_groups = client.monitor_groups.list()
        assert isinstance(monitor_groups, dict)
        assert "data" in monitor_groups
        assert isinstance(monitor_groups["data"], list)
        assert len(monitor_groups["data"]) == 1
        assert "id" in monitor_groups["data"][0]
        assert monitor_groups["data"][0]["id"] == "123456"
        assert "type" in monitor_groups["data"][0]
        assert monitor_groups["data"][0]["type"] == "monitor_group"

    def test_list_monitor_group_monitors(self, client: betteruptime.Client) -> None:
        """
        Test list monitor group monitors.
        """
        monitors = client.monitor_groups("123456").monitors()
        assert isinstance(monitors, dict)
        assert "data" in monitors
        assert isinstance(monitors["data"], list)
        assert len(monitors["data"]) == 1
        assert "id" in monitors["data"][0]
        assert monitors["data"][0]["id"] == "123456"
        assert "type" in monitors["data"][0]
        assert monitors["data"][0]["type"] == "monitor"
        monitors_iter = client.monitor_groups("123456").monitors_iter()
        assert isinstance(monitors_iter, types.GeneratorType)

    def test_list_on_calls(self, client: betteruptime.Client) -> None:
        """
        Test list on_calls.
        """
        on_calls = client.on_calls.list()
        assert isinstance(on_calls, dict)
        assert "data" in on_calls
        assert isinstance(on_calls["data"], list)
        assert len(on_calls["data"]) == 1
        assert "id" in on_calls["data"][0]
        assert on_calls["data"][0]["id"] == "123456"
        assert "type" in on_calls["data"][0]
        assert on_calls["data"][0]["type"] == "on_call_calendar"

    def test_list_policies(self, client: betteruptime.Client) -> None:
        """
        Test list escalation policies.
        """
        policies = client.policies.list()
        assert isinstance(policies, dict)
        assert "data" in policies
        assert isinstance(policies["data"], list)
        assert len(policies["data"]) == 0

    def test_list_status_pages(self, client: betteruptime.Client) -> None:
        """
        Test list status pages.
        """
        status_pages = client.status_pages.list()
        assert isinstance(status_pages, dict)
        assert "data" in status_pages
        assert isinstance(status_pages["data"], list)
        assert len(status_pages["data"]) == 1
        assert "id" in status_pages["data"][0]
        assert status_pages["data"][0]["id"] == "123456"
        assert "type" in status_pages["data"][0]
        assert status_pages["data"][0]["type"] == "status_page"

    def test_list_status_page_reports(self, client: betteruptime.Client) -> None:
        """
        Test list status page reports.
        """
        reports = client.status_pages("123456").reports.list()
        assert isinstance(reports, dict)
        assert "data" in reports
        assert isinstance(reports["data"], list)
        assert len(reports["data"]) == 0
        assert "pagination" in reports
        assert isinstance(reports["pagination"], dict)
        assert "first" in reports["pagination"]
        assert (
            "https://betteruptime.com/api/v2/status-pages/123456/status-reports?page=1"
            == reports["pagination"]["first"]
        )

    def test_list_status_page_report_status_updates(self, client: betteruptime.Client) -> None:
        """
        Test list status page report status updates.
        """
        status_updates = client.status_pages("123456").reports("123456").status_updates.list()
        assert isinstance(status_updates, dict)
        assert "data" in status_updates
        assert isinstance(status_updates["data"], list)
        assert len(status_updates["data"]) == 2
        assert "id" in status_updates["data"][0]
        assert status_updates["data"][0]["id"] == "123456"
        assert "type" in status_updates["data"][0]
        assert status_updates["data"][0]["type"] == "status_update"
        assert "attributes" in status_updates["data"][0]
        assert isinstance(status_updates["data"][0]["attributes"], dict)
        assert "message" in status_updates["data"][0]["attributes"]
        assert status_updates["data"][0]["attributes"]["message"] == "First status update message"
        assert "status_report_id" in status_updates["data"][0]["attributes"]
        assert status_updates["data"][0]["attributes"]["status_report_id"] == 123456
        assert "id" in status_updates["data"][1]
        assert status_updates["data"][1]["id"] == "123457"
        assert "type" in status_updates["data"][1]
        assert status_updates["data"][1]["type"] == "status_update"
        assert "attributes" in status_updates["data"][1]
        assert isinstance(status_updates["data"][1]["attributes"], dict)
        assert "message" in status_updates["data"][1]["attributes"]
        assert status_updates["data"][1]["attributes"]["message"] == "Second status update message"
        assert "status_report_id" in status_updates["data"][1]["attributes"]
        assert status_updates["data"][1]["attributes"]["status_report_id"] == 123456

    def test_list_status_page_resources(self, client: betteruptime.Client) -> None:
        """
        Test list status page resources.
        """
        resources = client.status_pages("123456").resources.list()
        assert isinstance(resources, dict)
        assert "data" in resources
        assert isinstance(resources["data"], list)
        assert len(resources["data"]) == 2
        assert "id" in resources["data"][0]
        assert resources["data"][0]["id"] == "123456"
        assert "type" in resources["data"][0]
        assert resources["data"][0]["type"] == "status_page_resource"
        assert "attributes" in resources["data"][0]
        assert isinstance(resources["data"][0]["attributes"], dict)
        assert "status_page_section_id" in resources["data"][0]["attributes"]
        assert resources["data"][0]["attributes"]["status_page_section_id"] == 1
        assert "resource_id" in resources["data"][0]["attributes"]
        assert resources["data"][0]["attributes"]["resource_id"] == 1
        assert "resource_type" in resources["data"][0]["attributes"]
        assert resources["data"][0]["attributes"]["resource_type"] == "EmailIntegration"
        assert "id" in resources["data"][1]
        assert resources["data"][1]["id"] == "123457"
        assert "type" in resources["data"][1]
        assert resources["data"][1]["type"] == "status_page_resource"
        assert "attributes" in resources["data"][1]
        assert isinstance(resources["data"][1]["attributes"], dict)
        assert "status_page_section_id" in resources["data"][1]["attributes"]
        assert resources["data"][1]["attributes"]["status_page_section_id"] == 1
        assert "resource_id" in resources["data"][1]["attributes"]
        assert resources["data"][1]["attributes"]["resource_id"] == 2
        assert "resource_type" in resources["data"][1]["attributes"]
        assert resources["data"][1]["attributes"]["resource_type"] == "Monitor"

    def test_list_status_page_sections(self, client: betteruptime.Client) -> None:
        """
        Test list status page sections.
        """
        sections = client.status_pages("123456").sections.list()
        assert isinstance(sections, dict)
        assert "data" in sections
        assert isinstance(sections["data"], list)
        assert len(sections["data"]) == 1
        assert "id" in sections["data"][0]
        assert sections["data"][0]["id"] == "123456"
        assert "type" in sections["data"][0]
        assert sections["data"][0]["type"] == "status_page_section"

    def test_get_heartbeat_200(self, client: betteruptime.Client) -> None:
        """
        Test get single heartbeat.
        """
        heartbeat = client.heartbeats.get("123456")
        assert isinstance(heartbeat, dict)
        assert "id" in heartbeat["data"]
        assert heartbeat["data"]["id"] == "123456"
        assert "type" in heartbeat["data"]
        assert heartbeat["data"]["type"] == "heartbeat"

    def test_get_heartbeat_404(self, client: betteruptime.Client) -> None:
        """
        Test get single heartbeat but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.heartbeats.get("123456")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'heartbeats' resource." == excinfo.value.message
        )

    def test_get_heartbeat_group_200(self, client: betteruptime.Client) -> None:
        """
        Test get single heartbeat group.
        """
        heartbeat_group = client.heartbeat_groups.get("123456")
        assert isinstance(heartbeat_group, dict)
        assert "id" in heartbeat_group["data"]
        assert heartbeat_group["data"]["id"] == "123456"
        assert "type" in heartbeat_group["data"]
        assert heartbeat_group["data"]["type"] == "heartbeat_group"

    def test_get_heartbeat_group_404(self, client: betteruptime.Client) -> None:
        """
        Test get single heartbeat group but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.heartbeat_groups.get("123456")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'heartbeat-groups' resource." == excinfo.value.message
        )

    def test_get_incident_200(self, client: betteruptime.Client) -> None:
        """
        Test get single incident.
        """
        incident = client.incidents.get("123456")
        assert isinstance(incident, dict)
        assert "id" in incident["data"]
        assert incident["data"]["id"] == "123456"
        assert "type" in incident["data"]
        assert incident["data"]["type"] == "incident"

    def test_get_incident_404(self, client: betteruptime.Client) -> None:
        """
        Test get single incident but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.incidents.get("123456")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'incidents' resource." == excinfo.value.message
        )

    def test_get_metadata_200(self, client: betteruptime.Client) -> None:
        """
        Test get single metadata.
        """
        metadata = client.metadata.get("123456")
        assert isinstance(metadata, dict)
        assert "id" in metadata["data"]
        assert metadata["data"]["id"] == "123456"
        assert "type" in metadata["data"]
        assert metadata["data"]["type"] == "metadata"

    def test_get_metadata_404(self, client: betteruptime.Client, mocker: MockerFixture) -> None:
        """
        Test get single metadata but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.metadata.get("123456")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'metadata' resource." == excinfo.value.message
        )

    def test_get_monitor_200(self, client: betteruptime.Client) -> None:
        """
        Test get single monitor.
        """
        monitor = client.monitors.get("123456")
        assert isinstance(monitor, dict)
        assert "id" in monitor["data"]
        assert monitor["data"]["id"] == "123456"
        assert "type" in monitor["data"]
        assert monitor["data"]["type"] == "monitor"

    def test_get_monitor_404(self, client: betteruptime.Client) -> None:
        """
        Test get single monitor but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.monitors.get("123456")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'monitors' resource." == excinfo.value.message
        )

    def test_get_monitor_by_name_200(self, client: betteruptime.Client) -> None:
        """
        Test get single monitor by name.
        """
        monitor = client.monitors.get_by_name("Backend")
        assert isinstance(monitor, dict)
        assert "id" in monitor["data"]
        assert monitor["data"]["id"] == "123456"
        assert "type" in monitor["data"]
        assert monitor["data"]["type"] == "monitor"
        assert "attributes" in monitor["data"]
        assert "pronounceable_name" in monitor["data"]["attributes"]
        assert monitor["data"]["attributes"]["pronounceable_name"] == "Backend"

    def test_get_monitor_by_name_404(self, client: betteruptime.Client) -> None:
        """
        Test get single monitor by name but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.monitors.get_by_name("Non existant monitor")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Nothing matches the given URI while querying 'monitors' resource." == excinfo.value.message
        )

    def test_get_monitor_by_url_200(self, client: betteruptime.Client) -> None:
        """
        Test get single monitor by url.
        """
        monitor = client.monitors.get_by_url("https://api.my.company")
        assert isinstance(monitor, dict)
        assert "id" in monitor["data"]
        assert monitor["data"]["id"] == "123456"
        assert "type" in monitor["data"]
        assert monitor["data"]["type"] == "monitor"
        assert "attributes" in monitor["data"]
        assert "url" in monitor["data"]["attributes"]
        assert monitor["data"]["attributes"]["url"] == "https://api.my.company"

    def test_get_monitor_by_url_404(self, client: betteruptime.Client) -> None:
        """
        Test get single monitor by url but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.monitors.get_by_url("https://non-existant.monitor")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Nothing matches the given URI while querying 'monitors' resource." == excinfo.value.message
        )

    def test_get_monitor_group_200(self, client: betteruptime.Client) -> None:
        """
        Test get single monitor group.
        """
        monitor_group = client.monitor_groups.get("123456")
        assert isinstance(monitor_group, dict)
        assert "id" in monitor_group["data"]
        assert monitor_group["data"]["id"] == "123456"
        assert "type" in monitor_group["data"]
        assert monitor_group["data"]["type"] == "monitor_group"

    def test_get_monitor_group_404(self, client: betteruptime.Client) -> None:
        """
        Test get single monitor group but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.monitor_groups.get("123456")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'monitor-groups' resource." == excinfo.value.message
        )

    def test_get_on_call_200(self, client: betteruptime.Client) -> None:
        """
        Test get single on call calendar.
        """
        on_call = client.on_calls.get("123456")
        assert isinstance(on_call, dict)
        assert "id" in on_call["data"]
        assert on_call["data"]["id"] == "123456"
        assert "type" in on_call["data"]
        assert on_call["data"]["type"] == "on_call_calendar"

    def test_get_on_call_404(self, client: betteruptime.Client) -> None:
        """
        Test get single on call calendar but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.on_calls.get("123456")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'on-calls' resource." == excinfo.value.message
        )

    def test_get_policy_200(self, client: betteruptime.Client) -> None:
        """
        Test get single escalation policy.
        """
        policy = client.policies.get("123456")
        assert isinstance(policy, dict)
        assert "id" in policy["data"]
        assert policy["data"]["id"] == "123456"
        assert "type" in policy["data"]
        assert policy["data"]["type"] == "policy"

    def test_get_policy_404(self, client: betteruptime.Client) -> None:
        """
        Test get single escalation policy but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.policies.get("123456")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'policies' resource." == excinfo.value.message
        )

    def test_get_status_page_200(self, client: betteruptime.Client) -> None:
        """
        Test get single status page.
        """
        status_page = client.status_pages.get("123456")
        assert isinstance(status_page, dict)
        assert "id" in status_page["data"]
        assert status_page["data"]["id"] == "123456"
        assert "type" in status_page["data"]
        assert status_page["data"]["type"] == "status_page"

    def test_get_status_page_404(self, client: betteruptime.Client) -> None:
        """
        Test get single status page but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.status_pages.get("123456")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'status-pages' resource." == excinfo.value.message
        )

    def test_get_status_page_report_200(self, client: betteruptime.Client) -> None:
        """
        Test get single status page report.
        """
        report = client.status_pages("123456").reports("123456").get()
        assert isinstance(report, dict)
        assert "id" in report["data"]
        assert report["data"]["id"] == "123456"
        assert "type" in report["data"]
        assert report["data"]["type"] == "status_report"

    def test_get_status_page_report_404(self, client: betteruptime.Client) -> None:
        """
        Test get single status page report but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.status_pages("123456").reports("123456").get()
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'status-reports' resource." == excinfo.value.message
        )

    def test_get_status_page_report_status_update_200(self, client: betteruptime.Client) -> None:
        """
        Test get single status page report status update.
        """
        status_update = client.status_pages("123456").reports("123456").status_updates.get("123456")
        assert isinstance(status_update, dict)
        assert "id" in status_update["data"]
        assert status_update["data"]["id"] == "123456"
        assert "type" in status_update["data"]
        assert status_update["data"]["type"] == "status_update"

    def test_get_status_page_report_status_update_404(self, client: betteruptime.Client) -> None:
        """
        Test get single status page report status update but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.status_pages("123456").reports("123456").status_updates.get("123456")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'status-updates' resource." == excinfo.value.message
        )

    def test_get_status_page_resource_200(self, client: betteruptime.Client) -> None:
        """
        Test get single status page resource.
        """
        resource = client.status_pages("123456").resources("123456").get()
        assert isinstance(resource, dict)
        assert "id" in resource["data"]
        assert resource["data"]["id"] == "123456"
        assert "type" in resource["data"]
        assert resource["data"]["type"] == "status_page_resource"

    def test_get_status_page_resource_404(self, client: betteruptime.Client) -> None:
        """
        Test get single status page resource but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.status_pages("123456").resources("123456").get()
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'resources' resource." == excinfo.value.message
        )

    def test_get_status_page_section_200(self, client: betteruptime.Client) -> None:
        """
        Test get single status page section.
        """
        section = client.status_pages("123456").sections("123456").get()
        assert isinstance(section, dict)
        assert "id" in section["data"]
        assert section["data"]["id"] == "123456"
        assert "type" in section["data"]
        assert section["data"]["type"] == "status_page_section"

    def test_get_status_page_section_404(self, client: betteruptime.Client) -> None:
        """
        Test get single status page section but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.status_pages("123456").sections("123456").get()
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'sections' resource." == excinfo.value.message
        )

    def test_post_monitor_201(self, client: betteruptime.Client) -> None:
        """
        Test create a monitor.
        """
        new_monitor = {
            "monitor_type": "status",
            "url": "https://facebook.com",
            "pronounceable_name": "Facebook homepage",
            "email": True,
            "sms": False,
            "call": False,
            "check_frequency": 30,
            "request_headers": [{"name": "X-Custom-Header", "value": "custom header value"}],
        }
        monitor = client.monitors.create(new_monitor)
        assert isinstance(monitor, dict)
        assert "id" in monitor["data"]
        assert monitor["data"]["id"] == "123456"
        assert "type" in monitor["data"]
        assert monitor["data"]["type"] == "monitor"

    def test_patch_monitor_200(self, client: betteruptime.Client) -> None:
        """
        Test update a monitor.
        """
        changed_fields = {"email": False}
        monitor = client.monitors("123456").update(changed_fields)
        assert isinstance(monitor, dict)
        assert "id" in monitor["data"]
        assert monitor["data"]["id"] == "123456"
        assert "type" in monitor["data"]
        assert monitor["data"]["type"] == "monitor"
        assert "attributes" in monitor["data"]
        assert "email" in monitor["data"]["attributes"]
        assert monitor["data"]["attributes"]["email"] is False

    def test_delete_monitor_204(self, client: betteruptime.Client) -> None:
        """
        Test delete a monitor.
        """
        result = client.monitors.delete("123456")
        assert result is None

    def test_delete_monitor_404(self, client: betteruptime.Client) -> None:
        """
        Test delete a monitor but not found.
        """
        with pytest.raises(ApiError) as excinfo:
            client.monitors.delete("123456")
        assert 404 == excinfo.value.status_code
        assert (
            "BetterUptime returned the following HTTP response code: 404"
            " - Not Found while querying 'monitors' resource." == excinfo.value.message
        )
        assert "Resource type monitor with id = 123456 was not found" == excinfo.value.errors

    def test_delete_monitor_by_name_204(self, client: betteruptime.Client) -> None:
        """
        Test delete a monitor by name.
        """
        result = client.monitors.delete_by_name("Backend")
        assert result is None

    def test_delete_monitor_by_url_204(self, client: betteruptime.Client) -> None:
        """
        Test delete a monitor by url.
        """
        result = client.monitors.delete_by_url("https://api.my.company")
        assert result is None
