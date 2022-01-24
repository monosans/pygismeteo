# -*- coding: utf-8 -*-
from pygismeteo import Gismeteo


def test_get_id_by_query() -> None:
    assert Gismeteo().get_id_by_query("Москва") == 4368
