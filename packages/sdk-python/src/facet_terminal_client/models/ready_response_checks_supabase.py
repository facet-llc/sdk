from enum import Enum

class ReadyResponseChecksSupabase(str, Enum):
    FAIL = "fail"
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
