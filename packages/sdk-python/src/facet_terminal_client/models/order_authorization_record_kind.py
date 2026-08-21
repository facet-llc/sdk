from enum import Enum

class OrderAuthorizationRecordKind(str, Enum):
    AUTONOMOUS_DELEGATION = "autonomous_delegation"
    BOSON_SELLER_OFFER = "boson_seller_offer"
    KYA = "kya"
    KYA_BUYER = "kya_buyer"
    KYA_OWNER = "kya_owner"
    UCP_PLATFORM_RFC9421 = "ucp_platform_rfc9421"
    X402_BUYER_ERC3009 = "x402_buyer_erc3009"

    def __str__(self) -> str:
        return str(self.value)
