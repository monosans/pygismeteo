from __future__ import annotations

from pygismeteo_base import types
from pygismeteo_base.http import BaseHttpClient
from requests import Session


class RequestsClient(BaseHttpClient[Session]):
    __slots__ = ()

    def get_response(self, endpoint: str, /, *, params: types.Params) -> str:
        params, headers = self._get_params_and_headers(params)
        if self.session is None:
            self.session = Session()
        with self.session.get(
            f"{self.base_url}/{endpoint}/", params=params, headers=headers
        ) as response:
            pass
        response.raise_for_status()
        return response.text
