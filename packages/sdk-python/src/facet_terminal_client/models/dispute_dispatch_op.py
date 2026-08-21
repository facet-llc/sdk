from enum import Enum

class DisputeDispatchOp(str, Enum):
    DISPUTE = "dispute"

    def __str__(self) -> str:
        return str(self.value)
