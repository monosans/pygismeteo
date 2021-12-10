# -*- coding: utf-8 -*-
from typing import Optional

from pygismeteo_base.constants import USER_AGENT
from requests import Session


class HTTPSession:
    def __init__(self, session: Optional[Session]) -> None:
        self.session = session

    @staticmethod
    def fetch(session: Session, endpoint: str) -> bytes:
        with session.get(
            f"https://gismeteo.ru{endpoint}",
            headers={"User-Agent": USER_AGENT},
        ) as r:
            return r.content

    def req(self, endpoint: str) -> bytes:
        if self.session:
            return self.fetch(self.session, endpoint)
        with Session() as session:
            return self.fetch(session, endpoint)
