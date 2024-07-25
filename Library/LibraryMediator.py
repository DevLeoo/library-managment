from typing import List, Optional
from Library import Library
from Books.Book import Book
from Users.User import User


class LibraryMediator:
    def __init__(self, library: Library) -> None:
        self.library = library

    def find_all_books(self) -> List[Book]:
        return self.library.find_all_books()

    def search_books(self, query: str) -> List[Book]:
        return self.library.search_books(query)

    def borrow_book(self, user_id: int, book_title: str) -> bool:
        return self.library.borrow_book(user_id, book_title)

    def return_book(self, user_id: int, book_title: str) -> bool:
        return self.library.return_book(user_id, book_title)

    def add_book_to_category(self, book: Book, category_name: str) -> None:
        self.library.add_book_to_category(book, category_name)

    def add_user(self, user: User) -> None:
        self.library.add_user(user)

    def find_user(self, user_id: str):
        return self.library.find_user(user_id)

    def add_category(self, category_name: str, parent_name: Optional[str] = None) -> None:
        self.library.add_category(category_name, parent_name)

    def get_configuration(self, key: str) -> any:
        return self.library.get_configuration(key)

    def set_configuration(self, key: str, value: any) -> None:
        self.library.set_configuration(key, value)

    def borrow_book_with_approval(self, user_id: int, book_title: str):
        return self.library.borrow_book_with_approval(user_id, book_title)

    def get_user_history(self, user_id: str):
        return self.library.get_user_history(user_id)
