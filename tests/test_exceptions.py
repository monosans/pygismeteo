# -*- coding: utf-8 -*-
import pytest

from pygismeteo import InvalidLocalityID, LocalityNotFound, gismeteo


def test_invalid_locality_id() -> None:
    with pytest.raises(InvalidLocalityID):
        gismeteo("moscow-weather-4368")


def test_locality_not_found() -> None:
    with pytest.raises(LocalityNotFound):
        gismeteo("волыфдаловыфалдоыфва")
