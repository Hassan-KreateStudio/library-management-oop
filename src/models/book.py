# src/models/book.py
from .library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title: str, author: str, isbn: str, pages: int):
        super().__init__(title, author)
        self._isbn = isbn
        self._pages = pages

    def get_loan_period(self) -> int:
        return 14

    def get_type(self) -> str:
        return "Book"

    @property
    def isbn(self) -> str:
        return self._isbn