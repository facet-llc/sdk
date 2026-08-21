from enum import Enum

class DisputeDispatchDisputeAction(str, Enum):
    ACCEPT = "accept"
    CHALLENGE = "challenge"

    def __str__(self) -> str:
        return str(self.value)
