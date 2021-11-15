# -*- coding: utf-8 -*-
from pygismeteo import gismeteo


def test_locality_id() -> None:
    moscow = gismeteo("https://www.gismeteo.ru/weather-moscow-4368/")
    assert moscow._BASE_ENDPOINT == "/weather-moscow-4368/"


def test_locality_name() -> None:
    moscow = gismeteo("Москва")
    assert moscow._BASE_ENDPOINT == "/weather-moscow-4368/"
