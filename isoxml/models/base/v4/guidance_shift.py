from dataclasses import dataclass, field

from isoxml.models.base.v4.allocation_stamp import AllocationStamp


@dataclass
class GuidanceShift:
    """
    GuidanceShift.

    :ivar allocation_stamp: ASP
    :ivar guidance_group_id_ref: A
    :ivar guidance_pattern_id_ref: B
    :ivar guidance_east_shift: C
    :ivar guidance_north_shift: D
    :ivar propagation_offset: E
    """

    class Meta:
        name = "GST"

    allocation_stamp: None | AllocationStamp = field(
        default=None,
        metadata={
            "name": "ASP",
            "full_name": "AllocationStamp",
            "type": "Element",
        },
    )
    guidance_group_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "GuidanceGroupIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(GGP|GGP-)([0-9])+",
        },
    )
    guidance_pattern_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "GuidancePatternIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(GPN|GPN-)([0-9])+",
        },
    )
    guidance_east_shift: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "GuidanceEastShift",
            "type": "Attribute",
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )
    guidance_north_shift: None | int = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "GuidanceNorthShift",
            "type": "Attribute",
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )
    propagation_offset: None | int = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "PropagationOffset",
            "type": "Attribute",
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )
