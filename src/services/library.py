# src/services/library.py
from datetime import datetime, timedelta
from typing import List, Optional
from ..models import LibraryItem, Member

class Library:
    def __init__(self):
        self._items: List[LibraryItem] = []
        self._members: List[Member] = []

    def add_item(self, item: LibraryItem) -> None:
        self._items.append(item)
        print(f"{item.get_type()} '{item.title}' added successfully.")

    def add_member(self, member: Member) -> None:
        self._members.append(member)
        print(f"Member {member.name} added successfully.")

    def find_item_by_id(self, item_id: str) -> Optional[LibraryItem]:
        return next((item for item in self._items if item.id == item_id), None)

    def find_member_by_id(self, member_id: str) -> Optional[Member]:
        return next((member for member in self._members if member.id == member_id), None)

    def borrow_item(self, item_id: str, member_id: str) -> None:
        item = self.find_item_by_id(item_id)
        member = self.find_member_by_id(member_id)

        if not item or not member:
            raise ValueError("Item or member not found")

        if not item.is_available:
            raise ValueError(f"'{item.title}' is currently not available")

        if len(member.borrowed_items) >= 3:
            raise ValueError(f"Member {member.name} has reached the maximum borrowing limit")

        item._is_available = False
        item._current_borrower = member
        item._due_date = datetime.now() + timedelta(days=item.get_loan_period())
        member.borrowed_items.append(item)
        
        print(f"{item.get_type()} '{item.title}' borrowed successfully by {member.name}")
        print(f"Due date: {item._due_date.strftime('%Y-%m-%d')}")

    def return_item(self, item_id: str) -> None:
        item = self.find_item_by_id(item_id)
        
        if not item:
            raise ValueError("Item not found")

        if item.is_available:
            raise ValueError(f"'{item.title}' is already available")

        member = item._current_borrower
        member.borrowed_items.remove(item)
        item._is_available = True
        item._current_borrower = None
        item._due_date = None

        print(f"{item.get_type()} '{item.title}' returned successfully")

    def list_available_items(self) -> None:
        available_items = [item for item in self._items if item.is_available]
        if not available_items:
            print("No items available")
            return

        print("\nAvailable Items:")
        for item in available_items:
            print(f"ID: {item.id}")
            print(f"Type: {item.get_type()}")
            print(f"Title: {item.title}")
            print(f"Author: {item.author}")
            print("---")

    def list_members(self) -> None:
        if not self._members:
            print("No members registered")
            return

        print("\nLibrary Members:")
        for member in self._members:
            print(f"ID: {member.id}")
            print(f"Name: {member.name}")
            print(f"Email: {member.email}")
            print("---")

    def list_member_items(self, member_id: str) -> None:
        member = self.find_member_by_id(member_id)
        if not member:
            raise ValueError("Member not found")

        if not member.borrowed_items:
            print(f"{member.name} has no borrowed items")
            return

        print(f"\nItems borrowed by {member.name}:")
        for item in member.borrowed_items:
            print(f"ID: {item.id}")
            print(f"Type: {item.get_type()}")
            print(f"Title: {item.title}")
            print(f"Due Date: {item._due_date.strftime('%Y-%m-%d')}")
            print("---")