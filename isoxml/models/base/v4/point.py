from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum


class PointType(Enum):
    Flag = '1'
    Other = '2'
    FieldAccess = '3'
    Storage = '4'
    Obstacle = '5'
    GuidanceReferenceA = '6'
    GuidanceReferenceB = '7'
    GuidanceReferenceCenter = '8'
    GuidancePoint = '9'
    PartfieldReferencePoint = '10'
    Homebase = '11'


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
    :ivar id: G
    :ivar horizontal_accuracy: H
    :ivar vertical_accuracy: I
    :ivar filename: J
    :ivar filelength: K
    """

    class Meta:
        name = "PNT"

    type: None | str | PointType = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "PointType",
            "type": "Attribute",
            "required": True,
            "length": 0,
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
    north: None | str | Decimal = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "PointNorth",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("-90.0"),
            "max_inclusive": Decimal("90.0"),
            "fraction_digits": 9,
        },
    )
    east: None | str | Decimal = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "PointEast",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("-180.0"),
            "max_inclusive": Decimal("180.0"),
            "fraction_digits": 9,
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
    colour: None | str = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "PointColour",
            "type": "Attribute",
            "length": 0,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "PointId",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(PNT|PNT-)([0-9])+",
        },
    )
    horizontal_accuracy: None | str | Decimal = field(
        default=None,
        metadata={
            "name": "H",
            "full_name": "PointHorizontalAccuracy",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("65.0"),
        },
    )
    vertical_accuracy: None | str | Decimal = field(
        default=None,
        metadata={
            "name": "I",
            "full_name": "PointVerticalAccuracy",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("65.0"),
        },
    )
    filename: None | str = field(
        default=None,
        metadata={
            "name": "J",
            "full_name": "Filename",
            "type": "Attribute",
            "length": 8,
            "pattern": r"PNT([0-9]){5}",
        },
    )
    filelength: None | int = field(
        default=None,
        metadata={
            "name": "K",
            "full_name": "Filelength",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
