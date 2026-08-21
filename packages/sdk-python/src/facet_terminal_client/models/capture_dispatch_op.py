from enum import Enum

class CaptureDispatchOp(str, Enum):
    CAPTURE = "capture"

    def __str__(self) -> str:
        return str(self.value)
