# pygismeteo

Обёртка для [Gismeteo API](https://gismeteo.ru/api/) на Python с типизированными ответами. Асинхронная версия называется [aiopygismeteo](https://monosans.github.io/aiopygismeteo).

!!! warning "Разработка приостановлена"

    Работает с Gismeteo API v2. Новая [v4](https://docs.gismeteo.net/v4/weather/) не поддерживается.

    У разработчика нет токена Gismeteo API, поэтому библиотека не проверяется на реальном API и модели ответов могут устареть. Токен выдают по запросу на [b2b@gismeteo.ru](mailto:b2b@gismeteo.ru). Погоду без токена можно получить через [pywttr](https://github.com/monosans/pywttr).

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

- [Руководство](guide.md) с примерами по задачам: найти город, текущая погода, прогнозы, ошибки, свой HTTP-клиент.
- [Справочник API](api.md) со всеми классами, методами и полями ответов.
