from dataclasses import dataclass, field
from enum import Enum

from isoxml.models.base.v3.point import Point


class LineStringType(Enum):
    PolygonExterior = "1"
    PolygonInterior = "2"
    TramLine = "3"
    SamplingRoute = "4"
    GuidancePath = "5"
    Drainage = "6"
    Fence = "7"
    Flag = "8"


@dataclass
class LineString:
    """
    Linestring.

    :ivar points: PNT
    :ivar type: A, (required)
    :ivar designator: B
    :ivar width: C
    :ivar length: D
    :ivar colour: E
    """

    class Meta:
        name = "LSG"

    points: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "PNT",
            "full_name": "Point",
            "type": "Element",
            "min_occurs": 2,
        },
    )
    type: None | LineStringType = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "LinestringType",
            "type": "Attribute",
            "required": True,
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "LinestringDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    width: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "LinestringWidth",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    length: None | int = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "LinestringLength",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    colour: None | int = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "LinestringColour",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
