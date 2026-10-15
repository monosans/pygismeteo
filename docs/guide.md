# Руководство

Примеры запускаются как есть, нужен только [токен](index.md). В примерах стоит образец токена, замените его своим. Пример с `base_url` требует ещё адрес вашего прокси.

## Найти город по названию

[`search.by_query`][pygismeteo.types.Search.by_query] ищет города, районы, страны и аэропорты. Если ничего не найдено, вернётся пустой кортеж.

```python
import pygismeteo

with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
    results = gismeteo.search.by_query("Москва")

for place in results:
    print(place.id, place.name, place.country.name)
```

`id` из результата нужен для запросов погоды по ID.

## Найти места рядом с точкой

[`search.by_coordinates`][pygismeteo.types.Search.by_coordinates] возвращает ближайшие к точке географические объекты, не больше `limit` (от 1 до 36).

```python
import pygismeteo

with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
    results = gismeteo.search.by_coordinates(55.75222, 37.61556, limit=5)

for place in results:
    print(place.name, place.distance)
```

## Определить город по IP

```python
from ipaddress import IPv4Address

import pygismeteo

with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
    place = gismeteo.search.by_ip(IPv4Address("8.8.8.8"))

print(place.id, place.name, place.country.name)
```

## Текущая погода

[`current.by_id`][pygismeteo.types.Current.by_id] принимает ID из поиска, а [`current.by_coordinates`][pygismeteo.types.Current.by_coordinates] принимает широту и долготу.

```python
import pygismeteo

with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
    current = gismeteo.current.by_id(4368)  # Москва

print(current.description.full)
print("Температура:", current.temperature.air.c, "°C")
print("Ощущается как:", current.temperature.comfort.c, "°C")
print("Ветер:", current.wind.speed.m_s, "м/с")
print("Влажность:", current.humidity.percent, "%")
print("Давление:", current.pressure.mm_hg_atm, "мм рт. ст.")
```

Все поля ответа описаны в [`models.current.Model`][pygismeteo.models.current.Model].

## Прогноз по дням

[`step24`][pygismeteo.types.Step24] даёт прогноз на срок от 3 до 10 дней, по элементу на сутки с суточными минимумами и максимумами.

```python
import pygismeteo

with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
    forecast = gismeteo.step24.by_id(4368, days=3)

for day in forecast:
    air = day.temperature.air
    print(day.date.local, air.min.c, air.max.c, day.description.full)
```

## Прогноз по часам

[`step3`][pygismeteo.types.Step3] даёт прогноз с шагом 3 часа на срок от 1 до 10 дней, а [`step6`][pygismeteo.types.Step6] с шагом 6 часов на срок от 3 до 10 дней. Ответы у них устроены одинаково.

```python
import pygismeteo

with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
    forecast = gismeteo.step3.by_id(4368, days=1)

for item in forecast:
    print(item.date.local, item.temperature.air.c, item.description.full)
```

## Облачность, осадки и ветер словами

У значений облачности, осадков, направления ветра и других [перечислений][pygismeteo.models.enums] есть поле `description` с описанием на русском и английском.

```python
import pygismeteo

with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
    current = gismeteo.current.by_id(4368)

print(current.cloudiness.type.description.ru)
print(current.precipitation.type.description.ru)
print(current.gm.description.en)
if current.wind.direction.scale_8 is not None:
    print(current.wind.direction.scale_8.description.ru)
```

## Язык ответов

По умолчанию названия и описания приходят на русском. Другой язык задаёт [`Lang`][pygismeteo.types.Lang].

```python
import pygismeteo

with pygismeteo.Gismeteo(
    token="56b30cb255.3443075", lang=pygismeteo.types.Lang.EN
) as gismeteo:
    current = gismeteo.current.by_id(4368)

print(current.description.full)
```

## Таймауты и свой HTTP-клиент

Свой [`httpx2.Client`][httpx2.Client] нужен, чтобы задать таймауты или прокси. По умолчанию таймаут 60 секунд, на подключение 5 секунд.

```python
import httpx2

import pygismeteo

with httpx2.Client(
    timeout=httpx2.Timeout(10, connect=3), follow_redirects=True
) as session:
    gismeteo = pygismeteo.Gismeteo(token="56b30cb255.3443075", session=session)
    current = gismeteo.current.by_id(4368)

print(current.description.full)
```

!!! warning

    [`Gismeteo.close`][pygismeteo.Gismeteo.close] и выход из `with pygismeteo.Gismeteo(...)` закрывают и переданный клиент. Если он нужен дальше, не используйте `Gismeteo` как контекстный менеджер.

## Другой адрес API

Параметр `base_url` пригодится, если перед API стоит ваш прокси. Замените `https://api.example.com/v2` в примере его адресом. По умолчанию используется `https://api.gismeteo.net/v2`.

```python
import pydantic

import pygismeteo

with pygismeteo.Gismeteo(
    token="56b30cb255.3443075",
    base_url=pydantic.AnyHttpUrl("https://api.example.com/v2"),
) as gismeteo:
    current = gismeteo.current.by_id(4368)

print(current.description.full)
```

## Обработка ошибок

Если API ответил кодом ошибки, поднимается [`httpx2.HTTPStatusError`][httpx2.HTTPStatusError]. При сбое сети или таймауте поднимается [`httpx2.RequestError`][httpx2.RequestError]. Аргументы вне допустимых границ и ответ неожиданной формы приводят к [`pydantic.ValidationError`][pydantic_core.ValidationError].

```python
import httpx2
import pydantic

import pygismeteo

with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
    try:
        forecast = gismeteo.step24.by_id(4368, days=10)
    except httpx2.HTTPStatusError as e:
        print("Ошибка API:", e.response.status_code)
    except httpx2.RequestError as e:
        print("Сеть недоступна:", e)
    except pydantic.ValidationError as e:
        print("Неверные данные:", e)
    else:
        print(len(forecast), "дней")
```

## Аннотации типов

Модели ответов лежат в `pygismeteo.models`, например [`models.current.Model`][pygismeteo.models.current.Model]. Типы аргументов лежат в `pygismeteo.types`, например [`LocalityID`][pygismeteo.types.LocalityID]. Модели неизменяемые и хешируемые.

```python
import pygismeteo


def summary(weather: pygismeteo.models.current.Model) -> str:
    return f"{weather.temperature.air.c} °C, {weather.description.full}"


def fetch(city_id: pygismeteo.types.LocalityID) -> str:
    with pygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        return summary(gismeteo.current.by_id(city_id))


print(fetch(4368))
```
