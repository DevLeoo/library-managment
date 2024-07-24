from Library import Library
from Books.Book import Book
from Users.User import User
from Users.StudentUserType import StudentUserType
from Users.TeacherUserType import TeacherUserType
from LibraryMediator import LibraryMediator
from typing import List, Optional


class LibraryFacade:
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
            user = StudentUserType(user_id, name)
        elif user_type == "teacher":
            user = TeacherUserType(user_id, name)
        else:
            raise ValueError(f"Invalid user type: {user_type}")
        self.mediator.add_user(user)

    def add_category(self, category_name: str, parent_name: Optional[str] = None) -> None:
        self.mediator.add_category(category_name, parent_name)

    def search_books(self, query: str) -> None:
        results = self.mediator.search_books(query)
        for book in results:
            print(
                f"Title: {book.title}, Author: {book.author}, Category: {book.category}")

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


# # Exemplo de uso do Facade com Mediator
# library_facade = LibraryFacade()

# # Configurações globais
# library_facade.set_configuration("max_borrow_days", 14)
# library_facade.set_configuration("fine_per_day", 0.50)

# max_borrow_days = library_facade.get_configuration("max_borrow_days")
# fine_per_day = library_facade.get_configuration("fine_per_day")

# print(f"Max Borrow Days: {max_borrow_days}")
# print(f"Fine Per Day: ${fine_per_day}")

# # Adicionar categorias, usuários e livros
# library_facade.add_category("Programming")
# library_facade.add_category("Python", "Programming")
# library_facade.add_category("Java", "Programming")
# library_facade.add_category("Data Science")

# library_facade.add_user(1, "John Doe", "student")
# library_facade.add_user(2, "Jane Smith", "teacher")

# library_facade.add_book("Python Programming", "John Doe", "Python")
# library_facade.add_book("Java Essentials", "Jane Smith", "Java")
# library_facade.add_book("Data Science with Python", "Alice Johnson", "Data Science")

# # Buscar livros
# library_facade.search_books("Python")

# # Emprestar livro
# library_facade.borrow_book(1, "Python Programming")
# library_facade.borrow_book(2, "Data Science with Python")

# # Devolver livro
# library_facade.return_book(1, "Python Programming")

# # Imprimir categorias
# library_facade.print_categories()
