from __future__ import annotations

from pygismeteo_base import models, types
from pygismeteo_base.current import CurrentBase

from ._http import RequestsClient


class Current(CurrentBase[RequestsClient]):
    """Текущая погода."""

    __slots__ = ()

    def by_coordinates(
        self, latitude: types.Latitude, longitude: types.Longitude
    ) -> models.current.Model:
        """По координатам.

        Args:
            latitude (-90 ≤ int | float ≤ 90):
                Широта.
            longitude (-180 ≤ int | float ≤ 180):
                Долгота.
        """
        url, params = self._get_params_by_coordinates(latitude, longitude)
        return self._get_result(url, params=params)

    def by_id(self, id: types.LocalityID) -> models.current.Model:  # noqa: A002
        """По ID географического объекта.

        Args:
            id (int ≥ 1):
                ID географического объекта. Получить можно через поиск.
        """
        url, params = self._get_params_by_id(id)
        return self._get_result(url, params=params)

    def _get_result(
        self, url: str, *, params: types.Params = None
    ) -> models.current.Model:
        response = self._session.get_response(url, params=params)
        model = models.current.Response.model_validate_json(response)
        return model.response
