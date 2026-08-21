from enum import Enum

class MerchantAttestation(str, Enum):
    CANNOT_FULFIL = "cannot_fulfil"
    FULFILLED = "fulfilled"

    def __str__(self) -> str:
        return str(self.value)
