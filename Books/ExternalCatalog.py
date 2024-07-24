class ExternalCatalog:
    def search_books(self, query):
        external_data = [
            {"title": "Python Programming",
                "author": "John Doe", "category": "Programming"},
            {"title": "Java Essentials", "author": "Jane Smith",
                "category": "Programming"},
            {"title": "Data Science with Python",
                "author": "Alice Johnson", "category": "Data Science"},
        ]
        return [book for book in external_data if query.lower() in book["title"].lower()]
