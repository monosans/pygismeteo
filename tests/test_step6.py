# -*- coding: utf-8 -*-
from pygismeteo import Gismeteo


def test_step6() -> None:
    Gismeteo().step6(4368, days="3")
