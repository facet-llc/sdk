from enum import Enum

class ReservationStatus(str, Enum):
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    RESERVED = "reserved"
    SETTLED = "settled"

    def __str__(self) -> str:
        return str(self.value)
