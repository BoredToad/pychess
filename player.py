from typing import Any


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.king: Any = None # using any to avoid circular imports :(((
