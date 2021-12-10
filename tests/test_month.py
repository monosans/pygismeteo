# -*- coding: utf-8 -*-
from utils import check_dict

import pygismeteo


def test_month() -> None:
    gm = pygismeteo.by_url("weather-moscow-4368")
    month = gm.month()
    for attr in (month.status, month.max_temperature, month.min_temperature):
        check_dict(attr, 21, 31)
