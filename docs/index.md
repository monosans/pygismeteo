# pygismeteo

Обёртка для [Gismeteo API](https://gismeteo.ru/api/) на Python с типизированными ответами. Асинхронная версия — [aiopygismeteo](https://monosans.github.io/aiopygismeteo).

!!! warning "Разработка приостановлена"

    У разработчика нет токена Gismeteo API, поэтому библиотека не проверяется на реальном API и модели ответов могут устареть. Токен выдают по запросу на [b2b@gismeteo.ru](mailto:b2b@gismeteo.ru). Погода без токена — в [pywttr](https://github.com/monosans/pywttr).

## Установка

=== "uv"

    ```bash
    uv add pygismeteo pygismeteo-base
    ```

=== "pip"

    ```bash
    pip install -U pygismeteo pygismeteo-base
    ```

## Быстрый старт

```python
import pygismeteo

with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
    city = gismeteo.search.by_query("Москва")[0]
    current = gismeteo.current.by_id(city.id)

print(current.temperature.air.c, current.description.full)
```

## Куда дальше

- [Руководство](guide.md) — примеры по задачам: найти город, текущая погода, прогнозы, ошибки, свой HTTP-клиент.
- [API Reference](api.md) — все классы, методы и поля ответов.
