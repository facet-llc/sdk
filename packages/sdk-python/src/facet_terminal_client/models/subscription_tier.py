from enum import Enum

class SubscriptionTier(str, Enum):
    ENTERPRISE = "enterprise"
    PRO = "pro"
    PRO_PLUS = "pro_plus"
    STARTER = "starter"

    def __str__(self) -> str:
        return str(self.value)
