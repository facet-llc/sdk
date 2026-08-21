from enum import Enum

class ProofKind(str, Enum):
    AGE = "age"
    JURISDICTION = "jurisdiction"
    KYC = "kyc"
    LICENSE = "license"
    LICENSE_EXPORT = "license_export"
    PRESCRIPTION = "prescription"

    def __str__(self) -> str:
        return str(self.value)
