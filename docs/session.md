# Свой экземпляр requests.Session

Данный пример выводит текущую температуру в населённом пункте с ID 4368 (Москва).

```python
import pygismeteo
from requests import Session

with Session() as s:
    gm = pygismeteo.current(4368, session=s)
print(gm.temperature.air.c)
```
