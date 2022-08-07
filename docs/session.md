# Свой экземпляр requests.Session

Классу `Gismeteo` можно передать экземпляр `requests.Session`.

Если его не передать, то для каждого запроса будет создаваться новый `requests.Session`.

## Пример

Выводит текущую температуру в географическом объекте с ID 4368 (Москва), используя свой экземпляр `requests.Session`.

```python
from pygismeteo import Gismeteo
from requests import Session

with Session() as session:
    gismeteo = Gismeteo(session=session)
    current = gismeteo.current.by_id(4368)
print(current.temperature.air.c)
```
