# -*- coding: utf-8 -*-
from typing import List, Optional

import pygismeteo_base
from requests import Session

from pygismeteo._http import get_response


def current(
    id: int,
    *,
    lang: pygismeteo_base.types.LANG = "ru",
    token: str = pygismeteo_base.constants.DEFAULT_TOKEN,
    session: Optional[Session] = None,
) -> pygismeteo_base.models.current.Model:
    return pygismeteo_base.models.current.Model(
        **get_response(
            f"weather/current/{id}",
            {"lang": lang},
            token=token,
            session=session,
        )
    )


def step3(
    id: int,
    days: pygismeteo_base.types.STEP3_DAYS,
    *,
    lang: pygismeteo_base.types.LANG = "ru",
    token: str = pygismeteo_base.constants.DEFAULT_TOKEN,
    session: Optional[Session] = None,
) -> List[pygismeteo_base.models.step3or6.ModelItem]:
    return pygismeteo_base.models.step3or6.Model(
        __root__=get_response(
            f"weather/forecast/{id}",
            {"lang": lang, "days": days},
            token=token,
            session=session,
        )
    ).__root__


def step6(
    id: int,
    days: pygismeteo_base.types.DAYS,
    *,
    lang: pygismeteo_base.types.LANG = "ru",
    token: str = pygismeteo_base.constants.DEFAULT_TOKEN,
    session: Optional[Session] = None,
) -> List[pygismeteo_base.models.step3or6.ModelItem]:
    return pygismeteo_base.models.step3or6.Model(
        __root__=get_response(
            f"weather/forecast/by_day_part/{id}",
            {"lang": lang, "days": days},
            token=token,
            session=session,
        )
    ).__root__


def step24(
    id: int,
    days: pygismeteo_base.types.DAYS,
    *,
    lang: pygismeteo_base.types.LANG = "ru",
    token: str = pygismeteo_base.constants.DEFAULT_TOKEN,
    session: Optional[Session] = None,
) -> List[pygismeteo_base.models.step24.ModelItem]:
    return pygismeteo_base.models.step24.Model(
        __root__=get_response(
            f"weather/forecast/aggregate/{id}",
            {"lang": lang, "days": days},
            token=token,
            session=session,
        )
    ).__root__
