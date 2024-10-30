# src/utils/exceptions.py
class LibraryError(Exception):
    """Base exception for library system"""
    pass

class ItemNotFoundError(LibraryError):
    """Raised when an item is not found"""
    pass

class BorrowingLimitError(LibraryError):
    """Raised when a member exceeds borrowing limit"""
    pass