from enum import Enum

class OpenEscrowBuyerCancelOpenDisputePhase(str, Enum):
    OPEN_DISPUTE = "open_dispute"

    def __str__(self) -> str:
        return str(self.value)
