# pygismeteo

[![CI](https://github.com/monosans/pygismeteo/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/monosans/pygismeteo/actions/workflows/ci.yml?query=event%3Apush+branch%3Amain)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/monosans/pygismeteo/main.svg)](https://results.pre-commit.ci/latest/github/monosans/pygismeteo/main)
[![Coverage](https://img.shields.io/codecov/c/github/monosans/pygismeteo/main)](https://codecov.io/gh/monosans/pygismeteo)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pygismeteo)](https://pypi.org/project/pygismeteo/)

Обёртка для [Gismeteo API](https://gismeteo.ru/api/).

Асинхронная версия [здесь](https://github.com/monosans/aiopygismeteo).

## Установка

```bash
python -m pip install -U pygismeteo
```

## Документация

[pygismeteo.readthedocs.io](https://pygismeteo.readthedocs.io/)

## Пример, выводящий температуру в Москве сейчас

```python
from pygismeteo import Gismeteo

gismeteo = Gismeteo()
search_results = gismeteo.search.by_query("Москва")
city_id = search_results[0].id
current = gismeteo.current.by_id(city_id)
print(current.temperature.air.c)
```

## License / Лицензия

[MIT](https://github.com/monosans/pygismeteo/blob/main/LICENSE)
