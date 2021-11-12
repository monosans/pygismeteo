# -*- coding: utf-8 -*-
from pygismeteo import gismeteo


def test_now() -> None:
    moscow = gismeteo("weather-moscow-4368")
    now = moscow.now()
    for attr in (
        now.status,
        now.temperature,
        now.real_feel,
        now.sunrise,
        now.sunset,
        now.wind_speed,
        now.wind_direction,
        now.pressure,
        now.humidity,
        now.gm_activity,
        now.water,
    ):
        assert isinstance(attr, str) and attr
