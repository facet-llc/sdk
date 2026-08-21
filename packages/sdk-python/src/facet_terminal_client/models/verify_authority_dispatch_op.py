from enum import Enum

class VerifyAuthorityDispatchOp(str, Enum):
    VERIFY_AUTHORITY = "verify_authority"

    def __str__(self) -> str:
        return str(self.value)
