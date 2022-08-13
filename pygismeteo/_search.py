from __future__ import annotations

from typing import Any, List

from pygismeteo_base import models, search
from pygismeteo_base.types import Params, SearchLimit

from pygismeteo._http import RequestsClient


class Search(search.Search):
    __slots__ = ("_session",)

    def __init__(self, session: RequestsClient) -> None:
        self._session = session

    def by_coordinates(
        self, latitude: float, longitude: float, *, limit: SearchLimit
    ) -> List[models.search_by_coordinates.ModelItem]:
        """Поиск по координатам.

        Args:
            latitude: Широта (от -90 до 90).
            longitude: Долгота (от -180 до 180).
            limit: Ограничение количества (от 1 до 36).
        """
        params = self._get_params_by_coordinates(
            latitude=latitude, longitude=longitude, limit=limit
        )
        response = self._get_response(params)
        model = models.search_by_coordinates.Model.parse_obj(response)
        return model.__root__

    def by_ip(self, ip: str) -> models.search_by_ip.Model:
        """Поиск по IP-адресу.

        Args:
            ip: IP-адрес.
        """
        params = self._get_params_by_ip(ip)
        response = self._get_response(params)
        return models.search_by_ip.Model.parse_obj(response)

    def by_query(self, query: str) -> List[models.search_by_query.ModelItem]:
        """Поиск по строке.

        Args:
            query: Город, район, область, страна или аэропорт.
        """
        params = self._get_params_by_query(query)
        response = self._get_response(params)
        model = models.search_by_query.Model.parse_obj(response["items"])
        return model.__root__

    def _get_response(self, params: Params) -> Any:
        return self._session.get_response(self._endpoint, params=params)
