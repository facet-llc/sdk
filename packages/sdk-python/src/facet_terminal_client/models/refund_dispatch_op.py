from enum import Enum

class RefundDispatchOp(str, Enum):
    REFUND = "refund"

    def __str__(self) -> str:
        return str(self.value)
