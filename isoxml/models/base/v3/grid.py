from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum


class GridType(Enum):
    GridType1 = "1"
    GridType2 = "2"


@dataclass
class Grid:
    """
    Grid.

    :ivar minimum_north_position: A, (required)
    :ivar minimum_east_position: B, (required)
    :ivar cell_north_size: C, (required)
    :ivar cell_east_size: D, (required)
    :ivar maximum_column: E, (required)
    :ivar maximum_row: F, (required)
    :ivar filename: G, (required)
    :ivar filelength: H
    :ivar type: I, (required)
    :ivar treatment_zone_code: J
    """

    class Meta:
        name = "GRD"

    minimum_north_position: None | Decimal = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "GridMinimumNorthPosition",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("-90.0"),
            "max_inclusive": Decimal("90.0"),
        },
    )
    minimum_east_position: None | Decimal = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "GridMinimumEastPosition",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("-180.0"),
            "max_inclusive": Decimal("180.0"),
        },
    )
    cell_north_size: None | float = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "GridCellNorthSize",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
    cell_east_size: None | float = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "GridCellEastSize",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
    maximum_column: None | int = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "GridMaximumColumn",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 4294967295,
        },
    )
    maximum_row: None | int = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "GridMaximumRow",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 4294967295,
        },
    )
    filename: None | str = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "Filename",
            "type": "Attribute",
            "required": True,
            "length": 8,
            "pattern": r"GRD[0-9][0-9][0-9][0-9][0-9]",
        },
    )
    filelength: None | int = field(
        default=None,
        metadata={
            "name": "H",
            "full_name": "Filelength",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    type: None | GridType = field(
        default=None,
        metadata={
            "name": "I",
            "full_name": "GridType",
            "type": "Attribute",
            "required": True,
        },
    )
    treatment_zone_code: None | int = field(
        default=None,
        metadata={
            "name": "J",
            "full_name": "TreatmentZoneCode",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
