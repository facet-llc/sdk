from enum import Enum

class CalendlyWebhookAckConfirmedAction(str, Enum):
    CONFIRMED = "confirmed"

    def __str__(self) -> str:
        return str(self.value)
