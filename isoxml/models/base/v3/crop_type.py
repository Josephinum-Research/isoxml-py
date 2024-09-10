from dataclasses import dataclass, field

from isoxml.models.base.v3.crop_variety import CropVariety


@dataclass
class CropType:
    """
    CropType.

    :ivar crop_varieties: CVT
    :ivar id: A, (required)
    :ivar designator: B, (required)
    """

    class Meta:
        name = "CTP"

    crop_varieties: list[CropVariety] = field(
        default_factory=list,
        metadata={
            "name": "CVT",
            "full_name": "CropVariety",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "CropTypeId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CTP|CTP-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "CropTypeDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
