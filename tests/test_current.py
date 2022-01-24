# -*- coding: utf-8 -*-
from pygismeteo import Gismeteo


def test_current() -> None:
    Gismeteo().current(4368)
