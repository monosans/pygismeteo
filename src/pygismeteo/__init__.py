"""Обёртка для Gismeteo API.

Examples:
    ```python
    with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        search_results = gismeteo.search.by_query("Москва")
        city_id = search_results[0].id
        current = gismeteo.current.by_id(city_id)
    print(current)
    ```

    Кастомный базовый URL:

    ```python
    with pygismeteo.Gismeteo(
        token=..., base_url=pydantic.AnyHttpUrl("https://api.example.com/v1")
    ) as gismeteo:
        ...
    ```

    Другой язык:

    ```python
    with pygismeteo.Gismeteo(token=..., lang=pygismeteo.Lang.EN) as gismeteo:
        ...
    ```

    Кастомный httpx.Client:

    ```python
    with httpx.Client(
        timeout=httpx.Timeout(60, connect=5), follow_redirects=True
    ) as session:
        gismeteo = pygismeteo.Gismeteo(token=..., session=session)
        ...
    ```
"""

from __future__ import annotations

from importlib.metadata import version as _version

from pygismeteo_base import models

from pygismeteo import types
from pygismeteo._gismeteo import Gismeteo

__version__ = _version(__name__)
__all__ = ("Gismeteo", "models", "types")
