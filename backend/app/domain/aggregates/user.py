from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    id: int
    username: str
    email: str
    password_hash: str
    role: str = "user"
    avatar_url: str = ""
    lists: dict[str, List[int]] = field(default_factory=dict) # e.g. {"reading": [1, 2], "completed": [3]}

    def add_to_list(self, list_name: str, manga_id: int):
        if list_name not in self.lists:
            self.lists[list_name] = []
        if manga_id not in self.lists[list_name]:
            self.lists[list_name].append(manga_id)
            
    def remove_from_list(self, list_name: str, manga_id: int):
        if list_name in self.lists and manga_id in self.lists[list_name]:
            self.lists[list_name].remove(manga_id)
