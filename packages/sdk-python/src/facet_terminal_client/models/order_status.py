from enum import Enum

class OrderStatus(str, Enum):
    CANCELLED = "cancelled"
    FULFILLED = "fulfilled"
    REFUNDED = "refunded"
    SETTLED = "settled"

    def __str__(self) -> str:
        return str(self.value)
