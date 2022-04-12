"""
Abstract BetterUptime Resource
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, Union

from yarl import URL

from betteruptime.api.http_client import HTTPClient


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

    @abstractmethod
    def __call__(self, resource_id: str) -> AbstractResource:
        pass

    def _get_base_path(self) -> URL:
        """
        returns resource's path.
        """
        return URL(self.name)


class AbstractSubResource(AbstractResource):
    """
    Abstract BetterUptime Sub-resource.
    """

    _parent: AbstractResource

    def __init__(self, http_client: HTTPClient, parent: AbstractResource) -> None:
        super().__init__(http_client=http_client)
        self.parent = parent

    @property
    def parent(self) -> Union[AbstractResource, AbstractSubResource]:
        """
        parent property getter.
        """
        return self._parent

    @parent.setter
    def parent(self, parent: Union[AbstractResource, AbstractSubResource]) -> None:
        """
        parent property setter.
        """
        self._parent = parent

    @abstractmethod
    def __call__(self, resource_id: str) -> AbstractSubResource:
        pass

    def _build_path(
        self,
        path: URL,
        parent: Union[AbstractResource, AbstractSubResource, None] = None,
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
            if parent.resource_id is not None:
                path = URL(parent.name) / parent.resource_id

        return path

    def _get_base_path(self) -> URL:
        """
        returns resource's path.
        """
        return URL(self.name)
