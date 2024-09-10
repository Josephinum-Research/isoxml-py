from dataclasses import dataclass, field

from isoxml.models.base.v4.guidance_pattern import GuidancePattern
from isoxml.models.base.v4.polygon import Polygon


@dataclass
class GuidanceGroup:
    """
    GuidanceGroup.

    :ivar guidance_patterns: GPN
    :ivar boundary_polygons: PLN
    :ivar id: A, (required)
    :ivar designator: B
    """

    class Meta:
        name = "GGP"

    guidance_patterns: list[GuidancePattern] = field(
        default_factory=list,
        metadata={
            "name": "GPN",
            "full_name": "GuidancePattern",
            "type": "Element",
        },
    )
    boundary_polygons: list[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "PLN",
            "full_name": "BoundaryPolygon",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "GuidanceGroupId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(GGP|GGP-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "GuidanceGroupDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
