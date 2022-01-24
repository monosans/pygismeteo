# -*- coding: utf-8 -*-
from pygismeteo import Gismeteo


def test_step3() -> None:
    Gismeteo().step3(4368, days="3")
