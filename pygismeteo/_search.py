from __future__ import annotations

from ipaddress import IPv4Address
from typing import Union

from pygismeteo_base import models, types
from pygismeteo_base.search import SearchBase
from typing_extensions import Literal, overload

from ._http import RequestsClient


class Search(SearchBase[RequestsClient]):
    """Поиск."""

    __slots__ = ()

    @overload
    def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        limit: types.SearchLimit,
        *,
        as_list: Literal[True] = ...,
    ) -> tuple[models.search_by_coordinates.ModelItem, ...]: ...

    @overload
    def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        limit: types.SearchLimit,
        *,
        as_list: Literal[False],
    ) -> models.search_by_coordinates.Model: ...

    @overload
    def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        limit: types.SearchLimit,
        *,
        as_list: bool,
    ) -> Union[
        tuple[models.search_by_coordinates.ModelItem, ...],
        models.search_by_coordinates.Model,
    ]: ...

    def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        limit: types.SearchLimit,
        *,
        as_list: bool = True,
    ) -> Union[
        tuple[models.search_by_coordinates.ModelItem, ...],
        models.search_by_coordinates.Model,
    ]:
        """По координатам.

        Args:
            latitude (-90 ≤ int | float ≤ 90):
                Широта.
            longitude (-180 ≤ int | float ≤ 180):
                Долгота.
            limit (1 ≤ int ≤ 36):
                Ограничение количества результатов.
            as_list (bool):
                Вернуть Model.root (tuple[ModelItem, ...]) вместо Model.
                По умолчанию True.
        """
        params = self._get_params_by_coordinates(
            latitude=latitude, longitude=longitude, limit=limit
        )
        response = self._get_response(params)
        model = models.search_by_coordinates.Response.model_validate_json(
            response
        )
        return model.response.root if as_list else model.response

    def by_ip(self, ip: Union[IPv4Address, str]) -> models.search_by_ip.Model:
        """По IPv4-адресу.

        Args:
            ip (ipaddress.IPv4Address | str):
                IPv4-адрес.
        """
        params = self._get_params_by_ip(ip)
        response = self._get_response(params)
        model = models.search_by_ip.Response.model_validate_json(response)
        return model.response

    @overload
    def by_query(
        self, query: str, *, as_list: Literal[True] = ...
    ) -> tuple[models.search_by_query.ModelItem, ...]: ...

    @overload
    def by_query(
        self, query: str, *, as_list: Literal[False]
    ) -> models.search_by_query.Model: ...

    @overload
    def by_query(
        self, query: str, *, as_list: bool
    ) -> Union[
        tuple[models.search_by_query.ModelItem, ...],
        models.search_by_query.Model,
    ]: ...

    def by_query(
        self, query: str, *, as_list: bool = True
    ) -> Union[
        tuple[models.search_by_query.ModelItem, ...],
        models.search_by_query.Model,
    ]:
        """По строке.

        Args:
            query (str):
                Город, район, область, страна или аэропорт.
            as_list (bool):
                Вернуть Model.root (tuple[ModelItem, ...]) вместо Model.
                По умолчанию True.
        """
        params = self._get_params_by_query(query)
        response = self._get_response(params)
        model = models.search_by_query.Response.model_validate_json(response)
        return model.response.items.root if as_list else model.response.items

    def _get_response(self, params: types.Params) -> str:
        return self._session.get_response(self._endpoint(), params=params)
