from dataclasses import dataclass, field
from enum import Enum


class ProductGroupType(Enum):
    ProductGroup = "1"
    CropType = "2"

@dataclass
class ProductGroup:
    """
    ProductGroup.

    :ivar id: A, (required)
    :ivar designator: B, (required)
    :ivar type: C
    """

    class Meta:
        name = "PGP"

    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "ProductGroupId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(PGP|PGP-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "ProductGroupDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
    type: None | ProductGroupType = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "ProductGroupType",
            "type": "Attribute",
        },
    )



