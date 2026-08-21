from enum import Enum

class EscalationStatus(str, Enum):
    ACKNOWLEDGED = "acknowledged"
    CLOSED = "closed"
    IN_PROGRESS = "in_progress"
    OPEN = "open"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
