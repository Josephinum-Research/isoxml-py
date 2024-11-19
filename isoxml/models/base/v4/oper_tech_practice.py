from dataclasses import dataclass, field


@dataclass
class OperTechPractice:
    """
    OperTechPractice.

    :ivar cultural_practice_id_ref: A, (required)
    :ivar operation_technique_id_ref: B
    """

    class Meta:
        name = "OTP"

    cultural_practice_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "CulturalPracticeIdRef",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CPC|CPC-)([0-9])+",
        },
    )
    operation_technique_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "OperationTechniqueIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(OTQ|OTQ-)([0-9])+",
        },
    )
