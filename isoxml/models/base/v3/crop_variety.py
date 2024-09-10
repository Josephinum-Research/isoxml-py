from dataclasses import dataclass, field


@dataclass
class CropVariety:
    """
    CropVariety.

    :ivar id: A, (required)
    :ivar designator: B, (required)
    """

    class Meta:
        name = "CVT"

    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "CropVarietyId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CVT|CVT-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "CropVarietyDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
