from enum import Enum

class OrderSignatureRecordParty(str, Enum):
    AGENT = "agent"
    FACET = "facet"
    MERCHANT = "merchant"

    def __str__(self) -> str:
        return str(self.value)
