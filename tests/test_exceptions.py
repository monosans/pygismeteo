# -*- coding: utf-8 -*-
import pytest

import pygismeteo
from pygismeteo.exceptions import InvalidLocalityID, LocalityNotFound


def test_invalid_locality_id() -> None:
    with pytest.raises(InvalidLocalityID):
        pygismeteo.by_url("moscow-weather-4368")


def test_locality_not_found() -> None:
    with pytest.raises(LocalityNotFound):
        pygismeteo.by_name("волыфдаловыфалдоыфва")
