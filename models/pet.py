from dataclasses import dataclass
from typing import List

from models.category import Category
from models.tag import Tag


@dataclass
class Pet:
    id: int
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tag]
    status: str
