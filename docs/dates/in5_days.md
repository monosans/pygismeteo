# Метод in5_days()

Данный метод класса `Gismeteo` позволяет получать погоду [через 5 дней](https://gismeteo.ru/weather-moscow-4368/5-day/).

## Пример, выводящий температуру в Москве через 5 дней

```python
import pygismeteo

moscow = pygismeteo.by_url("https://gismeteo.ru/weather-moscow-4368/")
in5_days = moscow.in5_days()
print(in5_days.temperature)
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
