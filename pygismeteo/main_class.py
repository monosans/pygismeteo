# -*- coding: utf-8 -*-
from pygismeteo.dates.month import Month
from pygismeteo.dates.now import Now
from pygismeteo.dates.one_day import OneDay
from pygismeteo.dates.ten_days import TenDays
from pygismeteo.dates.three_days import ThreeDays
from pygismeteo.dates.two_weeks import TwoWeeks
from pygismeteo.http import req


class Gismeteo:
    def __init__(self, base_endpoint: str) -> None:
        self._base_endpoint = base_endpoint

    def now(self) -> Now:
        """Сейчас."""
        return Now(req(f"{self._base_endpoint}now/"))

    def today(self) -> OneDay:
        """Сегодня."""
        return OneDay(req(self._base_endpoint))

    def tomorrow(self) -> OneDay:
        """Завтра."""
        return OneDay(req(f"{self._base_endpoint}tomorrow/"))

    def in3_days(self) -> OneDay:
        """Через 3 дня (послезавтра)."""
        return OneDay(req(f"{self._base_endpoint}3-day/"))

    def in4_days(self) -> OneDay:
        """Через 4 дня."""
        return OneDay(req(f"{self._base_endpoint}4-day/"))

    def in5_days(self) -> OneDay:
        """Через 5 дней."""
        return OneDay(req(f"{self._base_endpoint}5-day/"))

    def in6_days(self) -> OneDay:
        """Через 6 дней."""
        return OneDay(req(f"{self._base_endpoint}6-day/"))

    def in7_days(self) -> OneDay:
        """Через 7 дней."""
        return OneDay(req(f"{self._base_endpoint}7-day/"))

    def in8_days(self) -> OneDay:
        """Через 8 дней."""
        return OneDay(req(f"{self._base_endpoint}8-day/"))

    def in9_days(self) -> OneDay:
        """Через 9 дней."""
        return OneDay(req(f"{self._base_endpoint}9-day/"))

    def in10_days(self) -> OneDay:
        """Через 10 дней."""
        return OneDay(req(f"{self._base_endpoint}10-day/"))

    def three_days(self) -> ThreeDays:
        """3 дня."""
        return ThreeDays(req(f"{self._base_endpoint}3-days/"))

    def ten_days(self) -> TenDays:
        """10 дней."""
        return TenDays(req(f"{self._base_endpoint}10-days/"))

    def two_weeks(self) -> TwoWeeks:
        """2 недели."""
        return TwoWeeks(req(f"{self._base_endpoint}2-weeks/"))

    def month(self) -> Month:
        """Месяц."""
        return Month(req(f"{self._base_endpoint}month/"))
