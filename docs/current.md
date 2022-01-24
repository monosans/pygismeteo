# Метод current

Данный метод позволяет получить текущую погоду.

## Аргументы

Принимает 1 обязательный аргумент:

- id - ID населённого пункта. О том, как получить ID по названию населённого пункта, см. [Метод get_id_by_query](get_id_by_query.md).

## Пример

Выводит температуру в Москве сейчас.

```python
from pygismeteo import Gismeteo

gm = Gismeteo()
city_id = gm.get_id_by_query("Москва")
current = gm.current(city_id)
print(current.temperature.air.c)
```
