# -*- coding: utf-8 -*-
import pytest
from requests import Session

from pygismeteo import Gismeteo, LocalityNotFound


def test_exception_and_session() -> None:
    with Session() as s, pytest.raises(LocalityNotFound):
        Gismeteo(session=s).get_id_by_query("волыфдаловыфалдоыфва")
