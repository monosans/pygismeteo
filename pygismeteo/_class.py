# -*- coding: utf-8 -*-
from pygismeteo_base.dates.month import Month
from pygismeteo_base.dates.now import Now
from pygismeteo_base.dates.one_day import (
    In3Days,
    In4Days,
    In5Days,
    In6Days,
    In7Days,
    In8Days,
    In9Days,
    In10Days,
    Today,
    Tomorrow,
)
from pygismeteo_base.dates.ten_days import TenDays
from pygismeteo_base.dates.three_days import ThreeDays
from pygismeteo_base.dates.two_weeks import TwoWeeks
from pygismeteo._http import HTTPSession


class Gismeteo:
    """Возвращается фабрикой gismeteo()."""

    def __init__(self, base_endpoint: str, session: HTTPSession) -> None:
        self._BASE_ENDPOINT = base_endpoint
        self._session = session

    def now(self) -> Now:
        """Сейчас."""
        return Now(self._session.req(f"{self._BASE_ENDPOINT}now/"))

    def today(self) -> Today:
        """Сегодня."""
        return Today(self._session.req(self._BASE_ENDPOINT))

    def tomorrow(self) -> Tomorrow:
        """Завтра."""
        return Tomorrow(self._session.req(f"{self._BASE_ENDPOINT}tomorrow/"))

    def in3_days(self) -> In3Days:
        """Через 3 дня (послезавтра)."""
        return In3Days(self._session.req(f"{self._BASE_ENDPOINT}3-day/"))

    def in4_days(self) -> In4Days:
        """Через 4 дня."""
        return In4Days(self._session.req(f"{self._BASE_ENDPOINT}4-day/"))

    def in5_days(self) -> In5Days:
        """Через 5 дней."""
        return In5Days(self._session.req(f"{self._BASE_ENDPOINT}5-day/"))

    def in6_days(self) -> In6Days:
        """Через 6 дней."""
        return In6Days(self._session.req(f"{self._BASE_ENDPOINT}6-day/"))

    def in7_days(self) -> In7Days:
        """Через 7 дней."""
        return In7Days(self._session.req(f"{self._BASE_ENDPOINT}7-day/"))

    def in8_days(self) -> In8Days:
        """Через 8 дней."""
        return In8Days(self._session.req(f"{self._BASE_ENDPOINT}8-day/"))

    def in9_days(self) -> In9Days:
        """Через 9 дней."""
        return In9Days(self._session.req(f"{self._BASE_ENDPOINT}9-day/"))

    def in10_days(self) -> In10Days:
        """Через 10 дней."""
        return In10Days(self._session.req(f"{self._BASE_ENDPOINT}10-day/"))

    def three_days(self) -> ThreeDays:
        """3 дня."""
        return ThreeDays(self._session.req(f"{self._BASE_ENDPOINT}3-days/"))

    def ten_days(self) -> TenDays:
        """10 дней."""
        return TenDays(self._session.req(f"{self._BASE_ENDPOINT}10-days/"))

    def two_weeks(self) -> TwoWeeks:
        """2 недели."""
        return TwoWeeks(self._session.req(f"{self._BASE_ENDPOINT}2-weeks/"))

    def month(self) -> Month:
        """Месяц."""
        return Month(self._session.req(f"{self._BASE_ENDPOINT}month/"))
