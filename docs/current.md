# Атрибут current

## Метод by_id

Текущая погода по ID географического объекта.

Принимает 1 аргумент:

- id (int ≥ 1): ID географического объект. Получить можно через [Поиск](search.md).

Возвращает `pygismeteo.models.current.Model`.

## Метод by_coordinates

Текущая погода по координатам.

Принимает 2 аргумента:

- latitude (-90 ≤ float ≤ 90): Широта.
- longitude (-180 ≤ float ≤ 180): Долгота.

Возвращает `pygismeteo.models.current.Model`.

## Пример

Выводит температуру в Москве сейчас.

```python
import pygismeteo

gm = pygismeteo.Gismeteo()
search_results = gm.search.by_query("Москва")
city_id = search_results[0].id
current = gm.current.by_id(city_id)
print(current.temperature.air.c)
```
