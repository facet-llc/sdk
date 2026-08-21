from enum import Enum

class KgRelation(str, Enum):
    CITES = "cites"
    COMPETES_WITH = "competes_with"
    COMPLIES_WITH = "complies_with"
    DERIVED_FROM = "derived_from"
    LICENSED_BY = "licensed_by"
    LOCATED_IN = "located_in"
    OWNS = "owns"
    REFERENCES = "references"
    SAME_CORRIDOR = "same_corridor"
    SAME_NAICS = "same_naics"
    SAME_ZIP = "same_zip"
    SEMANTICALLY_SIMILAR_TO = "semantically_similar_to"
    SUPPLIES = "supplies"

    def __str__(self) -> str:
        return str(self.value)
