from enum import Enum

class SettlementState(str, Enum):
    CONFIRMED = "confirmed"
    FAILED = "failed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
