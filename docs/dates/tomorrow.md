# Метод tomorrow()

Данный метод класса `Gismeteo` позволяет получать данные с вкладки ["tomorrow"](https://gismeteo.ru/weather-moscow-4368/tomorrow/).

## Пример, выводящий температуру в Москве завтра

```python
from pygismeteo import gismeteo

moscow = gismeteo("https://gismeteo.ru/weather-moscow-4368/")
tomorrow = moscow.tomorrow()
print(tomorrow.temperature)
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
