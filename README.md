# pygismeteo

[![Build Status](https://github.com/monosans/pygismeteo/workflows/test/badge.svg?branch=main&event=push)](https://github.com/monosans/pygismeteo/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/monosans/pygismeteo/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/pygismeteo)
[![Python Version](https://img.shields.io/pypi/pyversions/pygismeteo.svg)](https://pypi.org/project/pygismeteo/)

Обёртка для [Gismeteo.ru](https://gismeteo.ru).

Асинхронная версия [здесь](https://github.com/monosans/aiopygismeteo).

## Установка

```sh
python -m pip install -U pygismeteo
```

## Документация

Для текущей релизной версии - https://pygismeteo.readthedocs.io

Для git версии - https://pygismeteo.readthedocs.io/ru/latest

## Пример, выводящий температуру в Москве сейчас

```python
from pygismeteo import gismeteo

moscow = gismeteo("Москва")
now = moscow.now()
print(now.temperature)
```

## License / Лицензия

[MIT](LICENSE)
