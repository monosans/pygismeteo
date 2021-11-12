# -*- coding: utf-8 -*-
from utils import check_dict

from pygismeteo import gismeteo


def test_month() -> None:
    gm = gismeteo("weather-moscow-4368")
    month = gm.month()
    for attr in (month.status, month.max_temperature, month.min_temperature):
        check_dict(attr, 27, 31)
