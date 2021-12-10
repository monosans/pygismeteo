# Метод in6_days()

Данный метод класса `Gismeteo` позволяет получать погоду [через 6 дней](https://gismeteo.ru/weather-moscow-4368/6-day/).

## Пример, выводящий температуру в Москве через 6 дней

```python
import pygismeteo

moscow = pygismeteo.by_url("https://gismeteo.ru/weather-moscow-4368/")
in6_days = moscow.in6_days()
print(in6_days.temperature)
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
