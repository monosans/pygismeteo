# -*- coding: utf-8 -*-
import pytest

import pygismeteo
from pygismeteo.exceptions import LocalityError


def test_by_url() -> None:
    with pytest.raises(LocalityError):
        pygismeteo.by_url("moscow-weather-4368")


def test_by_name() -> None:
    with pytest.raises(LocalityError):
        pygismeteo.by_name("волыфдаловыфалдоыфва")
