from enum import Enum

class ReserveResponseStatus(str, Enum):
    RESERVED = "reserved"

    def __str__(self) -> str:
        return str(self.value)
