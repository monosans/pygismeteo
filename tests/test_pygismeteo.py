from __future__ import annotations

from requests import Session

import pygismeteo


def test_pygismeteo() -> None:
    with Session() as session:
        gm = pygismeteo.Gismeteo(session=session)
        assert gm.session is session
        gm.current.by_id(4368)
        gm.current.by_coordinates(54.35, 52.52)

        gm.step3.by_id(4368, days=10)
        gm.step3.by_coordinates(54.35, 52.52, days=10)

        gm.step6.by_id(4368, days=10)
        gm.step6.by_coordinates(54.35, 52.52, days=10)

        gm.step24.by_id(4368, days=10)
        gm.step24.by_coordinates(54.35, 52.52, days=10)

        gm.search.by_query("lond")
        gm.search.by_coordinates(54.35, 52.52, limit=36)

    assert gm.lang is None
    gm.lang = "en"
    assert gm.lang == "en"

    gm.session = None
    assert gm.session is None

    gm.search.by_ip("8.8.8.8")

    assert gm.token is None
    gm.token = ""
    assert gm.token == ""  # noqa: PLC1901
