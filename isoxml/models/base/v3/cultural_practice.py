from dataclasses import dataclass, field

from isoxml.models.base.v3.operation_technique_reference import OperationTechniqueReference


@dataclass
class CulturalPractice:
    """
    CulturalPractice.

    :ivar operation_technique_references: OTR
    :ivar id: A, (required)
    :ivar designator: B, (required)
    """

    class Meta:
        name = "CPC"

    operation_technique_references: list[OperationTechniqueReference] = field(
        default_factory=list,
        metadata={
            "name": "OTR",
            "full_name": "OperationTechniqueReference",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "CulturalPracticeId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CPC|CPC-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "CulturalPracticeDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
