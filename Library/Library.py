from Books.ExternalCatalog import ExternalCatalog
from Books.ExternalCatalogAdapter import ExternalCatalogAdapter
from Books.BookAvailabilityNotifier import BookAvailabilityNotifier
from Books.BookAvailabilityHandler import BookAvailabilityHandler
from Books.BookCategory import BookCategory
from Users.User import User
from Users.UserEligibilityHandler import UserEligibilityHandler
from Borrow.BorrowLimitHandler import BorrowLimitHandler
from Config.Global import ConfigurationManager
from typing import List, Optional


class Library:
    def __init__(self):
        self.root_category = BookCategory("Root")
        self.users: List[User] = []
        self.external_catalog_adapter = ExternalCatalogAdapter(
            ExternalCatalog())
        self.configuration_manager = ConfigurationManager()
        self.notifier = BookAvailabilityNotifier()

    def find_all_books(self):
        return self.root_category.books

    def get_configuration(self, key: str) -> any:
        return self.configuration_manager.get_setting(key)

    def set_configuration(self, key: str, value: any) -> None:
        self.configuration_manager.set_setting(key, value)

    def add_user(self, user):
        self.users.append(user)
        self.notifier.subscribe(user)

    def find_user(self, user_id: int) -> Optional[User]:
        return next((user for user in self.users if user.user_id == user_id), None)

    def add_category(self, category_name, parent_name=None):
        new_category = BookCategory(category_name)
        if parent_name is None:
            self.root_category.add_subcategory(new_category)
        else:
            parent_category = self.find_category(
                self.root_category, parent_name)
            if parent_category:
                parent_category.add_subcategory(new_category)

    def find_category(self, current_category, category_name):
        if current_category.name == category_name:
            return current_category
        for subcategory in current_category.subcategories:
            found_category = self.find_category(subcategory, category_name)
            if found_category:
                return found_category
        return None

    def add_book_to_category(self, book, category_name):
        category = self.find_category(self.root_category, category_name)
        if category:
            category.add_book(book)
            self.notifier.notify(
                f"New book arrived in our library: {book.title} by {book.author}")
        else:
            self.add_category(category_name)
            self.root_category.add_book({
                "title": book.title,
                "author": book.author,
                "category": book.category,
                "is_available": book.is_available
            })

    def search_books(self, query):
        results = self.root_category.find_books(query)
        external_results = self.external_catalog_adapter.search(query)
        return results + external_results

    def borrow_book_with_approval(self, user_id: int, book_title: str) -> bool:
        availability_handler = BookAvailabilityHandler()
        eligibility_handler = UserEligibilityHandler(availability_handler)
        limit_handler = BorrowLimitHandler(eligibility_handler)

        return limit_handler.handle_request(user_id, book_title)

    def return_book(self, user_id: int, book_title: str) -> bool:
        user = self.find_user(user_id)
        if not user:
            return False
        book = next(
            (b for b in user.borrowed_books if b.get('title', '').lower() == book_title.lower()), None)
        if book:
            has_returned = user.return_book(book)
            if has_returned:
                self.notifier.notify(
                    f"Book returned: {book.get('title', '')} by {user.name}")
            return has_returned
        return False

    def get_user_history(self, user_id):
        user = self.find_user(user_id)
        if user:
            return {
                "borrowed_books": user.borrowed_books,
                "returned_books": user.returned_books
            }
        return None
