from enum import Enum

class OpenEscrowBuyerCancelOpenDisputeStatus(str, Enum):
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
