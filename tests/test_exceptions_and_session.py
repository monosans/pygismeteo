# -*- coding: utf-8 -*-
import pytest
from requests import Session

import pygismeteo
from pygismeteo.exceptions import LocalityNotFound


def test_locality_not_found() -> None:
    with pytest.raises(LocalityNotFound):
        with Session() as s:
            pygismeteo.search.id_by_query("волыфдаловыфалдоыфва", session=s)
