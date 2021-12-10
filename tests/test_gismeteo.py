# -*- coding: utf-8 -*-
import pygismeteo


def test_locality_id() -> None:
    moscow = pygismeteo.by_url("https://www.gismeteo.ru/weather-moscow-4368/")
    assert moscow._BASE_ENDPOINT == "/weather-moscow-4368/"


def test_locality_name() -> None:
    moscow = pygismeteo.by_name("Москва")
    assert moscow._BASE_ENDPOINT == "/weather-moscow-4368/"
