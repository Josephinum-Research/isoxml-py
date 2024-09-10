from dataclasses import dataclass, field

from isoxml.models.base.v4.colour_range import ColourRange


@dataclass
class ColourLegend:
    """
    ColourLegend.

    :ivar colour_ranges: CRG
    :ivar id: A, (required)
    :ivar default_color: B
    """

    class Meta:
        name = "CLD"

    colour_ranges: list[ColourRange] = field(
        default_factory=list,
        metadata={
            "name": "CRG",
            "full_name": "ColourRange",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "ColourLegendId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CLD|CLD-)([0-9])+",
        },
    )
    default_color: None | int = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "DefaultColor",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
