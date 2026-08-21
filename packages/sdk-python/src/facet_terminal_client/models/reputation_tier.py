from enum import Enum

class ReputationTier(str, Enum):
    GOOD = "good"
    NORMAL = "normal"
    POOR = "poor"
    TRUSTED = "trusted"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
