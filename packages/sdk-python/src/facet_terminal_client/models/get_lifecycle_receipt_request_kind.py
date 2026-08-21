from enum import Enum

class GetLifecycleReceiptRequestKind(str, Enum):
    CANCEL = "cancel"
    DISPUTE = "dispute"
    REFUND = "refund"
    WITHDRAW = "withdraw"

    def __str__(self) -> str:
        return str(self.value)
