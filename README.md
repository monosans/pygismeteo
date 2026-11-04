# <img src="https://raw.githubusercontent.com/monosans/pygismeteo/main/docs/assets/logo.svg" alt="" width="40" align="top"> pygismeteo

[![Downloads](https://static.pepy.tech/badge/pygismeteo)](https://pepy.tech/project/pygismeteo)

Обёртка для [Gismeteo API](https://gismeteo.ru/api/) на Python с типизированными ответами. Асинхронная версия называется [aiopygismeteo](https://github.com/monosans/aiopygismeteo).

Разработка приостановлена: у разработчика нет токена Gismeteo API, поэтому библиотека не проверяется на реальном API. Работает с Gismeteo API v2, новая v4 не поддерживается. Погоду без токена можно получить через [pywttr](https://github.com/monosans/pywttr).

## In English

pygismeteo is a Python wrapper for the [Gismeteo API](https://gismeteo.ru/api/) with typed responses. The async version is [aiopygismeteo](https://github.com/monosans/aiopygismeteo). The documentation and the rest of this README are in Russian, but the code example below should be easy to follow.

Development is on hold. The author has no Gismeteo API token, so the library isn't tested against the real API. It works with Gismeteo API v2 and doesn't support v4. Gismeteo issues tokens on request at [b2b@gismeteo.ru](mailto:b2b@gismeteo.ru). For weather data without a token, try [pywttr](https://github.com/monosans/pywttr).

## Установка

```bash
uv add pygismeteo pygismeteo-base
# или
pip install -U pygismeteo pygismeteo-base
```

## Пример

```python
import pygismeteo

with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
    city = gismeteo.search.by_query("Москва")[0]
    current = gismeteo.current.by_id(city.id)

print(current.temperature.air.c, current.description.full)
```

В примере стоит образец токена. Свой выдают по запросу на [b2b@gismeteo.ru](mailto:b2b@gismeteo.ru).

## Документация

<https://monosans.github.io/pygismeteo>

## License / Лицензия

[MIT](https://github.com/monosans/pygismeteo/blob/main/LICENSE)
