# src/models/member.py
import uuid
from typing import List
from .library_item import LibraryItem

class Member:
    def __init__(self, name: str, email: str):
        self._id = str(uuid.uuid4())
        self._name = name
        self._email = email
        self._borrowed_items: List[LibraryItem] = []

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def borrowed_items(self) -> List[LibraryItem]:
        return self._borrowed_items