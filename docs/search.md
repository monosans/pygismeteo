# Получение ID населённого пункта по названию

При поиске может возникнуть исключение `LocalityNotFound`. Подробнее см. [Исключения](exceptions.md)

В этом примере `city_id` - ID Москвы.

```python
import pygismeteo

city_id = pygismeteo.search.id_by_query("Москва")
gm = pygismeteo.current(city_id)
print(gm.temperature.air.c)
```
