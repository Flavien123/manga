from dataclasses import dataclass
from ..value_objects.page import Page

@dataclass
class Chapter:
    id: int
    manga_id: int
    title: str
    number: float
    volume: int
    pages: list[Page]
    created_at: str
