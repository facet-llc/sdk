from enum import Enum

class OpenEscrowBuyerCancelResolveDisputePhase(str, Enum):
    RESOLVE_DISPUTE = "resolve_dispute"

    def __str__(self) -> str:
        return str(self.value)
