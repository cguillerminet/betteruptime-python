"""
Abstract BetterUptime Resource
"""
from abc import ABC
from typing import Optional, Union

from betteruptime.api.http_client import HTTPClient
from yarl import URL


class AbstractResource(ABC):
    """
    Abstract BetterUptime Resource, all resources should inherit from
    this class.
    """

    _http_client: HTTPClient
    _name: str
    _resource_id: Optional[str] = None

    def __init__(self, http_client: HTTPClient) -> None:
        super().__init__()
        self.http_client = http_client

    @property
    def http_client(self) -> HTTPClient:
        """
        http_client property getter.
        """
        return self._http_client

    @http_client.setter
    def http_client(self, http_client: HTTPClient) -> None:
        """
        http_client property setter.
        """
        self._http_client = http_client

    @property
    def name(self) -> str:
        """
        name property getter.
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        name property setter.
        """
        self._name = name

    @property
    def resource_id(self) -> Optional[str]:
        """
        resource_id property getter.
        """
        return self._resource_id

    def __call__(self, resource_id: str) -> "AbstractResource":
        new_resource: AbstractResource = self.__class__(http_client=self.http_client)
        new_resource._resource_id = resource_id
        return new_resource

    def _get_base_path(self) -> URL:
        """
        returns resource's path.
        """
        return URL(self.name)


class AbstractSubResource(ABC):
    """
    Abstract BetterUptime Sub-resource.
    """

    _name: str
    _parent: Union[AbstractResource, "AbstractSubResource"]
    _resource_id: Optional[str] = None

    def __init__(self, parent: Union[AbstractResource, "AbstractSubResource"]) -> None:
        super().__init__()
        self.parent = parent

    @property
    def parent(self) -> Union[AbstractResource, "AbstractSubResource"]:
        """
        parent property getter.
        """
        return self._parent

    @parent.setter
    def parent(self, parent: Union[AbstractResource, "AbstractSubResource"]) -> None:
        """
        parent property setter.
        """
        self._parent = parent

    @property
    def name(self) -> str:
        """
        name property getter.
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        name property setter.
        """
        self._name = name

    @property
    def resource_id(self) -> Optional[str]:
        """
        resource_id property getter.
        """
        return self._resource_id

    def __call__(self, resource_id: str) -> "AbstractSubResource":
        new_subresource: AbstractSubResource = self.__class__(parent=self.parent)
        new_subresource._resource_id = resource_id
        return new_subresource

    def _build_path(
        self,
        path: URL,
        parent: Union[AbstractResource, "AbstractSubResource", None] = None,
    ) -> URL:
        if parent is None:
            path_part = self._build_path(path=URL(self.name), parent=self.parent)
            path = path_part / str(path)
        elif isinstance(parent, AbstractSubResource):
            path_part = self._build_path(path=path, parent=parent.parent)
            if parent.resource_id:
                path = path_part / str(URL(parent.name) / parent.resource_id)
            else:
                path = path_part / parent.name
        elif isinstance(parent, AbstractResource):
            path = URL(parent.name) / parent.resource_id

        return path

    def _get_base_path(self) -> URL:
        """
        returns resource's path.
        """
        return URL(self.name)

    def _get_http_client(
        self,
        parent: Union[AbstractResource, "AbstractSubResource", None] = None,
    ) -> HTTPClient:
        """
        returns HTTPClient.
        """
        if parent is None:
            http_client = self._get_http_client(parent=self.parent)
        elif isinstance(parent, AbstractSubResource):
            http_client = self._get_http_client(parent=parent.parent)
        elif isinstance(parent, AbstractResource):
            http_client = parent.http_client

        return http_client
