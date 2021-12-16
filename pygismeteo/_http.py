# -*- coding: utf-8 -*-
from typing import Any, Dict, Optional

import pygismeteo_base
from requests import Session


def _fetch(
    endpoint: str, params: Dict[str, Any], token: str, session: Session
) -> Dict[str, Any]:
    with session.get(
        f"https://api.gismeteo.net/v2/{endpoint}",
        params=params,
        headers={"X-Gismeteo-Token": token},
    ) as r:
        return dict(r.json())


def get_json(
    endpoint: str,
    params: Dict[str, Any],
    *,
    token: str = pygismeteo_base.constants.DEFAULT_TOKEN,
    session: Optional[Session] = None,
) -> Dict[str, Any]:
    if session:
        return _fetch(endpoint, params, token, session)
    with Session() as s:
        return _fetch(endpoint, params, token, s)


def get_response(
    endpoint: str,
    params: Dict[str, Any],
    *,
    token: str = pygismeteo_base.constants.DEFAULT_TOKEN,
    session: Optional[Session] = None,
) -> Dict[str, Any]:
    return (get_json(endpoint, params, token=token, session=session)).get(
        "response", {}
    )
