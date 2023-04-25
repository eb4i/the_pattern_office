from tpo.domain.base_data_entity import BaseDataEntity

class DataDomain(BaseDataEntity):
    def __init__(
        self,
        name: str,
        abbreviation: str,
        zone: str,
        description: str,
        location: str,
        owner: dict,
        tags: list,
    ):
        super().__init__(name, abbreviation, zone, description, location, owner, tags)
        self.patterns = []
        self.data_products = []

    def add_pattern(self, pattern):
        self.patterns.append(pattern)

    def add_data_product(self, data_product):
        self.data_products.append(data_product)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Abbreviation: {self.abbreviation}")
        print(f"Zone: {self.zone}")
        print(f"Description: {self.description}")
        print(f"Location: {self.location}")
        print(f"Owner: {self.owner}")
        print(f"Tags: {self.tags}")
        print(f"Patterns: {self.patterns}")
        print(f"Data Products: {self.data_products}")
