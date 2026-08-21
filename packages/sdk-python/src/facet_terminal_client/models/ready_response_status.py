from enum import Enum

class ReadyResponseStatus(str, Enum):
    NOT_READY = "not_ready"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
