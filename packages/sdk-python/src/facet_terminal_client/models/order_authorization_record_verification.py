from enum import Enum

class OrderAuthorizationRecordVerification(str, Enum):
    ATTESTED = "attested"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
