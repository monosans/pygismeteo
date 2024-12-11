from __future__ import annotations

from typing import Final, Optional

from httpx import Client
from pydantic import AnyHttpUrl, validate_call
from pygismeteo_base.types import Lang
from typing_extensions import Self, final

from pygismeteo._endpoints.current import Current
from pygismeteo._endpoints.search import Search
from pygismeteo._endpoints.step3 import Step3
from pygismeteo._endpoints.step6 import Step6
from pygismeteo._endpoints.step24 import Step24
from pygismeteo._http import HttpxClient


@final
class Gismeteo:
    """Обёртка для Gismeteo API.

    Examples:
        ```python
        with gismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
            search_results = gismeteo.search.by_query("Москва")
            city_id = search_results[0].id
            current = gismeteo.current.by_id(city_id)
        print(current)
        ```

        Кастомный базовый URL:

        ```python
        with gismeteo.Gismeteo(
            token=...,
            base_url=pydantic.AnyHttpUrl("https://api.example.com/v1"),
        ) as gismeteo:
            ...
        ```

        Другой язык:

        ```python
        with gismeteo.Gismeteo(token=..., lang=gismeteo.Lang.EN) as gismeteo:
            ...
        ```

        Кастомный httpx.Client:

        ```python
        with httpx.Client(timeout=300, follow_redirects=True) as session:
            gismeteo = gismeteo.Gismeteo(token=..., session=session)
            ...
        ```
    """

    __slots__ = (
        "_current",
        "_search",
        "_session",
        "_step3",
        "_step6",
        "_step24",
    )

    @validate_call(config={"arbitrary_types_allowed": True})
    def __init__(
        self,
        *,
        token: str,
        base_url: AnyHttpUrl = AnyHttpUrl.build(  # noqa: B008
            scheme="https", host="api.gismeteo.net", path="v2"
        ),
        lang: Lang = Lang.RU,
        session: Optional[Client] = None,
    ) -> None:
        """Обёртка для Gismeteo API.

        Args:
            token:
                X-Gismeteo-Token.
                Запросить можно по электронной почте
                [b2b@gismeteo.ru](mailto:b2b@gismeteo.ru).

        Examples:
            ```python
            with gismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
                search_results = gismeteo.search.by_query("Москва")
                city_id = search_results[0].id
                current = gismeteo.current.by_id(city_id)
            print(current)
            ```

            Кастомный базовый URL:

            ```python
            with gismeteo.Gismeteo(
                token=...,
                base_url=pydantic.AnyHttpUrl("https://api.example.com/v1"),
            ) as gismeteo:
                ...
            ```

            Другой язык:

            ```python
            with gismeteo.Gismeteo(
                token=..., lang=gismeteo.Lang.EN
            ) as gismeteo:
                ...
            ```

            Кастомный httpx.Client:

            ```python
            with httpx.Client(timeout=300, follow_redirects=True) as session:
                gismeteo = gismeteo.Gismeteo(token=..., session=session)
                ...
            ```
        """
        self._session: Final = HttpxClient(
            token=token, base_url=base_url, lang=lang, session=session
        )
        self._current: Final = Current(self._session)
        self._search: Final = Search(self._session)
        self._step3: Final = Step3(self._session)
        self._step6: Final = Step6(self._session)
        self._step24: Final = Step24(self._session)

    @property
    def current(self) -> Current:
        """Текущая погода."""
        return self._current

    @property
    def search(self) -> Search:
        """Поиск."""
        return self._search

    @property
    def step3(self) -> Step3:
        """Погода с шагом 3 часа."""
        return self._step3

    @property
    def step6(self) -> Step6:
        """Погода с шагом 6 часа."""
        return self._step6

    @property
    def step24(self) -> Step24:
        """Погода с шагом 24 часов."""
        return self._step24

    @property
    def token(self) -> str:
        """X-Gismeteo-Token."""
        return self._session.token.get_secret_value()

    @property
    def base_url(self) -> AnyHttpUrl:
        return self._session.base_url

    @property
    def lang(self) -> Lang:
        return self._session.lang

    @property
    def session(self) -> Optional[Client]:
        return self._session.session

    def close(self) -> None:
        """Закрыть HTTP сессию."""
        if self._session.session is not None:
            self._session.session.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
