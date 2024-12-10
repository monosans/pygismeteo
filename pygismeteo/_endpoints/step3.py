from __future__ import annotations

from pygismeteo_base import models, responses, types
from pygismeteo_base.endpoints.step3 import Step3Base

from pygismeteo._http import RequestsClient


class Step3(Step3Base[RequestsClient]):
    """Погода с шагом 3 часа."""

    __slots__ = ()

    def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        *,
        days: types.Step3Days,
    ) -> models.step3.Model:
        """По координатам.

        Args:
            latitude: Широта.
            longitude: Долгота.
            days: Количество дней.

        Examples:
            ```python
            step3 = gismeteo.step3.by_coordinates(55.75222, 37.61556, days=10)
            print(step3)
            ```
        """
        url, params = self._get_params_by_coordinates(
            latitude, longitude, days=days
        )
        return self._get_result(url, params=params)

    def by_id(
        self, id_: types.LocalityID, /, *, days: types.Step3Days
    ) -> models.step3.Model:
        """По ID географического объекта.

        Args:
            id_: ID географического объекта. Получить можно через поиск.
            days: Количество дней.

        Examples:
            ```python
            search_results = gismeteo.search.by_query("Москва")
            city_id = search_results[0].id
            step3 = gismeteo.step3.by_id(city_id, days=10)
            print(step3)
            ```
        """
        url, params = self._get_params_by_id(id_, days=days)
        return self._get_result(url, params=params)

    def _get_result(
        self, url: str, /, *, params: types.Params
    ) -> models.step3.Model:
        return responses.step3.validate_json(
            self._session.get_response(url, params=params)
        )["response"]
