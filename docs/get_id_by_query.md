# Метод get_id_by_query

Вспомогательный метод, позволяющий получить ID по названию населённого пункта.

При поиске может возникнуть исключение `LocalityNotFound`. Подробнее см. [Исключения](exceptions.md).

## Пример

В этом примере `city_id` - ID Москвы.

```python
from pygismeteo import Gismeteo

gm = Gismeteo()
city_id = gm.get_id_by_query("Москва")
current = gm.current(city_id)
print(current.temperature.air.c)
```
