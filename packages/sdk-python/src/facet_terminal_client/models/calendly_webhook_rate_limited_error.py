from enum import Enum

class CalendlyWebhookRateLimitedError(str, Enum):
    RATE_LIMITED = "rate_limited"

    def __str__(self) -> str:
        return str(self.value)
