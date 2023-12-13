# Свой экземпляр requests.Session

Классу `Gismeteo` можно передать экземпляр `requests.Session`.

Если его не передать, то для каждого запроса будет создаваться новый `requests.Session`.

## Пример

Выводит текущую температуру в географическом объекте с ID 4368 (Москва), используя свой экземпляр `requests.Session`.

```python
import pygismeteo
from requests import Session

with Session() as session:
    gm = pygismeteo.Gismeteo(token="56b30cb255.3443075", session=session)
    current = gm.current.by_id(4368)
print(current.temperature.air.c)
```
