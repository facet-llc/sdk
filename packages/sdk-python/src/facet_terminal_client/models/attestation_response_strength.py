from enum import Enum

class AttestationResponseStrength(str, Enum):
    SIGNED = "signed"

    def __str__(self) -> str:
        return str(self.value)
