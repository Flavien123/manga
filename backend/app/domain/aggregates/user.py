from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    id: int
    username: str
    email: str
    password_hash: str
    role: str 
    avatar_url: str 