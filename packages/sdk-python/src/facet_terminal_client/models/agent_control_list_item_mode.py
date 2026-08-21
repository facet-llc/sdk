from enum import Enum

class AgentControlListItemMode(str, Enum):
    ALLOWED = "allowed"
    BLOCKED = "blocked"
    THROTTLED = "throttled"

    def __str__(self) -> str:
        return str(self.value)
