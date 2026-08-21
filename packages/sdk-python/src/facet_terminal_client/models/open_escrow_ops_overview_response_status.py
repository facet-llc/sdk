from enum import Enum

class OpenEscrowOpsOverviewResponseStatus(str, Enum):
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
