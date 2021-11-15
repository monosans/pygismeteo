# -*- coding: utf-8 -*-
from typing import Optional

from requests import Session


class HTTPSession:
    def __init__(self, session: Optional[Session]) -> None:
        self.session = session

    @staticmethod
    def fetch(session: Session, endpoint: str) -> bytes:
        with session.get(
            f"https://gismeteo.ru{endpoint}",
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
                + " AppleWebKit/537.36 (KHTML, like Gecko)"
                + " Chrome/95.0.4638.69 Safari/537.36"
            },
        ) as r:
            return r.content

    def req(self, endpoint: str) -> bytes:
        if self.session:
            return self.fetch(self.session, endpoint)
        with Session() as session:
            return self.fetch(session, endpoint)
