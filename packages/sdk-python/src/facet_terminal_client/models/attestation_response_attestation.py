from enum import Enum

class AttestationResponseAttestation(str, Enum):
    CANNOT_FULFIL = "cannot_fulfil"
    FULFILLED = "fulfilled"
    NOT_RECEIVED = "not_received"
    RECEIVED = "received"

    def __str__(self) -> str:
        return str(self.value)
