# src/models/magazine.py
from .library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title: str, author: str, issue_number: str):
        super().__init__(title, author)
        self._issue_number = issue_number

    def get_loan_period(self) -> int:
        return 7

    def get_type(self) -> str:
        return "Magazine"