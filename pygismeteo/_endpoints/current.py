from __future__ import annotations

from pygismeteo_base import models, responses, types
from pygismeteo_base.endpoints.current import CurrentBase

from pygismeteo._http import RequestsClient


class Current(CurrentBase[RequestsClient]):
    """Текущая погода."""

    __slots__ = ()

    def by_coordinates(
        self, latitude: types.Latitude, longitude: types.Longitude
    ) -> models.current.Model:
        """По координатам.

        Args:
            latitude: Широта.
            longitude: Долгота.

        Examples:
            ```python
            current = gismeteo.current.by_coordinates(55.75222, 37.61556)
            print(current)
            ```
        """
        url, params = self._get_params_by_coordinates(latitude, longitude)
        return self._get_result(url, params=params)

    def by_id(self, id_: types.LocalityID, /) -> models.current.Model:
        """По ID географического объекта.

        Args:
            id_: ID географического объекта. Получить можно через поиск.

        Examples:
            ```python
            search_results = gismeteo.search.by_query("Москва")
            city_id = search_results[0].id
            current = gismeteo.current.by_id(city_id)
            print(current)
            ```
        """
        url, params = self._get_params_by_id(id_)
        return self._get_result(url, params=params)

    def _get_result(
        self, url: str, /, *, params: types.Params
    ) -> models.current.Model:
        return responses.current.validate_json(
            self._session.get_response(url, params=params)
        )["response"]
