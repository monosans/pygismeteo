from __future__ import annotations

import ipaddress
from collections.abc import Iterator

import httpx
import pydantic
import pytest

import pygismeteo


@pytest.fixture(scope="session")
def http_session() -> Iterator[httpx.Client]:
    with httpx.Client(timeout=300, follow_redirects=True) as s:
        yield s


@pytest.fixture
def gismeteo_token() -> str:
    return "56b30cb255.3443075"


@pytest.fixture
def location_id() -> int:
    # Moscow
    return 4368


@pytest.fixture
def coordinates() -> tuple[float, float]:
    # Moscow
    return 55.7522200, 37.6155600


@pytest.fixture
def search_query() -> str:
    return "mosc"


@pytest.fixture
def ipv4_address() -> ipaddress.IPv4Address:
    return ipaddress.IPv4Address("8.8.8.8")


@pytest.fixture
def gismeteo(
    gismeteo_token: str, http_session: httpx.Client
) -> pygismeteo.Gismeteo:
    return pygismeteo.Gismeteo(token=gismeteo_token, session=http_session)


def _get_models(
    cls: type[pydantic.BaseModel] = pydantic.BaseModel, /
) -> Iterator[type[pydantic.BaseModel]]:
    for subclass in cls.__subclasses__():
        if subclass.__module__.startswith(f"{pygismeteo.models.__name__}."):
            yield subclass
        yield from _get_models(subclass)


@pytest.fixture
def _pydantic_ignore_extra(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    models = tuple(_get_models())
    with monkeypatch.context() as m:
        for model in models:
            m.setitem(model.model_config, "extra", "ignore")
            model.model_rebuild(force=True)
        yield
    for model in models:
        model.model_rebuild(force=True)


@pytest.fixture(autouse=True)
def _pydantic_forbid_extra(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    models = tuple(_get_models())
    with monkeypatch.context() as m:
        for model in models:
            m.setitem(model.model_config, "extra", "forbid")
            model.model_rebuild(force=True)
        yield
    for model in models:
        model.model_rebuild(force=True)
