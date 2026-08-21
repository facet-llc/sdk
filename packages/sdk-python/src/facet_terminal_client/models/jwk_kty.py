from enum import Enum

class JwkKty(str, Enum):
    OKP = "OKP"

    def __str__(self) -> str:
        return str(self.value)
