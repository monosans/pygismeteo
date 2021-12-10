# Свой экземпляр requests.Session

Данный пример выводит температуру в Москве сегодня.

```python
import pygismeteo
from requests import Session

with Session() as s:
    moscow = pygismeteo.by_url(
        "https://gismeteo.ru/weather-moscow-4368/", session=s
    )
    today = moscow.today()
print(today.temperature)
```
