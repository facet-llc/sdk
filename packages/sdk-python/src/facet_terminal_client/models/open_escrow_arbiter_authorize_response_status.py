from enum import Enum

class OpenEscrowArbiterAuthorizeResponseStatus(str, Enum):
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
