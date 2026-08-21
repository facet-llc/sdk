from enum import Enum

class SubscriptionStatus(str, Enum):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
