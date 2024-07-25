from abc import abstractmethod
from typing import List, Optional
from Books.Book import Book
from Books.BookAvailabilityNotifier import Observer


class User(Observer):
    def __init__(self, user_id: int, name: str, user_type: str) -> None:
        self.user_id = user_id
        self.name = name
        self.user_type = user_type
        self.borrowed_books: List[Book] = []

    @abstractmethod
    def borrow_limit(self) -> int:
        pass

    def update(self, message: str) -> None:
        print(f"Notification for {self.name}: {message}")

    def borrow_book(self, book: Book) -> bool:
        if len(self.borrowed_books) < self.borrow_limit() and book.get("is_available", False):
            self.borrowed_books.append(book)
            book["is_available"] = False
            return True
        return False

    def has_reached_borrow_limit(self):
        return self.borrow_limit() < len(self.borrowed_books)

    def return_book(self, book: Book) -> bool:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book['is_available'] = True
            return True
        return False
