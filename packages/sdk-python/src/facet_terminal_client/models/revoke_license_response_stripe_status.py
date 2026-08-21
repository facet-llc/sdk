from enum import Enum

class RevokeLicenseResponseStripeStatus(str, Enum):
    FAILED = "failed"
    PENDING = "pending"
    REFUNDED = "refunded"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
