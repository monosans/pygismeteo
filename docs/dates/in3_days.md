# Метод in3_days()

Данный метод класса `Gismeteo` позволяет получать погоду [через 3 дня (послезавтра)](https://gismeteo.ru/weather-moscow-4368/3-day/).

## Пример, выводящий температуру в Москве через 3 дня

```python
import pygismeteo

moscow = pygismeteo.by_url("https://gismeteo.ru/weather-moscow-4368/")
in3_days = moscow.in3_days()
print(in3_days.temperature)
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
