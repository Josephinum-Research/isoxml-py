from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class BaseStation:
    """
    BaseStation.

    :ivar id: A, (required)
    :ivar designator: B, (required)
    :ivar north: C, (required)
    :ivar east: D, (required)
    :ivar up: E, (required)
    """

    class Meta:
        name = "BSN"

    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "BaseStationId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(BSN|BSN-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "BaseStationDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
    north: None | Decimal = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "BaseStationNorth",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("-90.0"),
            "max_inclusive": Decimal("90.0"),
            "fraction_digits": 9,
        },
    )
    east: None | Decimal = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "BaseStationEast",
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
            "full_name": "BaseStationUp",
            "type": "Attribute",
            "required": True,
            "min_inclusive": -2147483647,
            "max_inclusive": 2147483647,
        },
    )
