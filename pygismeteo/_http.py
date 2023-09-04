from __future__ import annotations

from pygismeteo_base.http import BaseHttpClient
from pygismeteo_base.types import Headers, Params
from requests import Response, Session
from typing_extensions import Any


class RequestsClient(BaseHttpClient[Session]):
    __slots__ = ()

    def get_response(self, endpoint: str, *, params: Params = None) -> Any:
        response = self._get_json(endpoint, params=params)
        return response["response"]

    def _get_json(self, endpoint: str, *, params: Params = None) -> Any:
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
        return response.json()

    def _fetch(
        self,
        endpoint: str,
        *,
        params: Params,
        headers: Headers,
        session: Session,
    ) -> Response:
        with session.get(
            f"https://api.gismeteo.net/v2/{endpoint}/",
            params=params,
            headers=headers,
        ) as response:
            return response
