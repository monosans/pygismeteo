# Метод in4_days()

Данный метод класса `Gismeteo` позволяет получать погоду [через 4 дня](https://gismeteo.ru/weather-moscow-4368/4-day/).

## Пример, выводящий температуру в Москве через 4 дня

```python
from pygismeteo import gismeteo

moscow = gismeteo("https://gismeteo.ru/weather-moscow-4368/")
in4_days = moscow.in4_days()
print(in4_days.temperature)
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
