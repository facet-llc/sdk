from enum import Enum

class ReserveAuthorityDispatchOp(str, Enum):
    RESERVE_AUTHORITY = "reserve_authority"

    def __str__(self) -> str:
        return str(self.value)
