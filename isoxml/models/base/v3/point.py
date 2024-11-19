from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum


class PointType(Enum):
    Flag = "1"
    Other = "2"


@dataclass
class Point:
    """
    Point.

    :ivar type: A, (required)
    :ivar designator: B
    :ivar north: C, (required)
    :ivar east: D, (required)
    :ivar up: E
    :ivar colour: F
    """

    class Meta:
        name = "PNT"

    type: None | PointType = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "PointType",
            "type": "Attribute",
            "required": True,
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "PointDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    north: None | Decimal = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "PointNorth",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("-90.0"),
            "max_inclusive": Decimal("90.0"),
        },
    )
    east: None | Decimal = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "PointEast",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("-180.0"),
            "max_inclusive": Decimal("180.0"),
        },
    )
    up: None | int = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "PointUp",
            "type": "Attribute",
            "min_inclusive": -2147483647,
            "max_inclusive": 2147483647,
        },
    )
    colour: None | int = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "PointColour",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
