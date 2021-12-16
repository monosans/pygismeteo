# -*- coding: utf-8 -*-
import pygismeteo


def test_step24() -> None:
    pygismeteo.step24(4368, days="3")
