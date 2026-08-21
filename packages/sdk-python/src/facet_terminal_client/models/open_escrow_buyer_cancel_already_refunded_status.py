from enum import Enum

class OpenEscrowBuyerCancelAlreadyRefundedStatus(str, Enum):
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
