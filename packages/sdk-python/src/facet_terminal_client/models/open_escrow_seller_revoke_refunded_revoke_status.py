from enum import Enum

class OpenEscrowSellerRevokeRefundedRevokeStatus(str, Enum):
    REFUNDED = "refunded"

    def __str__(self) -> str:
        return str(self.value)
