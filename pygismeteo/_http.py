from __future__ import annotations

from typing import Mapping, Optional

from pygismeteo_base import types
from pygismeteo_base.http import BaseHttpClient
from requests import Response, Session


class RequestsClient(BaseHttpClient[Session]):
    __slots__ = ()

    def get_response(
        self, endpoint: str, *, params: types.Params = None
    ) -> str:
        params, headers = self._get_params_and_headers(params)
        if isinstance(self.session, Session):
            response = self._fetch(
                endpoint, params=params, headers=headers, session=self.session
            )
        else:
            with Session() as session:
                response = self._fetch(
                    endpoint, params=params, headers=headers, session=session
                )
        response.raise_for_status()
        return response.text

    def _fetch(  # noqa: PLR6301
        self,
        endpoint: str,
        *,
        params: Optional[Mapping[str, str]],
        headers: Mapping[str, str],
        session: Session,
    ) -> Response:
        with session.get(
            f"https://api.gismeteo.net/v2/{endpoint}/",
            params=params,
            headers=headers,
        ) as response:
            return response
