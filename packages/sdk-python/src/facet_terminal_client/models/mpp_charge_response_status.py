from enum import Enum

class MppChargeResponseStatus(str, Enum):
    SETTLED = "settled"

    def __str__(self) -> str:
        return str(self.value)
