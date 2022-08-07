from __future__ import annotations

from requests import Session

from pygismeteo import Gismeteo


def test_everything() -> None:
    with Session() as session:
        gismeteo = Gismeteo(session=session)
        gismeteo.current.by_id(4368)
        gismeteo.current.by_coordinates(54.35, 52.52)

        gismeteo.step3.by_id(4368, days=10)
        gismeteo.step3.by_coordinates(54.35, 52.52, days=10)

        gismeteo.step6.by_id(4368, days=10)
        gismeteo.step6.by_coordinates(54.35, 52.52, days=10)

        gismeteo.step24.by_id(4368, days=10)
        gismeteo.step24.by_coordinates(54.35, 52.52, days=10)

        gismeteo.search.by_query("lond")
        gismeteo.search.by_coordinates(54.35, 52.52, limit=36)

    assert gismeteo.lang is None
    gismeteo.lang = "en"
    assert gismeteo.lang == "en"

    assert isinstance(gismeteo.session, Session)
    gismeteo.session = None
    assert gismeteo.session is None

    gismeteo.search.by_ip("8.8.8.8")

    assert gismeteo.token is None
    gismeteo.token = ""
    assert gismeteo.token == ""
