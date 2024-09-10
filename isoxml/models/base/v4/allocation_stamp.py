from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDateTime

from isoxml.models.base.v4.position import Position


class AllocationStampType(Enum):
    Planned = '1'
    EffectiveRealized = '4'


@dataclass
class AllocationStamp:
    """
    AllocationStamp.

    :ivar positions: PTN
    :ivar start: A, (required)
    :ivar stop: B
    :ivar duration: C
    :ivar type: D, (required)
    """

    class Meta:
        name = "ASP"

    positions: list[Position] = field(
        default_factory=list,
        metadata={
            "name": "PTN",
            "full_name": "Position",
            "type": "Element",
            "max_occurs": 2,
        },
    )
    start: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "Start",
            "type": "Attribute",
            "required": True,
        },
    )
    stop: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "Stop",
            "type": "Attribute",
        },
    )
    duration: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "Duration",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    type: None | AllocationStampType = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
