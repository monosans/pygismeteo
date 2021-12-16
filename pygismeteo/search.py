# -*- coding: utf-8 -*-
from typing import Optional as _Optional

import pygismeteo_base as _pygismeteo_base
from requests import Session as _Session

from pygismeteo._http import get_json as _get_json
from pygismeteo.exceptions import LocalityNotFound as _LocalityNotFound


def id_by_query(
    query: str,
    *,
    lang: _pygismeteo_base.types.LANG = "ru",
    token: str = _pygismeteo_base.constants.DEFAULT_TOKEN,
    session: _Optional[_Session] = None,
) -> int:
    r = _get_json(
        "search/cities",
        params={"lang": lang, "query": query},
        token=token,
        session=session,
    )
    items = r["response"]["items"]
    if not items:
        raise _LocalityNotFound("Населённый пункт не найден.")
    return int(items[0]["id"])
