from enum import Enum

class OpenEscrowSellerRevokeAlreadyRefundedRevokeStatus(str, Enum):
    ALREADY_REFUNDED = "already_refunded"

    def __str__(self) -> str:
        return str(self.value)
