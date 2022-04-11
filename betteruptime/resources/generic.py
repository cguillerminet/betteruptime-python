"""
BetterUptime generic Resource classes
"""
from typing import Any, Dict, Generator, Union

from betteruptime.api.exceptions import ApiError
from betteruptime.api.http_client import HTTPClient
from betteruptime.resources.abstract import AbstractResource, AbstractSubResource
from yarl import URL


class ImmutableResource(AbstractResource):
    """
    Immutable BetterUptime Resource.
    """

    def __init__(self, http_client: HTTPClient, name: str) -> None:
        super().__init__(http_client)
        self.name = name

    def get(self, resource_id: str = None) -> Dict[str, Any]:
        """
        Get a single resource.
        """
        resource_id = resource_id or self.resource_id
        if resource_id is None:
            raise ValueError(
                f"A resource_id is mandatory to call {self.__class__.__name__}.get()."
                f" You can either use {self.__class__.__name__}.get('12345') or"
                f" {self.__class__.__name__}('12345').get()."
            )

        result = self.http_client.get(path=self._get_base_path() / resource_id)
        if 200 == result.status_code:
            return result.json()
        raise ApiError(
            resource=self.name, status_code=result.status_code, reason=result.reason
        )

    def list(self, page: int = 1) -> Dict[str, Any]:
        """
        List paginated resource.
        """
        result = self.http_client.get(
            path=self._get_base_path().update_query(page=page)
        )
        if 200 == result.status_code:
            return result.json()
        raise ApiError(
            resource=self.name, status_code=result.status_code, reason=result.reason
        )

    def list_iter(self, page: int = 1) -> Generator[Dict[str, Any], None, None]:
        """
        List all resource items by itering over all pages.
        """
        while True:
            result = self.list(page=page)
            for monitor in result["data"]:
                yield monitor
            if result["pagination"]["next"]:
                next_url: URL = URL(result["pagination"]["next"])
                page = int(next_url.query["page"])
            else:
                break


class ImmutableSubResource(AbstractSubResource):
    """
    Immutable BetterUptime SubResource.
    """

    def __init__(
        self, parent: Union[AbstractResource, "AbstractSubResource"], name: str
    ) -> None:
        super().__init__(parent)
        self.name = name

    def get(self, resource_id: str = None) -> Dict[str, Any]:
        """
        Get a single sub-resource.
        """
        resource_id = resource_id or self.resource_id
        if resource_id is None:
            raise ValueError(
                f"A resource_id is mandatory to call {self.__class__.__name__}.get()."
                f" You can either use {self.__class__.__name__}.get('12345') or"
                f" {self.__class__.__name__}('12345').get()."
            )

        result = self._get_http_client().get(
            path=self._build_path(URL(self.name)) / resource_id
        )
        if 200 == result.status_code:
            return result.json()
        raise ApiError(
            resource=self.name, status_code=result.status_code, reason=result.reason
        )

    def list(self, page: int = 1) -> Dict[str, Any]:
        """
        List paginated sub-resource.
        """
        path: URL = self._build_path(URL(self.name))
        result = self._get_http_client().get(path=path.update_query(page=page))
        if 200 == result.status_code:
            return result.json()
        raise ApiError(
            resource=self.name, status_code=result.status_code, reason=result.reason
        )

    def list_iter(self, page: int = 1) -> Generator[Dict[str, Any], None, None]:
        """
        List all sub-resource itmes by itering over all pages.
        """
        while True:
            result = self.list(page=page)
            for monitor in result["data"]:
                yield monitor
            if result["pagination"]["next"]:
                next_url: URL = URL(result["pagination"]["next"])
                page = int(next_url.query["page"])
            else:
                break


class MutableResource(ImmutableResource):
    """
    Mutable BetterUptime Resource.
    """

    def create(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create resource.
        """
        result = self.http_client.post(path=self._get_base_path(), json=payload)
        if 201 == result.status_code:
            return result.json()
        raise ApiError(
            resource=self.name, status_code=result.status_code, reason=result.reason
        )

    def delete(self, resource_id: str = None) -> Dict[str, Any]:
        """
        Delete resource.
        """
        resource_id = resource_id or self.resource_id
        if resource_id is None:
            raise ValueError(
                f"A resource_id is mandatory to call {self.__class__.__name__}.delete()."
                f" You can either use {self.__class__.__name__}.delete('12345') or"
                f" {self.__class__.__name__}('12345').delete()."
            )

        result = self.http_client.delete(path=self._get_base_path() / resource_id)
        if 204 == result.status_code:
            return result.json()
        raise ApiError(
            resource=self.name, status_code=result.status_code, reason=result.reason
        )

    def update(
        self, payload: Dict[str, Any], resource_id: str = None
    ) -> Dict[str, Any]:
        """
        Update resource.
        """
        resource_id = resource_id or self.resource_id
        if resource_id is None:
            raise ValueError(
                f"A resource_id is mandatory to call {self.__class__.__name__}.update()."
                f" You can either use {self.__class__.__name__}.update('12345') or"
                f" {self.__class__.__name__}('12345').update()."
            )

        result = self.http_client.patch(
            path=self._get_base_path() / resource_id, json=payload
        )
        if 200 == result.status_code:
            return result.json()
        raise ApiError(
            resource=self.name, status_code=result.status_code, reason=result.reason
        )


class MutableSubResource(ImmutableSubResource):
    """
    Mutable BetterUptime SubResource.
    """

    def create(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create resource.
        """
        result = self._get_http_client().post(
            path=self._build_path(URL(self.name)), json=payload
        )
        if 201 == result.status_code:
            return result.json()
        raise ApiError(
            resource=self.name, status_code=result.status_code, reason=result.reason
        )

    def delete(self, resource_id: str = None) -> Dict[str, Any]:
        """
        Delete resource.
        """
        resource_id = resource_id or self.resource_id
        if resource_id is None:
            raise ValueError(
                f"A resource_id is mandatory to call {self.__class__.__name__}.delete()."
                f" You can either use {self.__class__.__name__}.delete('12345') or"
                f" {self.__class__.__name__}('12345').delete()."
            )

        result = self._get_http_client().delete(
            path=self._build_path(URL(self.name)) / resource_id
        )
        if 204 == result.status_code:
            return result.json()
        raise ApiError(
            resource=self.name, status_code=result.status_code, reason=result.reason
        )

    def update(
        self, payload: Dict[str, Any], resource_id: str = None
    ) -> Dict[str, Any]:
        """
        Update resource.
        """
        resource_id = resource_id or self.resource_id
        if resource_id is None:
            raise ValueError(
                f"A resource_id is mandatory to call {self.__class__.__name__}.update()."
                f" You can either use {self.__class__.__name__}.update('12345') or"
                f" {self.__class__.__name__}('12345').update()."
            )

        result = self._get_http_client().patch(
            path=self._build_path(URL(self.name)) / resource_id,
            json=payload,
        )
        if 200 == result.status_code:
            return result.json()
        raise ApiError(
            resource=self.name, status_code=result.status_code, reason=result.reason
        )
