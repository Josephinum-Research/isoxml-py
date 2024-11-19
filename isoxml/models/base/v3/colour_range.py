from dataclasses import dataclass, field


@dataclass
class ColourRange:
    """
    ColourRange.

    :ivar minimum_value: A, (required)
    :ivar maximum_value: B, (required)
    :ivar colour: C, (required)
    """

    class Meta:
        name = "CRG"

    minimum_value: None | int = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "MinimumValue",
            "type": "Attribute",
            "required": True,
            "min_inclusive": -2147483647,
            "max_inclusive": 2147483647,
        },
    )
    maximum_value: None | int = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "MaximumValue",
            "type": "Attribute",
            "required": True,
            "min_inclusive": -2147483647,
            "max_inclusive": 2147483647,
        },
    )
    colour: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "Colour",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
