from enum import Enum

class CancelReservationResponseStatus(str, Enum):
    CANCELLED = "cancelled"

    def __str__(self) -> str:
        return str(self.value)
