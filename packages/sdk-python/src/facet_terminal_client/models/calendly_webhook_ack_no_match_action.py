from enum import Enum

class CalendlyWebhookAckNoMatchAction(str, Enum):
    NO_MATCH = "no_match"

    def __str__(self) -> str:
        return str(self.value)
