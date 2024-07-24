from Library.LibraryMediator import LibraryMediator
from typing import Optional
from User import User
from Borrow.BorrowRequestHandler import BorrowRequestHandler


class UserEligibilityHandler(BorrowRequestHandler):
    def handle_request(self, user_id: int, book_title: str) -> bool:
        user = self.get_user_by_id(user_id)
        if not user:
            print(f"User with ID '{user_id}' not found.")
            return False
        if not user.is_eligible_for_loan():
            print(f"User '{user_id}' is not eligible for loan.")
            return False
        if self.successor:
            return self.successor.handle_request(user_id, book_title)
        return True

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return LibraryMediator().find_user(user_id)
