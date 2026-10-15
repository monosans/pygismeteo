# pygismeteo

[![Downloads](https://static.pepy.tech/badge/pygismeteo)](https://pepy.tech/project/pygismeteo)

Обёртка для [Gismeteo API](https://gismeteo.ru/api/) на Python с типизированными ответами. Асинхронная версия называется [aiopygismeteo](https://github.com/monosans/aiopygismeteo).

Разработка приостановлена: у разработчика нет токена Gismeteo API, поэтому библиотека не проверяется на реальном API. Работает с Gismeteo API v2, новая v4 не поддерживается. Погоду без токена можно получить через [pywttr](https://github.com/monosans/pywttr).

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

Токен выдают по запросу на [b2b@gismeteo.ru](mailto:b2b@gismeteo.ru).

## Документация

<https://monosans.github.io/pygismeteo>

## License / Лицензия

[MIT](https://github.com/monosans/pygismeteo/blob/main/LICENSE)
