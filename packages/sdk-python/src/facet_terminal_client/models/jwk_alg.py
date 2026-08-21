from enum import Enum

class JwkAlg(str, Enum):
    EDDSA = "EdDSA"

    def __str__(self) -> str:
        return str(self.value)
