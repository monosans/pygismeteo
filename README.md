# pygismeteo

[![Build Status](https://github.com/monosans/pygismeteo/workflows/test/badge.svg?branch=main&event=push)](https://github.com/monosans/pygismeteo/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/monosans/pygismeteo/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/pygismeteo)
[![Python Version](https://img.shields.io/pypi/pyversions/pygismeteo.svg)](https://pypi.org/project/pygismeteo/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/monosans/pygismeteo/blob/main/LICENSE)

Обёртка для [Gismeteo.ru API](https://gismeteo.ru/api).

Асинхронная версия [здесь](https://github.com/monosans/aiopygismeteo).

## Установка

```bash
python -m pip install -U pygismeteo
```

## Документация

Релизная версия - <https://pygismeteo.readthedocs.io>

Git версия - <https://pygismeteo.readthedocs.io/ru/latest>

## Пример, выводящий температуру в Москве сейчас

```python
import pygismeteo

city_id = pygismeteo.search.id_by_query("Москва")
gm = pygismeteo.current(city_id)
print(gm.temperature.air.c)
```
