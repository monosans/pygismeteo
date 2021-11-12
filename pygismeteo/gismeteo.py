# -*- coding: utf-8 -*-
from re import findall

from lxml.html import fromstring

from pygismeteo.exceptions import InvalidLocalityID, LocalityNotFound
from pygismeteo.http import req
from pygismeteo.main_class import Gismeteo


def gismeteo(locality: str) -> Gismeteo:
    """Фабрика для Gismeteo.

    Args:
        locality (str): Населённый пункт.
            Может быть ссылкой на сайт типа gismeteo.ru/weather-moscow-4368/
            или названием населённого пункта, например, Москва.

    Raises:
        InvalidLocalityID: Указана неверная ссылка.
        LocalityNotFound: Населённый пункт не найден.

    Returns:
        Gismeteo: Экземпляр класса Gismeteo.
    """
    if "weather-" in locality:
        endpoint = findall(r".*(weather-.*-\d+).*", locality)
        if len(endpoint) != 1:
            raise InvalidLocalityID()
        return Gismeteo(f"/{endpoint[0]}/")
    r = req(f"/search/{locality}")
    tree = fromstring(r)
    localities = tree.xpath(
        '//section[contains(@class,"section-catalog")]'
        + '/section[last()]//a[contains(@class,"link-item")]/@href'
    )
    if not localities:
        raise LocalityNotFound()
    return Gismeteo(localities[0])
