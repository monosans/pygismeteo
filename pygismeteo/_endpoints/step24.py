from __future__ import annotations

from pygismeteo_base import models, responses, types
from pygismeteo_base.endpoints.step24 import Step24Base

from pygismeteo._http import RequestsClient


class Step24(Step24Base[RequestsClient]):
    """Погода с шагом 24 часа."""

    __slots__ = ()

    def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        *,
        days: types.Step24Days,
    ) -> models.step24.Model:
        """По координатам.

        Args:
            latitude: Широта.
            longitude: Долгота.
            days: Количество дней.

        Examples:
            ```python
            step24 = gismeteo.step24.by_coordinates(55.75222, 37.61556, days=10)
            print(step24)
            ```
        """
        url, params = self._get_params_by_coordinates(
            latitude, longitude, days=days
        )
        return self._get_result(url, params=params)

    def by_id(
        self, id_: types.LocalityID, /, *, days: types.Step24Days
    ) -> models.step24.Model:
        """По ID географического объекта.

        Args:
            id_: ID географического объекта. Получить можно через поиск.
            days: Количество дней.

        Examples:
            ```python
            search_results = gismeteo.search.by_query("Москва")
            city_id = search_results[0].id
            step24 = gismeteo.step24.by_id(city_id, days=10)
            print(step24)
            ```
        """
        url, params = self._get_params_by_id(id_, days=days)
        return self._get_result(url, params=params)

    def _get_result(
        self, url: str, /, *, params: types.Params
    ) -> models.step24.Model:
        return responses.step24.validate_json(
            self._session.get_response(url, params=params)
        )["response"]
