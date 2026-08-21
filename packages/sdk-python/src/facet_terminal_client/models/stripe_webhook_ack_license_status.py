from enum import Enum

class StripeWebhookAckLicenseStatus(str, Enum):
    FAILED = "failed"
    REFUNDED = "refunded"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
