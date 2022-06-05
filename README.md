# pygismeteo

[![Build Status](https://github.com/monosans/pygismeteo/workflows/test/badge.svg?branch=main&event=push)](https://github.com/monosans/pygismeteo/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/monosans/pygismeteo/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/pygismeteo)

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

gm = Gismeteo()
search_results = gm.search.by_query("Москва")
city_id = search_results[0].id
current = gm.current.by_id(city_id)
print(current.temperature.air.c)
```

## License / Лицензия

[MIT](https://github.com/monosans/pygismeteo/blob/main/LICENSE)
