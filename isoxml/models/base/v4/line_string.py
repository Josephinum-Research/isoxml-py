from dataclasses import dataclass, field
from enum import Enum

from isoxml.models.base.v4.point import Point


class LineStringType(Enum):
    PolygonExterior = '1'
    PolygonInterior = '2'
    TramLine = '3'
    SamplingRoute = '4'
    GuidancePattern = '5'
    Drainage = '6'
    Fence = '7'
    Flag = '8'
    Obstacle = '9'


@dataclass
class LineString:
    """
    LineString.

    :ivar points: PNT
    :ivar type: A, (required)
    :ivar designator: B
    :ivar width: C
    :ivar length: D
    :ivar colour: E
    :ivar id: F
    """

    class Meta:
        name = "LSG"

    points: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "PNT",
            "full_name": "Point",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    type: None | LineStringType = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "LineStringType",
            "type": "Attribute",
            "required": True,
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "LineStringDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    width: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "LineStringWidth",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    length: None | int = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "LineStringLength",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    colour: None | int = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "LineStringColour",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "LineStringId",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(LSG|LSG-)([0-9])+",
        },
    )
