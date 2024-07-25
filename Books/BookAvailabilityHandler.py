from Borrow.BorrowRequestHandler import BorrowRequestHandler
from typing import Optional
from .Book import Book
from Library.LibraryMediator import LibraryMediator


class BookAvailabilityHandler(BorrowRequestHandler):
    def handle_request(self, user_id: int, book_title: str) -> bool:
        book = self.get_book_by_title(book_title)
        if not book:
            print(f"Book '{book_title}' not found.")
            return False
        if not book.is_available:
            print(f"Book '{book_title}' is not available.")
            return False
        if self.successor:
            return self.successor.handle_request(user_id, book_title)
        return True

    def get_book_by_title(self, book_title: str) -> Optional[Book]:
        return LibraryMediator().search_books(book_title)[0] if LibraryMediator().search_books(book_title) else None
