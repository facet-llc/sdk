from enum import Enum

class StripeWebhookAckSubscriptionUpdatedStatus(str, Enum):
    ACTIVE = "active"
    CANCELED = "canceled"
    INCOMPLETE = "incomplete"
    PAST_DUE = "past_due"

    def __str__(self) -> str:
        return str(self.value)
