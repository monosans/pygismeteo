# Класс Gismeteo

Всё взаимодействие с библиотекой осуществляется через класс Gismeteo:

```python
import pygismeteo

gm = pygismeteo.Gismeteo()
```

## Создание экземпляра класса Gismeteo

При инициализации класс Gismeteo принимает 3 необязательных аргумента:

- lang - язык. По умолчанию "ru".
- token - X-Gismeteo-Token, если используемый по умолчанию перестал работать.
- session - экземпляр requests.Session. Подробнее см. [Свой экземпляр requests.Session](session.md).
