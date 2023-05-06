from enum import Enum, auto
from dataclasses import dataclass, field

class Kind(Enum):
    DOMAIN = auto()
    PRODUCT = auto()
    PATTERN = auto()

@dataclass
class BaseConfig:
    name: str
    kind: Kind
    tags: list[str] = field(default_factory=list)
    version: str = ""
    location: str = ""
    owner: str = ""
    description: str = ""

    def build(self) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self.name} ({self.kind.name})"
