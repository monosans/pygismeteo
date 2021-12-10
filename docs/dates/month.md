# Метод month()

Данный метод класса `Gismeteo` позволяет получать данные с вкладки ["Месяц"](https://gismeteo.ru/weather-moscow-4368/month/).

## Пример, выводящий максимальную температуру в Москве на месяц

```python
import pygismeteo

moscow = pygismeteo.by_url("https://gismeteo.ru/weather-moscow-4368/")
month = moscow.month()
print(month.max_temperature)
```

## Атрибуты

Атрибуты возвращаемого объекта имеют вид `{'день': 'значение'}`.

Полный список атрибутов:

| Атрибут         | Описание                              |
| --------------- | ------------------------------------- |
| status          | Ясно, пасмурно, сильный дождь и т. д. |
| max_temperature | Макс. температура, °C                 |
| min_temperature | Мин. температура, °C                  |
