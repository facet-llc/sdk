from enum import Enum

class RfqQuoteStatus(str, Enum):
    ACCEPTED = "accepted"
    EXPIRED = "expired"
    LIVE = "live"
    REJECTED = "rejected"
    SUPERSEDED = "superseded"

    def __str__(self) -> str:
        return str(self.value)
