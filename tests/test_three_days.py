# -*- coding: utf-8 -*-
from utils import check_dict

from pygismeteo import gismeteo


def test_three_days() -> None:
    gm = gismeteo("weather-moscow-4368")
    three_days = gm.three_days()
    for time in (
        three_days.night,
        three_days.morning,
        three_days.afternoon,
        three_days.evening,
    ):
        for attr in (
            time.status,
            time.temperature,
            time.gusts,
            time.precipitation,
        ):
            check_dict(attr, 10)
        for attr in (
            time.wind_speed,
            time.wind_direction,
            time.falling_snow,
            time.snow_depth,
            time.pressure,
            time.humidity,
            time.ultraviolet_index,
            time.gm_activity,
        ):
            check_dict(attr, 3)
