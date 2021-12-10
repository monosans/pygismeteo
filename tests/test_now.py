# -*- coding: utf-8 -*-
import pygismeteo


def test_now() -> None:
    moscow = pygismeteo.by_url("weather-moscow-4368")
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
