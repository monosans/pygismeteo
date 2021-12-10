# Метод in9_days()

Данный метод класса `Gismeteo` позволяет получать погоду [через 9 дней](https://gismeteo.ru/weather-moscow-4368/9-day/).

## Пример, выводящий температуру в Москве через 9 дней

```python
import pygismeteo

moscow = pygismeteo.by_url("https://gismeteo.ru/weather-moscow-4368/")
in9_days = moscow.in9_days()
print(in9_days.temperature)
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
