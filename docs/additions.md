# Дополнительные возможности

## Свой экземпляр requests.Session

Данный пример выводит температуру в Москве сегодня.

```python
from pygismeteo import gismeteo
from requests import Session

with Session() as s:
    moscow = gismeteo("https://gismeteo.ru/weather-moscow-4368/", session=s)
    today = moscow.today()
print(today.temperature)
```
