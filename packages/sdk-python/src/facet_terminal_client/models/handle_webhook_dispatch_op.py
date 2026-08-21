from enum import Enum

class HandleWebhookDispatchOp(str, Enum):
    HANDLE_WEBHOOK = "handle_webhook"

    def __str__(self) -> str:
        return str(self.value)
