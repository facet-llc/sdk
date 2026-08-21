from enum import Enum

class AgentAttestation(str, Enum):
    NOT_RECEIVED = "not_received"
    RECEIVED = "received"

    def __str__(self) -> str:
        return str(self.value)
