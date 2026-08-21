from enum import Enum

class VerificationMethod(str, Enum):
    DNS = "dns"
    WELL_KNOWN = "well-known"

    def __str__(self) -> str:
        return str(self.value)
