from enum import Enum

class RefundStatus(str, Enum):
    APPROVED = "approved"
    FULFILLED = "fulfilled"
    REJECTED = "rejected"
    REQUESTED = "requested"

    def __str__(self) -> str:
        return str(self.value)
