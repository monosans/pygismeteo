# Атрибут step6

## Метод by_id

Погода с шагом 6 часов по ID географического объекта.

Принимает 2 аргумента:

- id (int) - ID географического объекта (получить можно через [Поиск](search.md)).
- days (int) - количество дней (от 3 до 10).

## Метод by_coordinates

Погода с шагом 6 часов по координатам.

Принимает 3 аргумента:

- latitude (float) - широта (от -90 до 90).
- longitude (float) - долгота (от -180 до 180).
- days (int) - количество дней (от 3 до 10).

## Возвращаемый объект

Оба метода возвращают `List[pygismeteo_base.models.step6.ModelItem]`. За каждый день, указанный в аргументах, в возвращаемый список добавляется 4 элемента. Например, если days=3, список будет состоять из 4\*3=12 элементов.

## Пример

Выводит температуру в Москве послезавтра в 09:00 часов.

```python
from pygismeteo import Gismeteo

gm = Gismeteo()
search_results = gm.search.by_query("Москва")
city_id = search_results[0].id
step6 = gm.step6.by_id(city_id, days=3)
print(step6[9].temperature.air.c)
```
