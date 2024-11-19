from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class DeviceValuePresentation:
    """
    DeviceValuePresentation.

    :ivar object_id: A, (required)
    :ivar offset: B, (required)
    :ivar scale: C, (required)
    :ivar number_of_decimals: D, (required)
    :ivar unit_designator: E
    """

    class Meta:
        name = "DVP"

    object_id: None | int = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "DeviceValuePresentationObjectId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 65534,
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
