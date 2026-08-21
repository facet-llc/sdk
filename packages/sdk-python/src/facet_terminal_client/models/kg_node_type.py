from enum import Enum

class KgNodeType(str, Enum):
    AGENT = "agent"
    BATCH = "batch"
    BUSINESS = "business"
    CAPABILITY = "capability"
    CERTIFICATION = "certification"
    CONCEPT = "concept"
    CONSTRAINT = "constraint"
    CORRIDOR = "corridor"
    FORMULATION = "formulation"
    INGREDIENT = "ingredient"
    JURISDICTION = "jurisdiction"
    LICENSE_TYPE = "license_type"
    MODULE = "module"
    NAICS_CLASS = "naics_class"
    REGULATION = "regulation"
    SKILL = "skill"
    TOOL_REF = "tool_ref"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
