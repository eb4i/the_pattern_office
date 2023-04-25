# An abstract Base Data Entity class that will be used to create Data Domain, Data Product, and Pattern classes
from abc import ABC, abstractmethod

class BaseDataEntity(ABC):
    def __init__(self, config_manager, name, abbreviation, zone, description, distribution, version, location, owner, tags):
        self.config_manager = config_manager
        self.config = None
        self.name = name
        self.abbreviation = abbreviation
        self.zone = zone
        self.description = description
        self.distribution = distribution
        self.version = version
        self.location = location
        self.owner = owner
        self.tags = tags
    
    @abstractmethod
    def display(self):
        pass

    # @abstractmethod
    # def load(self):
    #     pass

    # @abstractmethod
    # def save(self):
    #     pass

    # @abstractmethod
    # def create(self):
    #     pass

    # @abstractmethod
    # def update(self):
    #     pass

    # @abstractmethod
    # def delete(self):
    #     pass

    # @abstractmethod
    # def get(self):
    #     pass

    # @abstractmethod
    # def set(self):
    #     pass
