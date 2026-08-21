from enum import Enum

class FacetPublicKeyAlg(str, Enum):
    ED25519 = "Ed25519"

    def __str__(self) -> str:
        return str(self.value)
