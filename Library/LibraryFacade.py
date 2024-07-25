from .Library import Library
from Books.Book import Book
from Users.StudentUserType import StudentUserType
from Users.TeacherUserType import TeacherUserType
from .LibraryMediator import LibraryMediator
from typing import Optional


class LibraryFacade:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LibraryFacade, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.library = Library()
        self.mediator = LibraryMediator(self.library)

    def set_configuration(self, key: str, value: any) -> None:
        self.mediator.set_configuration(key, value)

    def get_configuration(self, key: str) -> any:
        return self.mediator.get_configuration(key)

    def add_book(self, title: str, author: str, category: str) -> None:
        book = Book(title, author, category)
        self.mediator.add_book_to_category(book, category)

    def add_user(self, user_id: int, name: str, user_type: str) -> None:
        if user_type == "student":
            user = StudentUserType(user_id, name, user_type)
        elif user_type == "teacher":
            user = TeacherUserType(user_id, name, user_type)
        else:
            raise ValueError(f"Invalid user type: {user_type}")
        self.mediator.add_user(user)

    def find_user(self, user_id: str):
        user = self.mediator.find_user(user_id)
        if user:
            return user
        else:
            return []

    def add_category(self, category_name: str, parent_name: Optional[str] = None) -> None:
        self.mediator.add_category(category_name, parent_name)

    def find_all_Books(self) -> None:
        return self.mediator.find_all_books()

    def search_books(self, query: str) -> None:
        results = self.mediator.search_books(query)
        for book in results:
            print(
                f"Title: {book.get('title', '')}, Author: {book.get('author', '')}, Category: {book.get('category', '')}")
        return results

    def borrow_book(self, user_id: int, book_title: str) -> None:
        success = self.mediator.borrow_book_with_approval(user_id, book_title)
        if success:
            print(f"Book '{book_title}' borrowed successfully.")
        else:
            print(f"Failed to borrow book '{book_title}'.")

    def return_book(self, user_id: int, book_title: str) -> None:
        success = self.mediator.return_book(user_id, book_title)
        if success:
            print(f"Book '{book_title}' returned successfully.")
        else:
            print(f"Failed to return book '{book_title}'.")

    def print_categories(self):
        self.library_system.print_categories()


LibraryFacadeSingleton = LibraryFacade()
