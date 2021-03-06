# Свой экземпляр requests.Session

Классу `Gismeteo` можно передать экземпляр `requests.Session`.

Если его не передать, то для каждого запроса будет создаваться новый `requests.Session`, что понижает производительность.

## Пример

Выводит текущую температуру в географическом объекте с ID 4368 (Москва), используя свой экземпляр `requests.Session`.

```python
from pygismeteo import Gismeteo
from requests import Session

with Session() as s:
    gm = Gismeteo(session=s)
    current = gm.current.by_id(4368)
print(current.temperature.air.c)
```
