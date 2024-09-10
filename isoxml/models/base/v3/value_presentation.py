from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class ValuePresentation:
    """
    ValuePresentation.

    :ivar id: A, (required)
    :ivar offset: B, (required)
    :ivar scale: C, (required)
    :ivar number_of_decimals: D, (required)
    :ivar unit_designator: E
    :ivar colour_legend_id_ref: F
    """

    class Meta:
        name = "VPN"

    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "ValuePresentationId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(VPN|VPN-)([0-9])+",
        },
    )
    offset: None | int = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "Offset",
            "type": "Attribute",
            "required": True,
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )
    scale: None | Decimal = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "Scale",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("1E-9"),
            "max_inclusive": Decimal("100000000.0"),
        },
    )
    number_of_decimals: None | int = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "NumberOfDecimals",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 7,
        },
    )
    unit_designator: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "UnitDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    colour_legend_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "ColourLegendIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CLD|CLD-)([0-9])+",
        },
    )
