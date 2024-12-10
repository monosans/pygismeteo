# pygismeteo

[![CI](https://github.com/monosans/pygismeteo/actions/workflows/ci.yml/badge.svg)](https://github.com/monosans/pygismeteo/actions/workflows/ci.yml)
[![Downloads](https://static.pepy.tech/badge/pygismeteo)](https://pepy.tech/project/pygismeteo)

Обёртка для [Gismeteo API](https://gismeteo.ru/api/).

Асинхронная версия [здесь](https://github.com/monosans/aiopygismeteo).

## Разработка приостановлена

Для использования библиотеки нужен API токен, который можно запросить по электронной почте [b2b@gismeteo.ru](mailto:b2b@gismeteo.ru).

В настоящее время у разработчика отсутствует API токен, что делает невозможными тестирование и дальнейшую разработку.

Если вам нужна погодная библиотека без API токена, можете рассмотреть <https://github.com/monosans/pywttr>.

## Установка

```bash
pip install -U pygismeteo pygismeteo-base
```

## Документация

<https://pygismeteo.readthedocs.io>

## Пример

```python
with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
    search_results = gismeteo.search.by_query("Москва")
    city_id = search_results[0].id
    current = gismeteo.current.by_id(city_id)
print(current)
```

## License / Лицензия

[MIT](https://github.com/monosans/pygismeteo/blob/main/LICENSE)
