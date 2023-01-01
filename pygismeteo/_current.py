from __future__ import annotations

from pygismeteo_base import models
from pygismeteo_base.current import CurrentBase
from pygismeteo_base.types import Params

from ._http import RequestsClient


class Current(CurrentBase[RequestsClient]):
    """Текущая погода."""

    __slots__ = ()

    def by_coordinates(
        self, latitude: float, longitude: float
    ) -> models.current.Model:
        """По координатам.

        Args:
            latitude: Широта (от -90 до 90).
            longitude: Долгота (от -180 до 180).
        """
        url, params = self._get_params_by_coordinates(latitude, longitude)
        return self._get_result(url, params=params)

    def by_id(
        self,
        # pylint: disable-next=invalid-name,redefined-builtin
        id: int,
    ) -> models.current.Model:
        """По ID географического объекта.

        Args:
            id: ID географического объекта. Получить можно через поиск.
        """
        url, params = self._get_params_by_id(id)
        return self._get_result(url, params=params)

    def _get_result(
        self, url: str, *, params: Params = None
    ) -> models.current.Model:
        response = self._session.get_response(url, params=params)
        return models.current.Model.parse_obj(response)
