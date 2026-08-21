from enum import Enum

class OrderAuthorizationRecordLeg(str, Enum):
    COMPLETE = "complete"
    CREATE = "create"

    def __str__(self) -> str:
        return str(self.value)
