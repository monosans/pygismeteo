# Метод in10_days()

Данный метод класса `Gismeteo` позволяет получать погоду [через 10 дней](https://gismeteo.ru/weather-moscow-4368/10-day/).

## Пример, выводящий температуру в Москве через 10 дней

```python
from pygismeteo import gismeteo

moscow = gismeteo("https://gismeteo.ru/weather-moscow-4368/")
in10_days = moscow.in10_days()
print(in10_days.temperature)
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
