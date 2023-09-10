from __future__ import annotations

from typing import Iterator, Tuple

import pydantic.v1 as pydantic
import pytest
from requests import Session

from pygismeteo import Gismeteo


@pytest.fixture(scope="session")
def http_session() -> Iterator[Session]:
    with Session() as s:
        yield s


@pytest.fixture()
def location_id() -> int:
    # Moscow
    return 4368


@pytest.fixture()
def coordinates() -> Tuple[float, float]:
    # Moscow
    return 55.7522200, 37.6155600


@pytest.fixture()
def search_query() -> str:
    return "mosc"


@pytest.fixture()
def ipv4_address() -> str:
    return "8.8.8.8"


@pytest.fixture()
def gismeteo(http_session: Session) -> Gismeteo:
    return Gismeteo(session=http_session)


@pytest.fixture()
def _pydantic_ignore_extra(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(pydantic.BaseConfig, "extra", pydantic.Extra.ignore)


@pytest.fixture(autouse=True)
def _pydantic_strict(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(pydantic.BaseConfig, "extra", pydantic.Extra.forbid)
    monkeypatch.setattr(pydantic.BaseConfig, "validate_all", True)
    monkeypatch.setattr(pydantic.BaseConfig, "validate_assignment", True)
