from enum import Enum

class OpenEscrowBuyerCancelAlreadyRefundedPhase(str, Enum):
    ALREADY_REFUNDED = "already_refunded"

    def __str__(self) -> str:
        return str(self.value)
