# tpo/domain/data_domain.py
from tpo.application.pattern_factory import PatternFactory

class DataDomain:
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
        self.name = name
        self.abbreviation = abbreviation
        self.zone = zone
        self.description = description
        self.location = location
        self.owner = owner
        self.tags = tags
        self.patterns = []
        self.data_products = []
        self.pattern_factory = PatternFactory()

    def add_pattern(self, pattern):
        self.patterns.append(pattern)

    def add_data_product(self, data_product):
        self.data_products.append(data_product)

    def load_pattern(self, pattern_name: str, *args, **kwargs):
        pattern_instance = self.pattern_factory.create_pattern(pattern_name, *args, **kwargs)
        self.add_pattern(pattern_instance)

    def __str__(self):
        return (
            f"DataDomain(name={self.name}, abbreviation={self.abbreviation}, "
            f"zone={self.zone}, description={self.description}, location={self.location}, "
            f"owner={self.owner}, tags={self.tags}, patterns={self.patterns}, "
            f"data_products={self.data_products})"
        )
