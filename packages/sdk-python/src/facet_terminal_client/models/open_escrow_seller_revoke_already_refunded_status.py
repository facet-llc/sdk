from enum import Enum

class OpenEscrowSellerRevokeAlreadyRefundedStatus(str, Enum):
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
