from enum import Enum

class RfqRequestStatus(str, Enum):
    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    COUNTERED = "countered"
    EXPIRED = "expired"
    OPEN = "open"
    QUOTED = "quoted"

    def __str__(self) -> str:
        return str(self.value)
