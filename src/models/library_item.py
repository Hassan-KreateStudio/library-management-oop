# src/models/library_item.py
from abc import ABC, abstractmethod
from datetime import datetime
import uuid
from typing import Optional

class LibraryItem(ABC):
    def __init__(self, title: str, author: str):
        self._id = str(uuid.uuid4())
        self._title = title
        self._author = author
        self._is_available = True
        self._current_borrower = None
        self._due_date = None

    @property
    def id(self) -> str:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def is_available(self) -> bool:
        return self._is_available

    @abstractmethod
    def get_loan_period(self) -> int:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass