class BookCategory:
    def __init__(self, name):
        self.name = name
        self.subcategories = []
        self.books = []

    def add_subcategory(self, subcategory):
        self.subcategories.append(subcategory)

    def add_book(self, book):
        self.books.append(book)

    def find_books(self, query):
        results = [book for book in self.books if query.lower()
                   in book.title.lower()]
        for subcategory in self.subcategories:
            results.extend(subcategory.find_books(query))
        return results

    def print_category(self, level=0):
        indent = " " * (level * 4)
        print(f"{indent}Category: {self.name}")
        for book in self.books:
            print(f"{indent}  Book: {book.title} by {book.author}")
        for subcategory in self.subcategories:
            subcategory.print_category(level + 1)
