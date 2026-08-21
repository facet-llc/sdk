from enum import Enum

class CapabilitiesResponseFulfillmentModesItem(str, Enum):
    CIPHERTEXT = "ciphertext"
    INLINE = "inline"
    REF = "ref"

    def __str__(self) -> str:
        return str(self.value)
