# Метод in7_days()

Данный метод класса `Gismeteo` позволяет получать погоду [через 7 дней](https://gismeteo.ru/weather-moscow-4368/7-day/).

## Пример, выводящий температуру в Москве через 7 дней

```python
import pygismeteo

moscow = pygismeteo.by_url("https://gismeteo.ru/weather-moscow-4368/")
in7_days = moscow.in7_days()
print(in7_days.temperature)
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
