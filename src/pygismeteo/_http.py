from __future__ import annotations

from httpx2 import Client, Timeout
from pygismeteo_base import types
from pygismeteo_base.http import BaseHttpClient


class HttpxClient(BaseHttpClient[Client]):
    __slots__ = ()

    def get_response(self, endpoint: str, /, *, params: types.Params) -> bytes:
        params, headers = self._get_params_and_headers(params)
        if self.session is None:
            self.session = Client(timeout=Timeout(60, connect=5), follow_redirects=True)
        response = self.session.get(
            f"{str(self.base_url).rstrip('/')}/{endpoint}/", params=params, headers=headers
        )
        response.raise_for_status()
        return response.content
