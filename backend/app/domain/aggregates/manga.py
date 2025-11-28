from dataclasses import dataclass

from src.domain.entities.chapter import Chapter
from src.domain.entities.genre import Genre
from src.domain.entities.tag import Tag
from src.domain.entities.artist import Artist
from src.domain.entities.author import Author

@dataclass
class Manga:
    id: int
    title: str
    description: str
    year: int
    rating: float
    original: str
    manga_status: str
    translation_status: str
    authors: list[Author]
    artists: list[Artist]
    genres: list[Genre]
    tags: list[Tag]
    chapters: list[Chapter]
    created_at: str