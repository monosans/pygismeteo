# -*- coding: utf-8 -*-
from pygismeteo import Gismeteo


def test_step24() -> None:
    Gismeteo().step24(4368, days="3")
