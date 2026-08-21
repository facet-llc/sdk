from enum import Enum

class WebhookEvent(str, Enum):
    AUCTION_BID_OUTBID = "auction.bid_outbid"
    AUCTION_ENDED_NO_SALE = "auction.ended_no_sale"
    AUCTION_ENDING_SOON = "auction.ending_soon"
    AUCTION_LOST = "auction.lost"
    AUCTION_WON = "auction.won"
    BOOKING_CANCELLED = "booking.cancelled"
    BOOKING_CONFIRMED = "booking.confirmed"
    DOCUMENT_AVAILABLE = "document.available"
    INVENTORY_RESTOCKED = "inventory.restocked"
    LICENSE_CONSUMED = "license.consumed"
    LICENSE_PURCHASED = "license.purchased"
    ORDER_REFUND_REQUESTED = "order.refund_requested"
    ORDER_SETTLED = "order.settled"
    ORDER_SHIPPED = "order.shipped"
    PRICE_CHANGED = "price.changed"
    RFQ_CANCELLED = "rfq.cancelled"
    RFQ_QUOTE_ACCEPTED = "rfq.quote_accepted"
    RFQ_QUOTE_RECEIVED = "rfq.quote_received"
    SUBSCRIPTION_PRICE_BREAKER_TRIPPED = "subscription.price_breaker_tripped"
    SUBSCRIPTION_RUN_FAILED = "subscription.run_failed"
    SUBSCRIPTION_RUN_SETTLED = "subscription.run_settled"

    def __str__(self) -> str:
        return str(self.value)
