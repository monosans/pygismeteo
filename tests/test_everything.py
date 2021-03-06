from __future__ import annotations

from requests import Session

from pygismeteo import Gismeteo


def test_everything() -> None:
    with Session() as s:
        g = Gismeteo(session=s)
        g.current.by_id(4368)
        g.current.by_coordinates(54.35, 52.52)

        g.step3.by_id(4368, days=10)
        g.step3.by_coordinates(54.35, 52.52, days=10)

        g.step6.by_id(4368, days=10)
        g.step6.by_coordinates(54.35, 52.52, days=10)

        g.step24.by_id(4368, days=10)
        g.step24.by_coordinates(54.35, 52.52, days=10)

        g.search.by_query("lond")
        g.search.by_coordinates(54.35, 52.52, limit=36)

    assert g.lang is None
    g.lang = "en"
    assert g.lang == "en"

    assert isinstance(g.session, Session)
    g.session = None
    assert g.session is None

    g.search.by_ip("8.8.8.8")

    assert g.token is None
    g.token = ""
    assert g.token == ""
