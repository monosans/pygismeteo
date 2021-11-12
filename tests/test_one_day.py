# -*- coding: utf-8 -*-
from requests import Session
from utils import check_dict

from pygismeteo import gismeteo


def test_one_day() -> None:
    with Session() as s:
        gm = gismeteo("weather-moscow-4368", session=s)
        for callable in (
            gm.today,
            gm.tomorrow,
            gm.in3_days,
            gm.in4_days,
            gm.in5_days,
            gm.in6_days,
            gm.in7_days,
            gm.in8_days,
            gm.in9_days,
            gm.in10_days,
        ):
            day = callable()
            for attr in (
                day.status,
                day.temperature,
                day.wind_speed,
                day.precipitation,
                day.wind_direction,
                day.falling_snow,
                day.snow_depth,
                day.road_condition,
                day.pressure,
                day.humidity,
                day.visibility,
                day.ultraviolet_index,
                day.gm_activity,
            ):
                check_dict(attr, 8)
