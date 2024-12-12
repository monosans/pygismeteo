from __future__ import annotations

import ipaddress

import httpx
import pytest

import pygismeteo


@pytest.mark.xfail(raises=httpx.HTTPStatusError)
def test_current_by_id(gismeteo_token: str, location_id: int) -> None:
    with pygismeteo.Gismeteo(token=gismeteo_token) as gismeteo:
        r = gismeteo.current.by_id(location_id)
    assert isinstance(r, pygismeteo.models.current.Model)


@pytest.mark.xfail(raises=httpx.HTTPStatusError)
def test_current_by_coordinates(
    gismeteo: pygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = gismeteo.current.by_coordinates(*coordinates)
    assert isinstance(r, pygismeteo.models.current.Model)


@pytest.mark.xfail(raises=httpx.HTTPStatusError)
def test_step3_by_id(gismeteo: pygismeteo.Gismeteo, location_id: int) -> None:
    r = gismeteo.step3.by_id(location_id, days=10)
    assert isinstance(r, pygismeteo.models.step3.Model)


@pytest.mark.xfail(raises=httpx.HTTPStatusError)
def test_step3_by_coordinates(
    gismeteo: pygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = gismeteo.step3.by_coordinates(*coordinates, days=10)
    assert isinstance(r, pygismeteo.models.step3.Model)


@pytest.mark.xfail(raises=httpx.HTTPStatusError)
def test_step6_by_id(gismeteo: pygismeteo.Gismeteo, location_id: int) -> None:
    r = gismeteo.step6.by_id(location_id, days=10)
    assert isinstance(r, pygismeteo.models.step6.Model)


@pytest.mark.xfail(raises=httpx.HTTPStatusError)
def test_step6_by_coordinates(
    gismeteo: pygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = gismeteo.step6.by_coordinates(*coordinates, days=10)
    assert isinstance(r, pygismeteo.models.step6.Model)


@pytest.mark.xfail(raises=httpx.HTTPStatusError)
def test_step24_by_id(gismeteo: pygismeteo.Gismeteo, location_id: int) -> None:
    r = gismeteo.step24.by_id(location_id, days=10)
    assert isinstance(r, pygismeteo.models.step24.Model)


@pytest.mark.xfail(raises=httpx.HTTPStatusError)
def test_step24_by_coordinates(
    gismeteo: pygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = gismeteo.step24.by_coordinates(*coordinates, days=10)
    assert isinstance(r, pygismeteo.models.step24.Model)


@pytest.mark.xfail(raises=httpx.HTTPStatusError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
def test_search_by_query(
    gismeteo: pygismeteo.Gismeteo, search_query: str
) -> None:
    r = gismeteo.search.by_query(search_query)
    assert isinstance(r, pygismeteo.models.search_by_query.Model)


@pytest.mark.xfail(raises=httpx.HTTPStatusError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
def test_search_by_coordinates(
    gismeteo: pygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = gismeteo.search.by_coordinates(*coordinates, limit=36)
    assert isinstance(r, pygismeteo.models.search_by_coordinates.Model)


@pytest.mark.xfail(raises=httpx.HTTPStatusError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
def test_search_by_ip(
    gismeteo: pygismeteo.Gismeteo, ipv4_address: ipaddress.IPv4Address
) -> None:
    r = gismeteo.search.by_ip(ipv4_address)
    assert isinstance(r, pygismeteo.models.search_by_ip.Model)
