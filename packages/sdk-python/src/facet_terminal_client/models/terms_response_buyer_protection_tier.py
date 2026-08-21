from enum import Enum

class TermsResponseBuyerProtectionTier(str, Enum):
    BONDED = "bonded"

    def __str__(self) -> str:
        return str(self.value)
