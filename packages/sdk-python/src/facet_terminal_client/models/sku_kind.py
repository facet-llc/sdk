from enum import Enum

class SkuKind(str, Enum):
    DIGITAL = "digital"
    PHYSICAL = "physical"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
