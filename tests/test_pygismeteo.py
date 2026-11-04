from __future__ import annotations

import ipaddress

import httpx2
import pytest
from pydantic import AnyHttpUrl

import pygismeteo


@pytest.mark.xfail(raises=httpx2.HTTPStatusError)
def test_current_by_id(gismeteo_token: str, location_id: int) -> None:
    with pygismeteo.Gismeteo(token=gismeteo_token) as gismeteo:
        r = gismeteo.current.by_id(location_id)
    assert isinstance(r, pygismeteo.models.current.Model)


@pytest.mark.xfail(raises=httpx2.HTTPStatusError)
def test_current_by_coordinates(
    gismeteo: pygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = gismeteo.current.by_coordinates(*coordinates)
    assert isinstance(r, pygismeteo.models.current.Model)


@pytest.mark.xfail(raises=httpx2.HTTPStatusError)
def test_step3_by_id(gismeteo: pygismeteo.Gismeteo, location_id: int) -> None:
    r = gismeteo.step3.by_id(location_id, days=10)
    assert isinstance(r, pygismeteo.models.step3.Model)


@pytest.mark.xfail(raises=httpx2.HTTPStatusError)
def test_step3_by_coordinates(
    gismeteo: pygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = gismeteo.step3.by_coordinates(*coordinates, days=10)
    assert isinstance(r, pygismeteo.models.step3.Model)


@pytest.mark.xfail(raises=httpx2.HTTPStatusError)
def test_step6_by_id(gismeteo: pygismeteo.Gismeteo, location_id: int) -> None:
    r = gismeteo.step6.by_id(location_id, days=10)
    assert isinstance(r, pygismeteo.models.step6.Model)


@pytest.mark.xfail(raises=httpx2.HTTPStatusError)
def test_step6_by_coordinates(
    gismeteo: pygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = gismeteo.step6.by_coordinates(*coordinates, days=10)
    assert isinstance(r, pygismeteo.models.step6.Model)


@pytest.mark.xfail(raises=httpx2.HTTPStatusError)
def test_step24_by_id(gismeteo: pygismeteo.Gismeteo, location_id: int) -> None:
    r = gismeteo.step24.by_id(location_id, days=10)
    assert isinstance(r, pygismeteo.models.step24.Model)


@pytest.mark.xfail(raises=httpx2.HTTPStatusError)
def test_step24_by_coordinates(
    gismeteo: pygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = gismeteo.step24.by_coordinates(*coordinates, days=10)
    assert isinstance(r, pygismeteo.models.step24.Model)


@pytest.mark.xfail(raises=httpx2.HTTPStatusError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
def test_search_by_query(gismeteo: pygismeteo.Gismeteo, search_query: str) -> None:
    r = gismeteo.search.by_query(search_query)
    assert isinstance(r, pygismeteo.models.search_by_query.Model)


@pytest.mark.xfail(raises=httpx2.HTTPStatusError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
def test_search_by_coordinates(
    gismeteo: pygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = gismeteo.search.by_coordinates(*coordinates, limit=36)
    assert isinstance(r, pygismeteo.models.search_by_coordinates.Model)


@pytest.mark.xfail(raises=httpx2.HTTPStatusError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
def test_search_by_ip(gismeteo: pygismeteo.Gismeteo, ipv4_address: ipaddress.IPv4Address) -> None:
    r = gismeteo.search.by_ip(ipv4_address)
    assert isinstance(r, pygismeteo.models.search_by_ip.Model)


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("", "/weather/current/4368/"),
        ("/v2", "/v2/weather/current/4368/"),
        ("/v2/", "/v2/weather/current/4368/"),
    ],
)
def test_request_url(gismeteo_token: str, path: str, expected: str) -> None:
    requests: list[httpx2.Request] = []

    def handler(request: httpx2.Request) -> httpx2.Response:
        requests.append(request)
        return httpx2.Response(500)

    with httpx2.Client(transport=httpx2.MockTransport(handler)) as session:
        gismeteo = pygismeteo.Gismeteo(
            token=gismeteo_token, base_url=AnyHttpUrl(f"https://example.com{path}"), session=session
        )
        with pytest.raises(httpx2.HTTPStatusError):
            gismeteo.current.by_id(4368)
    assert [request.url.path for request in requests] == [expected]
