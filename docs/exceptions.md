# Исключения (exceptions)

При вызове функций `pygismeteo.by_name` или `pygismeteo.by_url` может возникнуть исключение `LocalityError`.

1. При использовании `by_name` исключение возникает, если указан несуществующий населённый пункт, например:
   ```python
   gm = pygismeteo.by_name("алыфдаождваолыфволадф")
   ```
2. При использовании `by_url` исключение возникает, если количество ссылок не равно `1`, например:
   ```python
   gm = pygismeteo.by_url("алыфдаождваолыфволадф")
   ```

## Пример обработки исключений

В этом примере пользователь вводит название населённого пункта, и программа выводит температуру на данный момент в указанном населённом пункте. Если пользователь введёт неверное название, он получит сообщение об этом.

```python
import pygismeteo
from pygismeteo.exceptions import LocalityError

locality = input("Название населённого пункта: ")
try:
    gm = pygismeteo.by_name(locality)
except LocalityError:
    print("Населённый пункт не найден")
else:
    now = gm.now()
    print(now.temperature)
```
