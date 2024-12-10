from __future__ import annotations

from ipaddress import IPv4Address

from pygismeteo_base import models, responses, types
from pygismeteo_base.endpoints.search import SearchBase

from pygismeteo._http import RequestsClient


class Search(SearchBase[RequestsClient]):
    """Поиск."""

    __slots__ = ()

    def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        *,
        limit: types.SearchLimit,
    ) -> models.search_by_coordinates.Model:
        """По координатам.

        Args:
            latitude: Широта.
            longitude: Долгота.
            limit: Ограничение количества результатов.

        Examples:
            ```python
            search_results = gismeteo.search.by_coordinates(
                55.75222, 37.61556, limit=36
            )
            print(search_results)
            ```
        """
        url, params = self._get_params_by_coordinates(
            latitude=latitude, longitude=longitude, limit=limit
        )
        return responses.search_by_coordinates.validate_json(
            self._session.get_response(url, params=params)
        )["response"]

    def by_ip(self, ip: IPv4Address, /) -> models.search_by_ip.Model:
        """По IPv4-адресу.

        Args:
            ip: IPv4-адрес.

        Examples:
            ```python
            from ipaddress import IPv4Address

            search_results = gismeteo.search.by_ip(IPv4Address("8.8.8.8"))
            print(search_results)
            ```
        """
        url, params = self._get_params_by_ip(ip)
        return responses.search_by_ip.validate_json(
            self._session.get_response(url, params=params)
        )["response"]

    def by_query(self, query: str, /) -> models.search_by_query.Model:
        """По строке.

        Args:
            query: Город, район, область, страна или аэропорт.

        Examples:
            ```python
            search_results = gismeteo.search.by_query("Москва")
            print(search_results)
            ```
        """
        url, params = self._get_params_by_query(query)
        return responses.search_by_query.validate_json(
            self._session.get_response(url, params=params)
        )["response"]["items"]
