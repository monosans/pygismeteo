# -*- coding: utf-8 -*-
from utils import check_dict

from pygismeteo import gismeteo


def test_two_weeks() -> None:
    gm = gismeteo("weather-moscow-4368")
    two_weeks = gm.two_weeks()
    for attr in (
        two_weeks.status,
        two_weeks.max_temperature,
        two_weeks.min_temperature,
        two_weeks.gusts,
        two_weeks.precipitation,
        two_weeks.temperature,
        two_weeks.wind_speed,
        two_weeks.wind_direction,
        two_weeks.max_pressure,
        two_weeks.min_pressure,
        two_weeks.humidity,
        two_weeks.gm_activity,
    ):
        check_dict(attr, 14)
