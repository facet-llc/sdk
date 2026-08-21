from enum import Enum

class ReconcileSettlementOutcome(str, Enum):
    ADVANCED = "advanced"
    SKIPPED = "skipped"
    STILL_PENDING = "still_pending"

    def __str__(self) -> str:
        return str(self.value)
