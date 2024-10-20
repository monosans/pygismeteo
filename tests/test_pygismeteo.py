from __future__ import annotations

from ipaddress import IPv4Address
from typing import Union

import pydantic
import pytest
from requests import HTTPError, Session

from pygismeteo import Gismeteo, models


@pytest.mark.xfail(raises=HTTPError)
def test_current_by_id(gismeteo_token: str, location_id: int) -> None:
    gismeteo = Gismeteo(lang="en", token=gismeteo_token)
    r = gismeteo.current.by_id(location_id)
    assert isinstance(r, models.current.Model)


@pytest.mark.xfail(raises=HTTPError)
def test_current_by_coordinates(
    gismeteo: Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = gismeteo.current.by_coordinates(*coordinates)
    assert isinstance(r, models.current.Model)


@pytest.mark.xfail(raises=HTTPError)
@pytest.mark.parametrize("as_list", [True, False])
def test_step3_by_id(
    gismeteo: Gismeteo, location_id: int, as_list: bool
) -> None:
    r = gismeteo.step3.by_id(location_id, days=10, as_list=as_list)
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.step3.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=HTTPError)
@pytest.mark.parametrize("as_list", [True, False])
def test_step3_by_coordinates(
    gismeteo: Gismeteo, coordinates: tuple[float, float], as_list: bool
) -> None:
    r = gismeteo.step3.by_coordinates(*coordinates, days=10, as_list=as_list)
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.step3.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=HTTPError)
@pytest.mark.parametrize("as_list", [True, False])
def test_step6_by_id(
    gismeteo: Gismeteo, location_id: int, as_list: bool
) -> None:
    r = gismeteo.step6.by_id(location_id, days=10, as_list=as_list)
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.step6.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=HTTPError)
@pytest.mark.parametrize("as_list", [True, False])
def test_step6_by_coordinates(
    gismeteo: Gismeteo, coordinates: tuple[float, float], as_list: bool
) -> None:
    r = gismeteo.step6.by_coordinates(*coordinates, days=10, as_list=as_list)
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.step6.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=HTTPError)
@pytest.mark.parametrize("as_list", [True, False])
def test_step24_by_id(
    gismeteo: Gismeteo, location_id: int, as_list: bool
) -> None:
    r = gismeteo.step24.by_id(location_id, days=10, as_list=as_list)
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.step24.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=HTTPError)
@pytest.mark.parametrize("as_list", [True, False])
def test_step24_by_coordinates(
    gismeteo: Gismeteo, coordinates: tuple[float, float], as_list: bool
) -> None:
    r = gismeteo.step24.by_coordinates(*coordinates, days=10, as_list=as_list)
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.step24.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=HTTPError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
@pytest.mark.parametrize("as_list", [True, False])
def test_search_by_query(
    gismeteo: Gismeteo, search_query: str, as_list: bool
) -> None:
    r = gismeteo.search.by_query(search_query, as_list=as_list)
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.search_by_query.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=HTTPError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
@pytest.mark.parametrize("as_list", [True, False])
def test_search_by_coordinates(
    gismeteo: Gismeteo, coordinates: tuple[float, float], as_list: bool
) -> None:
    r = gismeteo.search.by_coordinates(*coordinates, limit=36, as_list=as_list)
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.search_by_coordinates.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=HTTPError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
@pytest.mark.parametrize("type_", [str, IPv4Address])
def test_search_by_ip(
    gismeteo: Gismeteo, ipv4_address: str, type_: type[Union[str, IPv4Address]]
) -> None:
    r = gismeteo.search.by_ip(type_(ipv4_address))
    assert isinstance(r, models.search_by_ip.Model)


def test_session(gismeteo: Gismeteo, http_session: Session) -> None:
    assert gismeteo.session is http_session
    gismeteo.session = None
    assert gismeteo.session is None


def test_valid_lang(gismeteo: Gismeteo) -> None:
    assert gismeteo.lang is None
    gismeteo.lang = "en"
    assert gismeteo.lang == "en"


def test_invalid_lang(gismeteo: Gismeteo) -> None:
    with pytest.raises(pydantic.ValidationError):
        gismeteo.lang = "asdf"  # type: ignore[assignment]


def test_token(gismeteo: Gismeteo, gismeteo_token: str) -> None:
    assert gismeteo.token == gismeteo_token
    gismeteo.token = ""
    assert gismeteo.token == ""  # noqa: PLC1901
    gismeteo.token = gismeteo_token
    assert gismeteo.token == gismeteo_token
