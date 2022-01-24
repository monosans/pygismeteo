# Класс Gismeteo

Чтобы начать работу с библиотекой, делаем следующий импорт:

```python
from pygismeteo import Gismeteo
```

## Создание экземпляра класса Gismeteo

При инициализации класс Gismeteo принимает 3 необязательных аргумента:

- lang - язык. По умолчанию "ru".
- token - X-Gismeteo-Token, если используемый по умолчанию перестал работать.
- session - экземпляр requests.Session. Подробнее см. [Свой экземпляр requests.Session](session.md).
