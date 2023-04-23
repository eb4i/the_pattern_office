class DataDomain:
    def __init__(self, name, abbreviation, zone, description, location, owner, tags, patterns=None, data_products=None):
        self.name = name
        self.abbreviation = abbreviation
        self.zone = zone
        self.description = description
        self.location = location
        self.owner = owner
        self.tags = tags
        self.patterns = patterns or []
        self.data_products = data_products or []

    def add_pattern(self, pattern):
        self.patterns.append(pattern)

    def add_data_product(self, data_product):
        self.data_products.append(data_product)

    def __str__(self):
        patterns_str = ', '.join(self.patterns)
        data_products_str = ', '.join(self.data_products)
        tags_str = ', '.join(self.tags)

        return (f"Data Domain: {self.name}\n"
                f"Abbreviation: {self.abbreviation}\n"
                f"Zone: {self.zone}\n"
                f"Description: {self.description}\n"
                f"Location: {self.location}\n"
                f"Owner: {self.owner['name']} ({self.owner['email']})\n"
                f"Tags: {tags_str}\n"
                f"Patterns: {patterns_str}\n"
                f"Data Products: {data_products_str}")

