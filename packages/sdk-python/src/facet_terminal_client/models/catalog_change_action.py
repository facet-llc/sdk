from enum import Enum

class CatalogChangeAction(str, Enum):
    ADDED = "added"
    REMOVED = "removed"
    RESTOCKED = "restocked"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
