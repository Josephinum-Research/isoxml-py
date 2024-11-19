from dataclasses import dataclass, field

from isoxml.models.base.v4.allocation_stamp import AllocationStamp
from isoxml.models.base.v4.guidance_shift import GuidanceShift


@dataclass
class GuidanceAllocation:
    """
    GuidanceAllocation.

    :ivar allocation_stamps: ASP
    :ivar guidance_shifts: GST
    :ivar guidance_group_id_ref: A, (required)
    """

    class Meta:
        name = "GAN"

    allocation_stamps: list[AllocationStamp] = field(
        default_factory=list,
        metadata={
            "name": "ASP",
            "full_name": "AllocationStamp",
            "type": "Element",
        },
    )
    guidance_shifts: list[GuidanceShift] = field(
        default_factory=list,
        metadata={
            "name": "GST",
            "full_name": "GuidanceShift",
            "type": "Element",
        },
    )
    guidance_group_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "GuidanceGroupIdRef",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(GGP|GGP-)([0-9])+",
        },
    )
