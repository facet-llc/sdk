from enum import Enum

class OpenEscrowBuyerCancelResolveDisputeStatus(str, Enum):
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
