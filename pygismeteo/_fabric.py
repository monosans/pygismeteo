# -*- coding: utf-8 -*-
from re import findall
from typing import Optional

from lxml.html import fromstring
from requests import Session

from pygismeteo._class import Gismeteo
from pygismeteo._http import HTTPSession
from pygismeteo.exceptions import InvalidLocalityID, LocalityNotFound


def by_name(locality: str, *, session: Optional[Session] = None) -> Gismeteo:
    """Создание экземпляра Gismeteo по названию населённого пункта.

    Args:
        locality (str): Название населённого пункта.
        session (Optional[Session], optional): Экземпляр requests.Session,
            если нужно использовать свой. Defaults to None.

    Raises:
        LocalityNotFound: Населённый пункт не найден.

    Returns:
        Gismeteo: Экземпляр класса Gismeteo.

    Examples:
        >>> gm = pygismeteo.by_name("Москва")
        ... now = gm.now()
        ... print(now.temperature)

        >>> gm = pygismeteo.by_name("Kazan")
        ... today = gm.today()
        ... print(today.wind_speed)
    """
    sess = HTTPSession(session)
    r = sess.req(f"/search/{locality}")
    tree = fromstring(r)
    localities = tree.xpath(
        '//section[contains(@class,"section-catalog")]'
        + '/section[last()]//a[contains(@class,"link-item")]/@href'
    )
    if not localities:
        raise LocalityNotFound("Населённый пункт не найден.")
    return Gismeteo(localities[0], sess)


def by_url(locality: str, *, session: Optional[Session] = None) -> Gismeteo:
    """Создание экземпляра Gismeteo по ссылке на населённый пункт.

    Args:
        locality (str): Ссылка на населённый пункт.
        session (Optional[Session], optional): Экземпляр requests.Session,
            если нужно использовать свой. Defaults to None.

    Raises:
        InvalidLocalityID: Количество ссылок не равно 1.

    Returns:
        Gismeteo: Экземпляр класса Gismeteo.

    Examples:
        >>> gm = pygismeteo.by_url("https://gismeteo.ru/weather-moscow-4368/")
        ... now = gm.now()
        ... print(now.temperature)

        >>> gm = pygismeteo.by_url("gismeteo.ru/weather-kazan-4364/")
        ... month = gm.month()
        ... print(month.status)

        >>> gm = pygismeteo.by_url("weather-sankt-peterburg-4079")
        ... today = gm.today()
        ... print(today.wind_speed)
    """
    endpoint = findall(r".*(weather-.*-\d+).*", locality)
    if len(endpoint) != 1:
        raise InvalidLocalityID("Количество ссылок не равно 1.")
    return Gismeteo(f"/{endpoint[0]}/", HTTPSession(session))
