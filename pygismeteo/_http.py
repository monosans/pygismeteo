from __future__ import annotations

from typing import Any, Optional

from pygismeteo_base.http import BaseHttpClient
from pygismeteo_base.types import Params
from pygismeteo_base.validators import Settings
from requests import Session


class RequestsClient(BaseHttpClient):
    __slots__ = ("session",)

    def __init__(self, session: Optional[Session], settings: Settings) -> None:
        super().__init__(settings)
        self.session = session

    def get_response(self, endpoint: str, *, params: Params = None) -> Any:
        response = self._get_json(endpoint, params=params)
        return response["response"]

    def _get_json(self, endpoint: str, *, params: Params = None) -> Any:
        if isinstance(self.session, Session):
            return self._fetch(endpoint, params=params, session=self.session)
        with Session() as session:
            return self._fetch(endpoint, params=params, session=session)

    def _fetch(
        self, endpoint: str, *, params: Params, session: Session
    ) -> Any:
        params, headers = self._get_params_and_headers(params)
        with session.get(
            f"https://api.gismeteo.net/v2/{endpoint}/",
            params=params,
            headers=headers,
        ) as response:
            response.raise_for_status()
            return response.json()
