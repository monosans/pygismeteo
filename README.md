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

<https://pygismeteo.readthedocs.io>

## Пример, выводящий температуру в Москве сейчас

```python
from pygismeteo import Gismeteo

gm = Gismeteo()
city_id = gm.get_id_by_query("Москва")
current = gm.current(city_id)
print(current.temperature.air.c)
```
