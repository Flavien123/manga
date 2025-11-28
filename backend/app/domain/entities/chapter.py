from dataclasses import dataclass

@dataclass
class Chapter:
    id: int
    manga_id: int
    title: str
    number: float
    volume: int
    pages: list[str] # List of image URLs
    created_at: str
