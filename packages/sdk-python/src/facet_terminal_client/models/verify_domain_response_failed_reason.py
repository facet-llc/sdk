from enum import Enum

class VerifyDomainResponseFailedReason(str, Enum):
    FETCH_FAILED = "fetch_failed"
    MISMATCH = "mismatch"

    def __str__(self) -> str:
        return str(self.value)
