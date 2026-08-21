from enum import Enum

class CalendlyWebhookAckIgnoredAction(str, Enum):
    IGNORED = "ignored"

    def __str__(self) -> str:
        return str(self.value)
