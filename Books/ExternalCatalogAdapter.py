class ExternalCatalogAdapter:
    def __init__(self, external_catalog):
        self.external_catalog = external_catalog

    def search(self, query):
        return self.external_catalog.search_books(query)
