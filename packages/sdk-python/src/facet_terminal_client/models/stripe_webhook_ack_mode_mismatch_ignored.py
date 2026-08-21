from enum import Enum

class StripeWebhookAckModeMismatchIgnored(str, Enum):
    MODE_MISMATCH = "mode_mismatch"

    def __str__(self) -> str:
        return str(self.value)
