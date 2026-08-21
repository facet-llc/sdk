from enum import Enum

class JwkUse(str, Enum):
    SIG = "sig"

    def __str__(self) -> str:
        return str(self.value)
