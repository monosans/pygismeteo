# -*- coding: utf-8 -*-
import pygismeteo


def test_search_and_session() -> None:
    assert pygismeteo.search.id_by_query("Москва") == 4368
