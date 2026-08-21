from enum import Enum

class CatalogChangeKind(str, Enum):
    DOCUMENT = "document"
    INVENTORY = "inventory"
    MANIFEST = "manifest"
    PRICE = "price"
    PRODUCT = "product"

    def __str__(self) -> str:
        return str(self.value)
