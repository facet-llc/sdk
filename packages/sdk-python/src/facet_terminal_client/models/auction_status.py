from enum import Enum

class AuctionStatus(str, Enum):
    ENDED_NO_SALE = "ended_no_sale"
    ENDED_SOLD = "ended_sold"
    LIVE = "live"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
