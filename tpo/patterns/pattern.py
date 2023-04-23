from abc import ABC, abstractmethod

class Pattern(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_metadata(self):
        pass

    @abstractmethod
    def get_definition(self):
        pass

class Ingestion(Pattern):
    pass

class Transformation(Pattern):
    pass

class Serving(Pattern):
    pass
