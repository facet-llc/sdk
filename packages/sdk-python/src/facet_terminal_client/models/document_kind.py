from enum import Enum

class DocumentKind(str, Enum):
    COA = "coa"
    LABEL = "label"
    OTHER = "other"
    SDS = "sds"
    SPEC_SHEET = "spec_sheet"

    def __str__(self) -> str:
        return str(self.value)
