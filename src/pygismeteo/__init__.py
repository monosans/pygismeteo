"""Обёртка для Gismeteo API.

Документация: <https://monosans.github.io/pygismeteo>.

Examples:
    ```python
    with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        city = gismeteo.search.by_query("Москва")[0]
        current = gismeteo.current.by_id(city.id)
    print(current.temperature.air.c)
    ```
"""

from __future__ import annotations

from pygismeteo_base import models

from pygismeteo import types
from pygismeteo._gismeteo import Gismeteo

__version__ = "8.0.6"
__all__ = ("Gismeteo", "models", "types")
