# -*- coding: utf-8 -*-
from typing import Any, Dict, Optional

import pygismeteo_base
from requests import Session

from pygismeteo._exceptions import LocalityNotFound


class Gismeteo:
    def __init__(
        self,
        *,
        lang: pygismeteo_base.types.LANG = "ru",
        token: str = pygismeteo_base.constants.DEFAULT_TOKEN,
        session: Optional[Session] = None,
    ) -> None:
        self.lang = lang.strip()
        self.token = token.strip()
        self._session = session

    def current(self, id: int) -> pygismeteo_base.models.current.Model:
        return pygismeteo_base.models.current.Model.parse_obj(
            self._get_response(f"weather/current/{id}")
        )

    def step3(
        self, id: int, days: pygismeteo_base.types.STEP3_DAYS
    ) -> pygismeteo_base.models.step3or6.Model:
        return pygismeteo_base.models.step3or6.Model.parse_obj(
            self._get_response(f"weather/forecast/{id}", {"days": str(days)})
        )

    def step6(
        self, id: int, days: pygismeteo_base.types.DAYS
    ) -> pygismeteo_base.models.step3or6.Model:
        return pygismeteo_base.models.step3or6.Model.parse_obj(
            self._get_response(
                f"weather/forecast/by_day_part/{id}", {"days": str(days)}
            )
        )

    def step24(
        self, id: int, days: pygismeteo_base.types.DAYS
    ) -> pygismeteo_base.models.step24.Model:
        return pygismeteo_base.models.step24.Model.parse_obj(
            self._get_response(
                f"weather/forecast/aggregate/{id}", {"days": str(days)}
            )
        )

    def get_id_by_query(self, query: str) -> int:
        items = self._get_response("search/cities", {"query": query})["items"]
        if not items:
            raise LocalityNotFound("Населённый пункт не найден.")
        return int(items[0]["id"])

    def _fetch(
        self, endpoint: str, params: Optional[Dict[str, str]], session: Session
    ) -> Any:
        with session.get(
            f"https://api.gismeteo.net/v2/{endpoint}",
            params={"lang": self.lang, **(params or {})},
            headers={"X-Gismeteo-Token": self.token},
        ) as r:
            r.raise_for_status()
            return r.json()

    def _get_json(
        self, endpoint: str, params: Optional[Dict[str, str]] = None
    ) -> Any:
        if isinstance(self._session, Session):
            return self._fetch(endpoint, params, self._session)
        with Session() as session:
            return self._fetch(endpoint, params, session)

    def _get_response(
        self, endpoint: str, params: Optional[Dict[str, str]] = None
    ) -> Any:
        return self._get_json(endpoint, params)["response"]
