from dataclasses import dataclass, field


@dataclass
class OperationTechnique:
    """
    OperationTechnique.

    :ivar id: A, (required)
    :ivar designator: B, (required)
    """

    class Meta:
        name = "OTQ"

    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "OperationTechniqueId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(OTQ|OTQ-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "OperationTechniqueDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
