# pygismeteo

[![CI](https://github.com/monosans/pygismeteo/actions/workflows/ci.yml/badge.svg)](https://github.com/monosans/pygismeteo/actions/workflows/ci.yml)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pygismeteo?logo=pypi)](https://pypi.org/project/pygismeteo/)

Обёртка для [Gismeteo API](https://gismeteo.ru/api/).

Асинхронная версия [здесь](https://github.com/monosans/aiopygismeteo).

## Установка

```bash
python -m pip install -U pygismeteo pygismeteo-base
```

## Документация

<https://pygismeteo.readthedocs.io/>

## Пример, выводящий температуру в Москве сейчас

```python
import pygismeteo

gm = pygismeteo.Gismeteo()
search_results = gm.search.by_query("Москва")
city_id = search_results[0].id
current = gm.current.by_id(city_id)
print(current.temperature.air.c)
```

## License / Лицензия

[MIT](https://github.com/monosans/pygismeteo/blob/main/LICENSE)
