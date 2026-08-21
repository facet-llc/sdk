from enum import Enum

class AttestationParty(str, Enum):
    AGENT = "agent"
    MERCHANT = "merchant"

    def __str__(self) -> str:
        return str(self.value)
