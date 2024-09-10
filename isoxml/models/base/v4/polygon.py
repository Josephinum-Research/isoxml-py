from dataclasses import dataclass, field
from enum import Enum

from isoxml.models.base.v4.line_string import LineString


class PolygonType(Enum):
    PartfieldBoundary = '1'
    TreatmentZone = '2'
    WaterSurface = '3'
    Building = '4'
    Road = '5'
    Obstacle = '6'
    Flag = '7'
    Other = '8'
    Mainfield = '9'
    Headland = '10'
    BufferZone = '11'
    Windbreak = '12'


@dataclass
class Polygon:
    """
    Polygon.

    :ivar line_strings: LSG
    :ivar type: A, (required)
    :ivar designator: B
    :ivar area: C
    :ivar colour: D
    :ivar id: E
    """

    class Meta:
        name = "PLN"

    line_strings: list[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LSG",
            "full_name": "LineString",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    type: None | PolygonType = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "PolygonType",
            "type": "Attribute",
            "required": True,
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "PolygonDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    area: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "PolygonArea",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    colour: None | int = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "PolygonColour",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "PolygonId",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(PLN|PLN-)([0-9])+",
        },
    )
