from enum import Enum

class UcpDisputeRequestDisputeLineItemsItemAction(str, Enum):
    ESCALATE = "escalate"
    RAISE = "raise"
    RETRACT = "retract"

    def __str__(self) -> str:
        return str(self.value)
