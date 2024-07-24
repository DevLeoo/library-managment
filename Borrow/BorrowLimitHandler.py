from BorrowRequestHandler import BorrowRequestHandler
from typing import Optional
from Library.LibraryMediator import LibraryMediator
from Users.User import User


class BorrowLimitHandler(BorrowRequestHandler):
    def handle_request(self, user_id: int, book_title: str) -> bool:
        user = self.get_user_by_id(user_id)
        if not user:
            print(f"User ID '{user_id}' not found.")
            return False
        if user.has_reached_loan_limit():
            print(f"User '{user_id}' cannot borrow. Borrow limit checked")
            return False
        self.borrow_book(user_id, book_title)
        return True

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return LibraryMediator().find_user(user_id)

    def borrow_book(self, user_id: int, book_title: str) -> None:
        library_system = LibraryMediator()
        book = library_system.search_books(book_title)[0]
        if book:
            user = self.get_user_by_id(user_id)
            if user:
                user.borrow_book(book)
                print(
                    f"Book '{book_title}' successfully borrowed by user '{user_id}'.")
